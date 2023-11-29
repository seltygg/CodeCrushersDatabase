from django.shortcuts import render,redirect
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from django.db import connection
from django.contrib.auth.decorators import login_required
@login_required
def passingDashboardView(request):

    sql_query = """
    WITH QuizPassingScores AS (
        SELECT
            s.quizid,
            s.score,
            q.passingscore,
            q.certificateid
        FROM
            scores s
        JOIN
            quizzes q ON s.quizid = q.quizid
    )
    SELECT
        c.certificateid,
        c.name AS "Certificate Name",
        qps.quizid AS "Quiz ID",
        q.name AS "Quiz Name",
        q.passingscore AS "Quiz Passing Score",
        COUNT(qps.score) AS num_attempts,
        SUM(CASE WHEN qps.score >= qps.passingscore THEN 1 ELSE 0 END) AS num_passing_scores,
        ROUND(SUM(CASE WHEN qps.score >= qps.passingscore THEN 1 ELSE 0 END) * 100 / COUNT(qps.score), 2) AS passing_percentage
    FROM
        certificates c
    JOIN
        QuizPassingScores qps ON c.certificateid = qps.certificateid
    JOIN
        quizzes q ON qps.quizid = q.quizid
    GROUP BY
        c.certificateid, c.name, qps.quizid, q.name, q.passingscore
    ORDER BY
        passing_percentage DESC
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    df = pd.read_sql_query(sql_query, connection)
    fig = px.bar(df, x='Certificate Name', y='PASSING_PERCENTAGE', text='PASSING_PERCENTAGE',
                labels={'PASSING_PERCENTAGE': 'Passing Percentage (%)'},
                title='Passing Percentage for Certificates')
    fig.update_xaxes(tickangle=45, tickmode='array')
    graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
    context = {'graph': graph}
    return render(request, 'DashboardTemplates/passingPercentageDashboard.html', context)
@login_required
def topVoiceDashboardView(request):
    sql_query = """
    WITH f_count AS (SELECT ac.accountid accID, COUNT(DISTINCT fl.followerpageid) follower_counts
                    FROM accounts ac
                    JOIN  followings fl
                        ON ac.pageid = fl.followeepageid
                    GROUP BY (ac.accountid)),
    l_count AS (SELECT ac2.accountid accID, SUM(p.likecount) T_like_counts
                FROM accounts ac2
                JOIN posts p 
                    ON p.pagepostedid = ac2.pageid
                GROUP BY (ac2.accountid)),
      final_q AS (SELECT f_count.accID "Account No.",follower_counts, T_like_counts ,(follower_counts + T_like_counts) "Top Voice Metrics",
                DENSE_RANK() OVER(ORDER BY(follower_counts + T_like_counts)DESC) RANKING
        FROM f_count
        FULL OUTER JOIN l_count 
            ON f_count.accid = l_count.accid
        WHERE (follower_counts + T_like_counts) IS NOT NULL
        )
        
        SELECT (ius.fname||' '|| ius.lname) "Top Voice Owner", "Top Voice Metrics",RANKING
        FROM individual_users ius
        JOIN final_q fq
            ON fq."Account No." = ius.useraccountid
        FETCH FIRST 5 rows WITH TIES
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    df = pd.read_sql_query(sql_query, connection)
    fig = px.scatter(df, x='Top Voice Owner', y='Top Voice Metrics',
                 size='Top Voice Metrics', color='RANKING',
                 labels={'Top Voice Metrics': 'Metrics'},
                 title='Top Voice Metrics by Owner',
                 size_max=60)
    fig.update_xaxes(tickangle=45, tickmode='array')
    graph = fig.to_html(full_html=False, default_height=600, default_width=800)
    context = {'graph': graph}
    return render(request, 'DashboardTemplates/passingPercentageDashboard.html', context)
@login_required
def topMessagesDashboardView(request):
    sql_query = """
    WITH all_messages AS (
    SELECT
        IU.usertype,
        ROUND(COUNT(M.messageID)/(COUNT (DISTINCT M.mSenderID)),2) msgAvg,
        to_char(msgtimestamp, 'DY') Days
    FROM
        messages M
        JOIN individual_users IU ON M.mSenderID = IU.userAccountID
    GROUP BY
        to_char(msgtimestamp, 'DY'),IU.usertype
    )
    SELECT
        *
    FROM
        all_messages
    PIVOT (
        sum(msgAvg) FOR usertype IN ('Employer' AS Employer, 'Employee' AS Employee, 'JobSeeker' AS JobSeeker)
    )
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    custom_order = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    df = pd.read_sql_query(sql_query, connection)
    df['DAYS'] = pd.Categorical(df['DAYS'], categories=custom_order, ordered=True)
    df = df.sort_values('DAYS')
    fig = px.bar(df, x='DAYS', y=['EMPLOYER', 'EMPLOYEE', 'JOBSEEKER'],
             labels={'value': 'Average Messages', 'variable': 'User Type'},
             title='Average Messages by User Type and Day',
             color='variable',barmode='group')
    fig.update_xaxes(tickangle=45, tickmode='array')
    graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
    context = {'graph': graph}
    return render(request, 'DashboardTemplates/passingPercentageDashboard.html', context)


def indexView(request):
    return redirect('login')
    return render(request, 'DashboardTemplates/passingPercentageDashboard.html', {})