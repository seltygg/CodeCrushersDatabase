import plotly.graph_objects as go

# Data
categories = ['Analytics', 'Engineering', 'Project Management', 'IT', 'Logistics', 'Product Management']
avg_min_salary = [73333, 68571, 90000, 80000, 60000, 88333]
avg_max_salary = [94667, 90286, 120000, 105000, 78000, 113333]

# Create a grouped bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=categories,
    y=avg_min_salary,
    name='Avg. Min. Salary',
    marker_color='rgb(55, 83, 109)'
))

fig.add_trace(go.Bar(
    x=categories,
    y=avg_max_salary,
    name='Avg. Max. Salary',
    marker_color='rgb(26, 118, 255)'
))

# Update layout
fig.update_layout(barmode='group',
                  title='Average Minimum and Maximum Salary by Job Category',
                  xaxis=dict(title='Job Category'),
                  yaxis=dict(title='Salary'))

# Show the graph
fig.show()
