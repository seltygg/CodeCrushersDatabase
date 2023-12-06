from django.shortcuts import render,redirect
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from django.db import connection
from django.contrib.auth.decorators import login_required
import networkx as nx
import plotly.graph_objects as go
import plotly.subplots as sp
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
    certifications c
    JOIN
    QuizPassingScores qps ON c.certificateid = qps.certificateid
    JOIN
    quizzes q ON qps.quizid = q.quizid
    GROUP BY
    c.certificateid, c.name, c.description, c.duration, c.topic, qps.quizid, q.name, q.passingscore
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
                    ON p.pageid = ac2.pageid
                WHERE postid IN (SELECT postid
                                 FROM posts
                                 WHERE (posttimestamp >= sysdate - 30))
                GROUP BY (ac2.accountid)),
      final_q AS (SELECT f_count.accID "Account No.",follower_counts, T_like_counts ,(follower_counts + T_like_counts) "TOP VOICE METRICS",
                DENSE_RANK() OVER(ORDER BY(follower_counts + T_like_counts)DESC) RANKING
        FROM f_count
        FULL OUTER JOIN l_count 
            ON f_count.accid = l_count.accid
        WHERE (follower_counts + T_like_counts) IS NOT NULL)
        SELECT (ius.fname||' '|| ius.lname) "TOP VOICE OWNER", T_like_counts, follower_counts ,"TOP VOICE METRICS", RANKING
        FROM individual_users ius
        JOIN final_q fq
            ON fq."Account No." = ius.useraccountid
        WHERE fq.ranking <= 5
        ORDER BY ranking
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    df = pd.read_sql_query(sql_query, connection)
    fig = px.scatter(df, x='TOP VOICE OWNER', y='TOP VOICE METRICS',
                 size='TOP VOICE METRICS', color='RANKING',
                 labels={'Top Voice Metrics': 'Metrics'},
                 title='Top Voice Metrics by Owner',
                 size_max=60)
    fig.update_xaxes(tickangle=45, tickmode='array')
    graph = fig.to_html(full_html=False, default_height=600, default_width=800)
    context = {'graph': graph}
    return render(request, 'DashboardTemplates/topVoiceDashboard.html', context)

@login_required
def averageMessagesPerUserType(request):
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
    return render(request, 'DashboardTemplates/averageMessagesPerUserType.html', context)


@login_required
def mostPopularTeachersDashboard(request):
    sql_query = """
    WITH TeacherCourseCounts AS (
    SELECT t.TEACHERID,
            (t.fname ||' '||t.lname) AS TEACHER_NAME,
            ct.CERTIFICATEID
    FROM TEACHERS t
    JOIN TEACH c ON t.TEACHERID = c.TEACHERID
    JOIN CERTIFICATions ct ON ct.CERTIFICATEID = c.CERTIFICATEID),

    PopularCourses AS (SELECT r.CERTIFICATEID,
            COUNT(DISTINCT r.USERACCOUNTID) AS NUM_CERTIFICATES
            FROM RESULTS r
            GROUP BY r.CERTIFICATEID)
    SELECT
    tc.TEACHERID,
    tc.TEACHER_NAME,
    COUNT(tc.CERTIFICATEID) TOTAL_COURSES,
    NVL(SUM(pc.NUM_CERTIFICATES), 0) AS POPULARITY_SCORE
    FROM
    TeacherCourseCounts tc
    LEFT JOIN
    PopularCourses pc ON tc.CERTIFICATEID = pc.CERTIFICATEID
    GROUP BY
    tc.TEACHERID, tc.TEACHER_NAME
    ORDER BY
    POPULARITY_SCORE DESC
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)

    df = pd.read_sql_query(sql_query, connection)

    # Create a bar chart using Plotly Express
    fig = px.bar(df, x='TEACHER_NAME', y='POPULARITY_SCORE', title='Teachers Sorted By Popularity' , labels={'experience': 'Experience'})
    fig.update_layout(xaxis_title='Teacher Name', yaxis_title='Popularity')

    # Convert the Plotly figure to HTML
    chart_html = fig.to_html(full_html=False)

    context = {'graph': chart_html}
    return render(request, 'DashboardTemplates/mostPopularTeachersDashboard.html', context)

@login_required
def connectionsNetworkDashboard(request):
    sql_query = """
    WITH df AS (
    SELECT senderid AS user_id, receiverid AS friend_id
    FROM CONNECTIONS
    UNION
    SELECT receiverid AS user_id, senderid AS friend_id
    FROM CONNECTIONS
    ),
    fl_list AS (
    SELECT ius.useraccountid,
            (ius.fname || ' ' || ius.lname) AS User_Name,
            COALESCE(df.friend_id, 'No friends') AS Friends,
            (ius1.fname || ' ' || ius1.lname) AS Friend_Name
    FROM individual_users ius
    LEFT JOIN df ON ius.useraccountid = df.user_id
    LEFT JOIN individual_users ius1 ON df.friend_id = ius1.useraccountid
    ),
    hey AS (
    SELECT fl_list.useraccountid,
            fl_list.user_name,
            fl_list.Friends,
            fl_list.friend_name,
            COALESCE(df.friend_id, 'N/A') AS mutual_friends,
            (i.fname || ' ' || i.lname) AS mutual_connections
    FROM fl_list
    LEFT JOIN df ON fl_list.Friends = df.user_id
    LEFT JOIN individual_users i ON i.useraccountid = df.friend_id
    WHERE (df.friend_id <> fl_list.useraccountid) OR (df.friend_id IS NULL)
    )

    SELECT user_name,
        CASE
            WHEN MIN(Friends) = 'No friends' THEN 'No Friends YET'
            ELSE friend_name
        END AS "1st Friends",
        CASE
            WHEN MIN(mutual_friends) = 'N/A' THEN 'No Mutual Friends Either'
            ELSE LISTAGG(DISTINCT mutual_connections, ', ') WITHIN GROUP (ORDER BY friend_name)
        END AS "Mutual Friends",
        LISTAGG(DISTINCT mutual_friends, ', ') WITHIN GROUP (ORDER BY friend_name) AS "Mutuals FAccID"
    FROM hey
    GROUP BY user_name, friend_name
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)

    df = pd.read_sql_query(sql_query, connection)

    # Create a directed graph
    G = nx.DiGraph()

    #remove space fromc column names in df
    df.columns = df.columns.str.replace(' ', '')

    # Add nodes and edges based on the provided information
    for index, row in df.iterrows():
        user_name = row['USER_NAME']
        friends_list = row['1stFriends'].split(', ')
        mutual_friends_list = row['MutualFriends'].split(', ')
        mutuals_faccid_list = row['MutualsFAccID'].split(', ')

        G.add_node(user_name)
        G.add_nodes_from(friends_list)
        G.add_nodes_from(mutual_friends_list)
        G.add_nodes_from(mutuals_faccid_list)

        G.add_edges_from([(user_name, friend) for friend in friends_list])
        G.add_edges_from([(user_name, friend) for friend in mutual_friends_list])
        G.add_edges_from([(user_name, friend) for friend in mutuals_faccid_list])

    # Use networkx.layout to compute a layout for the graph
    pos = nx.spring_layout(G)

    # Create a Plotly figure
    fig = go.Figure()

    # Add nodes to the Plotly figure
    for node in G.nodes():
        x, y = pos[node]
        fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers', marker=dict(size=10), text=node, hoverinfo='text'))

    # Add edges to the Plotly figure
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='gray'), hoverinfo='none'))

    # Customize layout
    fig.update_layout(
        title='Connections Network Graph',
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        hovermode='closest'
    )

    # Encode the Plotly figure as HTML
    chart_html = fig.to_html(full_html=False)

    # Close the connection
    connection.close()

    # Pass the HTML and other context variables to the template
    context = {'graph': chart_html, 'df': df}
    return render(request, 'DashboardTemplates/connectionsNetworkDashBoard.html', context)

def numberOfUsersPerCourse(request):
    sql_query = """
    SELECT c.name, COUNT(iu.userAccountID) "No. of User", 
    RANK() OVER (ORDER BY COUNT(iu.userAccountID) DESC) AS rank 
    FROM RESULTS r 
    JOIN INDIVIDUAL_USERS iu ON r.userAccountID = iu.userAccountID 
    JOIN CERTIFICATIONS c ON r.certificateid = c.certificateid 
    JOIN ( 
    SELECT DISTINCT e.employeeID 
    FROM Employees e 
    JOIN INDIVIDUAL_USERS iu ON iu.userAccountID = e.employeeID 
    WHERE REGEXP_LIKE(e.jobTitle, 'IT|engineer|data', 'i'))e 
    ON r.userAccountID = e.employeeID 
    GROUP BY c.name 
    ORDER BY rank 
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)

    df = pd.read_sql_query(sql_query, connection)

    # Create a bar chart using Plotly Express
    fig = px.pie(df, names="NAME", values="No. of User", title="Number of Users per Course")
    fig.update_layout(title_text="Number of Users per Course")

    # Convert the Plotly figure to HTML
    chart_html = fig.to_html(full_html=False)

    context = {'graph': chart_html}
    return render(request, 'DashboardTemplates/numberOfUsersPerCourse.html', context)

@login_required
def averageNumberOfMessagesByUser(request):
    sql_query = """
    SELECT ROUND(AVG(message_count),2) AS average_message_count 
    FROM ( 
        SELECT COUNT(*) AS message_count 
        FROM messages  
        JOIN accounts sender ON (sender.accountID = messages.msenderID) 
        JOIN accounts receiver ON (receiver.accountID = messages.mreceiverID) 
        GROUP BY LEAST (messages.msenderID, messages.mreceiverID), GREATEST (messages.msenderID, messages.mreceiverID) 
    ) subquery
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    df = pd.read_sql_query(sql_query, connection)
    fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", 
    value = df["AVERAGE_MESSAGE_COUNT"][0], 
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {"text": "Average Message Count"},
    delta = {'reference': 1.5},
    gauge = {
        'axis': {'range': [None, 5]},
        'steps' : [
            {'range': [0, 1.5], 'color': "lightgray"},
            {'range': [1.5, 2.5], 'color': "gray"}],
        'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 2}}))

    fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
    chart_html = fig.to_html(full_html=False)
    context = {'graph': chart_html}
    return render(request, 'DashboardTemplates/numberOfUsersPerCourse.html', context)

@login_required
def topicsByPopularityDashboard(request):
    sql_query = """
    WITH t_topic AS ( SELECT t.teacherid, t.certificateid, topic
    FROM teach t
    JOIN certifications c
        ON c.certificateid = t.certificateid),

    users_count AS ( SELECT topic, COUNT(DISTINCT teacherid) Teacher_Count,
    COUNT(DISTINCT useraccountid) User_Count
    FROM t_topic
    JOIN results r
        ON r.certificateid = t_topic.certificateid
    GROUP BY topic)

    SELECT topic, (Teacher_Count + User_Count) "Topic Popularity Score",
    DENSE_RANK() OVER(ORDER BY (Teacher_Count + User_Count) DESC) "RANKING"
    FROM users_count
    ORDER BY  "RANKING" DESC
    FETCH FIRST 10 ROWS ONLY
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    df = pd.read_sql_query(sql_query, connection)
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df['TOPIC'],
        y=df['Topic Popularity Score'],
        marker_color='blue',  # You can change the color as needed
    ))

    # Customize layout
    fig.update_layout(
        title="Least 10 Topics by Popularity",
        xaxis_title="Topics",
        yaxis_title="Popularity Score",
    )
    chart_html = fig.to_html(full_html=False)
    context = {'graph': chart_html}
    return render(request, 'DashboardTemplates/bottomTopicsDashboard.html', context)

@login_required
def minMaxSalaryByDepartmentDashboard(request):
    sql_query = """
    SELECT 
    jobcategory, COUNT(DISTINCT employerid) "No. of EMPLOYERS",  
    TO_CHAR(ROUND(AVG(min_salary)),'$9,999,999') "Avg. Min. Salary", 
    TO_CHAR(ROUND(AVG(max_salary)),'$9,999,999') "Avg. Max. Salary" 
    FROM jobs 
    WHERE employerid IN (SELECT employerid 
                        FROM employers 
                        WHERE sponsorship = 'Y') 
    GROUP BY jobcategory 
    ORDER BY "No. of EMPLOYERS" DESC 
    FETCH FIRST 5 ROWS WITH TIES
    """
    cursor = connection.cursor()
    cursor.execute(sql_query)
    df = pd.read_sql_query(sql_query, connection)
    
    fig = px.bar(df, x='JOBCATEGORY', y=['Avg. Min. Salary', 'Avg. Max. Salary'],
                 title='Average Min. and Max. Salaries by Department',
                 labels={'value': 'Salary'},
                 hover_name='JOBCATEGORY',
                 color_discrete_map={'Avg. Min. Salary': 'blue', 'Avg. Max. Salary': 'orange'})

    # Customize the layout if needed
    fig.update_layout(barmode='group')
    
    chart_html = fig.to_html(full_html=False)
    context = {'graph': chart_html}
    
    return render(request, 'DashboardTemplates/minMaxSalaryByDepartmentDashboard.html', context)

def indexView(request):
    return redirect('login')