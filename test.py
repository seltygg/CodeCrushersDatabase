import plotly.express as px
import pandas as pd

# Create a DataFrame with the given data
data = {
    'CERTIFICATEID': ["CE00000011", "CE00000013", "CE00000014", "CE00000005", "CE00000010", "CE00000007",
                      "CE00000012", "CE00000003", "CE00000009", "CE00000006", "CE00000001", "CE00000008",
                      "CE00000002", "CE00000019", "CE00000018", "CE00000004", "CE00000015", "CE00000016",
                      "CE00000020", "CE00000017"],
    'Certificate Name': ["Python Programming Basics", "Machine Learning Essentials", "Mobile App Development",
                         "Web Development Basics", "Digital Marketing Specialist", "Graphic Design Essentials",
                         "Cloud Computing Fundamentals", "Oracle SQL Developer", "Cybersecurity Fundamentals",
                         "Data Science Foundations", "Microsoft Office Specialist", "Project Management Professional",
                         "SQL Fundamentals", "IoT Essentials", "Business Analytics Foundations", "Java Programmer",
                         "Agile Project Management", "Frontend Web Development", "Digital Photography Basics",
                         "Network Security Specialist"],
    'Quiz ID': ["QZ00000011", "QZ00000013", "QZ00000014", "QZ00000005", "QZ00000010", "QZ00000007", "QZ00000012",
                "QZ00000003", "QZ00000009", "QZ00000006", "QZ00000001", "QZ00000008", "QZ00000002", "QZ00000019",
                "QZ00000018", "QZ00000004", "QZ00000015", "QZ00000016", "QZ00000020", "QZ00000017"],
    'Quiz Name': ["Python Basics", "Machine Learning", "Mobile App Development Basics", "Fundamentals of Web Development",
                  "Digital Marketing", "Graphic Design 101", "Cloud Computing", "Oracle SQL Developer", "Cybersecurity",
                  "Data Science 101", "Microsoft Office Suite Basics", "Project Management Fundamentals", "SQL 101",
                  "IoT Foundations", "Business Analytics Essentials", "Java Programming Basics",
                  "Agile Project Management Basics", "Frontend Web Development 101", "Digital Photography",
                  "Network Security Specialist Basics"],
    'Quiz Passing Score': [20, 28, 30, 25, 48, 20, 38, 50, 15, 40, 45, 55, 30, 18, 22, 35, 50, 32, 40, 52],
    'NUM_ATTEMPTS': [3, 2, 4, 4, 4, 4, 2, 6, 4, 4, 4, 4, 4, 1, 1, 4, 2, 1, 1, 1],
    'NUM_PASSING_SCORES': [2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'PASSING_PERCENTAGE': [66.67, 50, 50, 50, 50, 50, 50, 33.33, 25, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x='Certificate Name', y='PASSING_PERCENTAGE', text='PASSING_PERCENTAGE',
             labels={'PASSING_PERCENTAGE': 'Passing Percentage (%)'},
             title='Passing Percentage for Certificates')

# Rotate x-axis labels for better readability
fig.update_xaxes(tickangle=45, tickmode='array')

# Show the figure
fig.show()
