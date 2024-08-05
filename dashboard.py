# %%
#####CHILDBIRTH GRAPH

import plotly.graph_objects as go

# Data
indicators = ['Childbirth by<br>skilled attendant', 'Childbirth by<br>unskilled attendant']
percentages = [98.2, 1.8]
colors = ['#3498db', '#e74c3c']  # Blue for skilled, Red for unskilled

# Create hover text
hover_text = [
    "98.2% of childbirths are attended by skilled professionals, ensuring safer deliveries.",
    "1.8% of childbirths are attended by unskilled individuals, which may pose higher risks."
]

# Create the figure
fig = go.Figure()

# Add bars with custom hover text
fig.add_trace(
    go.Bar(
        x=[0, 0.5],
        y=percentages,
        marker_color=colors,
        width=0.4,
        hoverinfo='text',
        hovertext=hover_text,
        hoverlabel=dict(bgcolor=colors)
    )
)

# Update layout
fig.update_layout(
    title={
        'text': 'Childbirth Attendance',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, color='#333', family='Arial Black')
    },
    showlegend=False,
    plot_bgcolor='white',
    height=600,
    margin=dict(t=100, l=50, r=50, b=100),
    xaxis=dict(
        showticklabels=False,
        range=[-0.2, 0.7]
    ),
    yaxis=dict(visible=False),
    bargap=0,
)

# Add percentage labels above bars
for i, (percentage, color) in enumerate(zip(percentages, colors)):
    fig.add_annotation(
        x=i*0.5,
        y=percentage,
        text=f"<b>{percentage}%</b>",
        showarrow=False,
        font=dict(size=20, color=color, family='Arial Black'),
        xanchor='center',
        yanchor='bottom',
        yshift=10
    )

# Add bar labels below
for i, (indicator, color) in enumerate(zip(indicators, colors)):
    fig.add_annotation(
        x=i*0.5,
        y=-0.05,
        text=f"<b>{indicator}</b>",
        showarrow=False,
        font=dict(size=16, color=color, family='Arial Black'),
        xanchor='center',
        yanchor='top',
        yref='paper'
    )

# Show the plot
fig.show()


#####PLACE OF BIRTH GRAPH

# Data
places = ['Private hospital or clinic', 'Public hospital', 'Private doctor', 'Home', 
          'Non-governmental health centre', 'General health centre']
percentages = [80.1, 11.9, 2.8, 2.4, 1.2, 0.7]
colors = ['#3498db', '#2ecc71', '#9b59b6', '#e74c3c', '#f39c12', '#1abc9c']

# Sort data in descending order
sorted_data = sorted(zip(places, percentages, colors), key=lambda x: x[1], reverse=True)
places, percentages, colors = zip(*sorted_data)

# Create hover text
hover_text = [
    f"{place}: {percentage}% of childbirths"
    for place, percentage in zip(places, percentages)
]

# Create the figure
fig = go.Figure()

# Add bars with custom hover text
fig.add_trace(
    go.Bar(
        y=places,
        x=percentages,
        orientation='h',
        marker_color=colors,
        hoverinfo='text',
        hovertext=hover_text,
        hoverlabel=dict(bgcolor=colors)
    )
)

# Update layout
fig.update_layout(
    title={
        'text': 'Place of Childbirth',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, color='#333', family='Arial Black')
    },
    showlegend=False,
    plot_bgcolor='white',
    height=600,
    margin=dict(t=100, l=250, r=100, b=50),
    xaxis=dict(
        visible=False,
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    yaxis=dict(
        tickfont=dict(size=14, color='#333', family='Arial'),
        showgrid=False,
        autorange="reversed"  # This ensures the y-axis is in descending order
    ),
    bargap=0.2,
)

# Add percentage labels at the end of bars
for i, (percentage, color) in enumerate(zip(percentages, colors)):
    fig.add_annotation(
        x=percentage,
        y=i,
        text=f"<b>{percentage}%</b>",
        showarrow=False,
        font=dict(size=14, color=color, family='Arial Black'),
        xanchor='left',
        yanchor='middle',
        xshift=5,
    )

# Show the plot
fig.show()

######## PRIVATE HOSPITAL DLIVERIES 

hospital_types = ['Private', 'Public']
percentages = [77.8, 22.2]
colors = ['#3498db', '#e74c3c']  # Blue for Private, Red for Public

# Create the pie chart
fig = go.Figure(data=[go.Pie(
    labels=hospital_types,
    values=percentages,
    hole=.4,
    marker_colors=colors,
    textinfo='label+percent',
    textposition='outside',
    textfont_size=14,
    textfont_color=colors,  # Match text color to slice color
    pull=[0.05, 0],  # Slightly pull out the Private slice
    hoverinfo='label+value+percent',
    hovertemplate='%{label}<br>%{value}% of deliveries<br>(%{percent})<extra></extra>'
)])

# Update layout
fig.update_layout(
    title={
        'text': 'Percentage of Deliveries by Type of Hospital',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=20, color='#333', family='Arial Black')
    },
    showlegend=False,  # Remove the legend
    annotations=[
        dict(
            text='Total Deliveries<br>35,883',
            x=0.5,
            y=0.5,
            font=dict(size=14, color='#333', family='Arial'),  # Increased from 12 to 14
            showarrow=False,
            align='center'
        )
    ]
)

# Show the plot
fig.show()


##### CESARIAN BIRTH GRAPH

import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    'Year': list(range(2011, 2023)),
    'Cesarean Delivery Rate (%)': [46.1, 47.6, 46.5, 45.6, 46.7, 47.0, 47.0, 47.5, 49.5, 48.3, 50.2, 49.0],
    'World Average (%)': [19.3, 19.7, 20.1, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5]
}

df = pd.DataFrame(data)

# Create the line chart
fig = go.Figure()

# Add Cesarean Delivery Rate line
fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['Cesarean Delivery Rate (%)'],
    mode='lines+markers',
    name='Cesarean Delivery Rate',
    line=dict(width=3, color='blue'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Cesarean Delivery Rate in Lebanon was %{y:.1f}%.<extra></extra>'
))

# Add World Average line
fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['World Average (%)'],
    mode='lines+markers',
    name='World Average',
    line=dict(width=3, color='red'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, World Average Cesarean Delivery Rate was %{y:.1f}%.<extra></extra>'
))

# Add text annotations under each line
fig.add_annotation(
    x=df['Year'].iloc[-1] - 0.5,
    y=df['Cesarean Delivery Rate (%)'].iloc[-1] - 5,
    text='In Lebanon',
    showarrow=False,
    font=dict(color='blue', size=12),
    align='left',
    xanchor='left'
)

fig.add_annotation(
    x=df['Year'].iloc[-1] - 0.5,
    y=df['World Average (%)'].iloc[-1] - 2,
    text='World Average',
    showarrow=False,
    font=dict(color='red', size=12),
    align='left',
    xanchor='left'
)

# Update layout
fig.update_layout(
    title={
        'text': 'Cesarean Delivery Rate (in %)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, family='Arial Black')
    },
    hovermode="closest",
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        range=[0, 55],
        tickfont=dict(size=12),
        title=None
    ),
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        tickangle=45,
        tickfont=dict(size=12),
        showgrid=False,
        range=[2010.5, 2022.5]  # Adjust range to add space between 2011 and 2022
    ),
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=False,
    height=600,
    width=1000
)

# Show the plot
fig.show()



##GRAPH FOR BIRTH AND DEATH 

import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    'Year': list(range(2010, 2023)),
    'Number of Registered Lebanese Births (\'000)': [91.795, 97.887, 90.167, 86.950, 88.704, 85.453, 88.996, 90.647, 89.772, 86.179, 74.049, 68.130, 62.868],
    'Number of Registered Lebanese Deaths (\'000)': [21.441, 23.257, 22.792, 23.414, 25.117, 25.275, 24.617, 25.847, 25.096, 24.950, 28.637, 34.725, 29.455]
}

df = pd.DataFrame(data)

# Create the line chart
fig = go.Figure()

# Add Number of Registered Lebanese Births line
fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['Number of Registered Lebanese Births (\'000)'],
    mode='lines+markers',
    name='Registered Births',
    line=dict(width=3, color='green'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Number of Registered Births was %{y:.1f}k.<extra></extra>'
))

# Add Number of Registered Lebanese Deaths line
fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['Number of Registered Lebanese Deaths (\'000)'],
    mode='lines+markers',
    name='Registered Deaths',
    line=dict(width=3, color='red'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Number of Registered Deaths was %{y:.1f}k.<extra></extra>'
))

# Add text annotations under each line
fig.add_annotation(
    x=df['Year'].iloc[-1] - 0.5,
    y=df['Number of Registered Lebanese Births (\'000)'].iloc[-1] - 2,
    text='Registered Births',
    showarrow=False,
    font=dict(color='green', size=12),
    align='left',
    xanchor='left'
)

fig.add_annotation(
    x=df['Year'].iloc[-1] - 0.5,
    y=df['Number of Registered Lebanese Deaths (\'000)'].iloc[-1] - 2,
    text='Registered Deaths',
    showarrow=False,
    font=dict(color='red', size=12),
    align='left',
    xanchor='left'
)

# Update layout
fig.update_layout(
    title={
        'text': 'Lebanese Births and Deaths Data (\'000) (2010-2022)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, family='Arial Black')
    },
    hovermode="closest",
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=12),
        title=None
    ),
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        tickangle=0,  # Set tick angle to 0 for horizontal labels
        tickfont=dict(size=12),
        showgrid=False,
        range=[2009.5, 2022.5]
    ),
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=False,
    height=600,
    width=1000
)

# Show the plot
fig.show()


###GRAPH FOR LEBANESE NON LEBANSE BIRTH

import plotly.graph_objects as go
import pandas as pd

# Combined data for 2017-2022
data_combined = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'Proportion of Lebanese Live Birth (%)': [55.6, 54.2, 56.5, 55.74, 55.42, 52.20],
    'Proportion of Non-Lebanese Live Birth (%)': [44.4, 45.8, 43.5, 44.26, 44.57, 47.80],
    'Neonatal MR per 1,000 Live Birth - Lebanese': [4.3, 4.5, 4.4, 4.61, 5.65, 4.37],
    'Neonatal MR per 1,000 Live Birth - Non-Lebanese': [6.7, 6.4, 6.3, 7.08, 7.89, 8.11],
    'Maternal MR per 100,000 Live Birth - Lebanese': [8.7, 10.2, 6.1, 15.66, 15.76, 43.15],
    'Maternal MR per 100,000 Live Birth - Non-Lebanese': [27.1, 17.2, 23.7, 19.73, 51.83, 21.99]
}

df_combined = pd.DataFrame(data_combined)

# Extract data for the first graph: Proportion of Lebanese and Non-Lebanese Live Births
df_births = df_combined[['Year', 'Proportion of Lebanese Live Birth (%)', 'Proportion of Non-Lebanese Live Birth (%)']]

# Create the line chart for live births
fig_births = go.Figure()

# Add Proportion of Lebanese Live Birth line
fig_births.add_trace(go.Scatter(
    x=df_births['Year'],
    y=df_births['Proportion of Lebanese Live Birth (%)'],
    mode='lines+markers',
    name='Lebanese Live Birth',
    line=dict(width=3, color='blue'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Proportion of Lebanese Live Birth was %{y:.1f}%.<extra></extra>'
))

# Add Proportion of Non-Lebanese Live Birth line
fig_births.add_trace(go.Scatter(
    x=df_births['Year'],
    y=df_births['Proportion of Non-Lebanese Live Birth (%)'],
    mode='lines+markers',
    name='Non-Lebanese Live Birth',
    line=dict(width=3, color='red'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Proportion of Non-Lebanese Live Birth was %{y:.1f}%.<extra></extra>'
))

# Add text annotations under each line
fig_births.add_annotation(
    x=df_births['Year'].iloc[-1] - 0.5,
    y=df_births['Proportion of Lebanese Live Birth (%)'].iloc[-1] - 2,
    text='Lebanese Live Birth',
    showarrow=False,
    font=dict(color='blue', size=12),
    align='left',
    xanchor='left'
)

fig_births.add_annotation(
    x=df_births['Year'].iloc[-1] - 0.5,
    y=df_births['Proportion of Non-Lebanese Live Birth (%)'].iloc[-1] - 2,
    text='Non-Lebanese Live Birth',
    showarrow=False,
    font=dict(color='red', size=12),
    align='left',
    xanchor='left'
)

# Update layout
fig_births.update_layout(
    title={
        'text': 'Proportion of Lebanese and Non-Lebanese Live Births (2017-2022)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, family='Arial Black')
    },
    hovermode="closest",
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=12),
        title=None
    ),
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        tickangle=0,  # Set tick angle to 0 for horizontal labels
        tickfont=dict(size=12),
        showgrid=False,
        range=[2016.5, 2022.5]
    ),
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=False,
    height=600,
    width=1000
)

# Show the plot
fig_births.show()


##### MR FOR LEBANESE NON LEBANESE

# Extract data for the second graph: Neonatal Mortality Rate for Lebanese and Non-Lebanese
df_neonatal_mr = df_combined[['Year', 'Neonatal MR per 1,000 Live Birth - Lebanese', 'Neonatal MR per 1,000 Live Birth - Non-Lebanese']]

# Create the line chart for neonatal mortality rate
fig_neonatal_mr = go.Figure()

# Add Neonatal MR for Lebanese line
fig_neonatal_mr.add_trace(go.Scatter(
    x=df_neonatal_mr['Year'],
    y=df_neonatal_mr['Neonatal MR per 1,000 Live Birth - Lebanese'],
    mode='lines+markers',
    name='Lebanese Neonatal MR',
    line=dict(width=3, color='blue'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Lebanese Neonatal MR was %{y:.2f} per 1,000 live births.<extra></extra>'
))

# Add Neonatal MR for Non-Lebanese line
fig_neonatal_mr.add_trace(go.Scatter(
    x=df_neonatal_mr['Year'],
    y=df_neonatal_mr['Neonatal MR per 1,000 Live Birth - Non-Lebanese'],
    mode='lines+markers',
    name='Non-Lebanese Neonatal MR',
    line=dict(width=3, color='red'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Non-Lebanese Neonatal MR was %{y:.2f} per 1,000 live births.<extra></extra>'
))

# Add text annotations under each line
fig_neonatal_mr.add_annotation(
    x=df_neonatal_mr['Year'].iloc[-1] - 0.5,
    y=df_neonatal_mr['Neonatal MR per 1,000 Live Birth - Lebanese'].iloc[-1] - 0.5,
    text='Lebanese Neonatal MR',
    showarrow=False,
    font=dict(color='blue', size=12),
    align='left',
    xanchor='left'
)

fig_neonatal_mr.add_annotation(
    x=df_neonatal_mr['Year'].iloc[-1] - 0.5,
    y=df_neonatal_mr['Neonatal MR per 1,000 Live Birth - Non-Lebanese'].iloc[-1] - 0.5,
    text='Non-Lebanese Neonatal MR',
    showarrow=False,
    font=dict(color='red', size=12),
    align='left',
    xanchor='left'
)

# Update layout
fig_neonatal_mr.update_layout(
    title={
        'text': 'Neonatal MR per 1,000 Live Birth - Lebanese/Non Lebanese',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, family='Arial Black')
    },
    hovermode="closest",
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=12),
        title=None
    ),
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        tickangle=0,  # Set tick angle to 0 for horizontal labels
        tickfont=dict(size=12),
        showgrid=False,
        range=[2016.5, 2022.5]
    ),
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=False,
    height=600,
    width=1000
)

# Show the plot
fig_neonatal_mr.show()


############ maternal MR FOR WOMEN

# Extract data for the Maternal Mortality Rate graph
df_maternal_mr = df_combined[['Year', 'Maternal MR per 100,000 Live Birth - Lebanese', 'Maternal MR per 100,000 Live Birth - Non-Lebanese']]

# Create the line chart for maternal mortality rate
fig_maternal_mr = go.Figure()

# Add Maternal MR for Lebanese line
fig_maternal_mr.add_trace(go.Scatter(
    x=df_maternal_mr['Year'],
    y=df_maternal_mr['Maternal MR per 100,000 Live Birth - Lebanese'],
    mode='lines+markers',
    name='Lebanese Maternal MR',
    line=dict(width=3, color='blue'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Lebanese Maternal MR was %{y:.2f} per 100,000 live births.<extra></extra>'
))

# Add Maternal MR for Non-Lebanese line
fig_maternal_mr.add_trace(go.Scatter(
    x=df_maternal_mr['Year'],
    y=df_maternal_mr['Maternal MR per 100,000 Live Birth - Non-Lebanese'],
    mode='lines+markers',
    name='Non-Lebanese Maternal MR',
    line=dict(width=3, color='red'),
    marker=dict(size=6, symbol='circle'),
    hovertemplate='In %{x}, Non-Lebanese Maternal MR was %{y:.2f} per 100,000 live births.<extra></extra>'
))

# Add text annotations under each line
fig_maternal_mr.add_annotation(
    x=df_maternal_mr['Year'].iloc[-1] - 0.5,
    y=df_maternal_mr['Maternal MR per 100,000 Live Birth - Lebanese'].iloc[-1] + 5,
    text='Lebanese Maternal MR',
    showarrow=False,
    font=dict(color='blue', size=12),
    align='left',
    xanchor='left'
)

fig_maternal_mr.add_annotation(
    x=df_maternal_mr['Year'].iloc[-1] - 0.5,
    y=df_maternal_mr['Maternal MR per 100,000 Live Birth - Non-Lebanese'].iloc[-1] - 5,
    text='Non-Lebanese Maternal MR',
    showarrow=False,
    font=dict(color='red', size=12),
    align='left',
    xanchor='left'
)

# Update layout
fig_maternal_mr.update_layout(
    title={
        'text': 'Maternal Mortality Rate (per 100,000 Live Births) for Lebanese and Non-Lebanese (2017-2022)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, family='Arial Black')
    },
    hovermode="closest",
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=12),
        title=None
    ),
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        tickangle=0,  # Set tick angle to 0 for horizontal labels
        tickfont=dict(size=12),
        showgrid=False,
        range=[2016.5, 2022.5]
    ),
    margin=dict(l=50, r=50, t=80, b=50),
    showlegend=False,
    height=600,
    width=1000
)

# Show the plot
fig_maternal_mr.show()

 

# %%
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# %% [markdown]
# ### Childbirth attendance

# %%
def childbirth_attendance_graph():
    indicators = ['Childbirth by<br>skilled attendant', 'Childbirth by<br>unskilled attendant']
    percentages = [98.2, 1.8]
    colors = ['#3498db', '#e74c3c']
    hover_text = [
        "98.2% of childbirths are attended by skilled professionals, ensuring safer deliveries.",
        "1.8% of childbirths are attended by unskilled individuals, which may pose higher risks."
    ]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=[0, 0.5],
            y=percentages,
            marker_color=colors,
            width=0.4,
            hoverinfo='text',
            hovertext=hover_text,
            hoverlabel=dict(bgcolor=colors)
        )
    )

    fig.update_layout(
        title={
            'text': 'Childbirth Attendance',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='white', family='Arial Black')
        },
        showlegend=False,
        plot_bgcolor='black',
        paper_bgcolor='black',
        height=600,
        margin=dict(t=100, l=50, r=50, b=100),
        xaxis=dict(
            showticklabels=False,
            range=[-0.2, 0.7],
            color='white'
        ),
        yaxis=dict(visible=False),
        bargap=0,
    )

    for i, (percentage, color) in enumerate(zip(percentages, colors)):
        fig.add_annotation(
            x=i*0.5,
            y=percentage,
            text=f"<b>{percentage}%</b>",
            showarrow=False,
            font=dict(size=20, color=color, family='Arial Black'),
            xanchor='center',
            yanchor='bottom',
            yshift=10
        )

    for i, (indicator, color) in enumerate(zip(indicators, colors)):
        fig.add_annotation(
            x=i*0.5,
            y=-0.05,
            text=f"<b>{indicator}</b>",
            showarrow=False,
            font=dict(size=16, color=color, family='Arial Black'),
            xanchor='center',
            yanchor='top',
            yref='paper'
        )

    return fig

# %% [markdown]
# PoB Graph

# %%
def place_of_birth_graph():
    places = ['Private hospital or clinic', 'Public hospital', 'Private doctor', 'Home', 
              'Non-governmental health centre', 'General health centre']
    percentages = [80.1, 11.9, 2.8, 2.4, 1.2, 0.7]
    colors = ['#3498db', '#2ecc71', '#9b59b6', '#e74c3c', '#f39c12', '#1abc9c']
    sorted_data = sorted(zip(places, percentages, colors), key=lambda x: x[1], reverse=True)
    places, percentages, colors = zip(*sorted_data)
    hover_text = [f"{place}: {percentage}% of childbirths" for place, percentage in zip(places, percentages)]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=places,
            x=percentages,
            orientation='h',
            marker_color=colors,
            hoverinfo='text',
            hovertext=hover_text,
            hoverlabel=dict(bgcolor=colors)
        )
    )

    fig.update_layout(
        title={
            'text': 'Place of Childbirth',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='white', family='Arial Black')
        },
        showlegend=False,
        plot_bgcolor='black',
        paper_bgcolor='black',
        height=600,
        margin=dict(t=100, l=250, r=100, b=50),
        xaxis=dict(
            visible=False,
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            color='white'
        ),
        yaxis=dict(
            tickfont=dict(size=14, color='white', family='Arial'),
            showgrid=False,
            autorange="reversed"
        ),
        bargap=0.2,
    )

    for i, (percentage, color) in enumerate(zip(percentages, colors)):
        fig.add_annotation(
            x=percentage,
            y=i,
            text=f"<b>{percentage}%</b>",
            showarrow=False,
            font=dict(size=14, color=color, family='Arial Black'),
            xanchor='left',
            yanchor='middle',
            xshift=5,
        )

    return fig


# %% [markdown]
# Private Hospital

# %%
def private_hospital_deliveries_graph():
    hospital_types = ['Private', 'Public']
    percentages = [77.8, 22.2]
    colors = ['#3498db', '#e74c3c']

    fig = go.Figure(data=[go.Pie(
        labels=hospital_types,
        values=percentages,
        hole=.4,
        marker_colors=colors,
        textinfo='label+percent',
        textposition='outside',
        textfont_size=14,
        textfont_color=colors,
        pull=[0.05, 0],
        hoverinfo='label+value+percent',
        hovertemplate='%{label}<br>%{value}% of deliveries<br>(%{percent})<extra></extra>'
    )])

    fig.update_layout(
        title={
            'text': 'Percentage of Deliveries by Type of Hospital',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, color='white', family='Arial Black')
        },
        showlegend=False,
        annotations=[
            dict(
                text='Total Deliveries<br>35,883',
                x=0.5,
                y=0.5,
                font=dict(size=14, color='white', family='Arial'),
                showarrow=False,
                align='center'
            )
        ],
        plot_bgcolor='black',
        paper_bgcolor='black',
    )

    return fig


# %% [markdown]
# C-section delivery rate

# %%
def cesarean_delivery_rate_graph(start_year, end_year):
    data = {
        'Year': list(range(2011, 2023)),
        'Cesarean Delivery Rate (%)': [46.1, 47.6, 46.5, 45.6, 46.7, 47.0, 47.0, 47.5, 49.5, 48.3, 50.2, 49.0],
        'World Average (%)': [19.3, 19.7, 20.1, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5]
    }
    df = pd.DataFrame(data)
    df_filtered = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Cesarean Delivery Rate (%)'],
        mode='lines+markers',
        name='Cesarean Delivery Rate',
        line=dict(width=3, color='blue'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Cesarean Delivery Rate in Lebanon was %{y:.1f}%.<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['World Average (%)'],
        mode='lines+markers',
        name='World Average',
        line=dict(width=3, color='red'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, World Average Cesarean Delivery Rate was %{y:.1f}%.<extra></extra>'
    ))

    fig.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Cesarean Delivery Rate (%)'].iloc[-1] - 5,
        text='In Lebanon',
        showarrow=False,
        font=dict(color='blue', size=12),
        align='left',
        xanchor='left'
    )

    fig.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['World Average (%)'].iloc[-1] - 2,
        text='World Average',
        showarrow=False,
        font=dict(color='red', size=12),
        align='left',
        xanchor='left'
    )

    fig.update_layout(
        title={
            'text': 'Cesarean Delivery Rate (in %)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black', color='white')
        },
        hovermode="closest",
        plot_bgcolor='black',
        paper_bgcolor='black',
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            range=[0, 55],
            tickfont=dict(size=12, color='white'),
            title=None
        ),
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            tickangle=45,
            tickfont=dict(size=12, color='white'),
            showgrid=False,
            range=[start_year - 0.5, end_year + 0.5]
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=False,
        height=600,
        width=1000
    )

    return fig

# %% [markdown]
# B & D Graph

# %%
def births_and_deaths_graph(start_year, end_year):
    data = {
        'Year': list(range(2010, 2023)),
        'Number of Registered Lebanese Births (\'000)': [91.795, 97.887, 90.167, 86.950, 88.704, 85.453, 88.996, 90.647, 89.772, 86.179, 74.049, 68.130, 62.868],
        'Number of Registered Lebanese Deaths (\'000)': [21.441, 23.257, 22.792, 23.414, 25.117, 25.275, 24.617, 25.847, 25.096, 24.950, 28.637, 34.725, 29.455]
    }
    df = pd.DataFrame(data)
    df_filtered = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Number of Registered Lebanese Births (\'000)'],
        mode='lines+markers',
        name='Registered Births',
        line=dict(width=3, color='green'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Number of Registered Births was %{y:.1f}k.<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Number of Registered Lebanese Deaths (\'000)'],
        mode='lines+markers',
        name='Registered Deaths',
        line=dict(width=3, color='red'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Number of Registered Deaths was %{y:.1f}k.<extra></extra>'
    ))

    fig.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Number of Registered Lebanese Births (\'000)'].iloc[-1] - 2,
        text='Registered Births',
        showarrow=False,
        font=dict(color='green', size=12),
        align='left',
        xanchor='left'
    )

    fig.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Number of Registered Lebanese Deaths (\'000)'].iloc[-1] - 2,
        text='Registered Deaths',
        showarrow=False,
        font=dict(color='red', size=12),
        align='left',
        xanchor='left'
    )

    fig.update_layout(
        title={
            'text': 'Lebanese Births and Deaths Data (\'000) (2010-2022)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black', color='white')
        },
        hovermode="closest",
        plot_bgcolor='black',
        paper_bgcolor='black',
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color='white'),
            title=None
        ),
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            tickangle=0,
            tickfont=dict(size=12, color='white'),
            showgrid=False,
            range=[start_year - 0.5, end_year + 0.5]
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=False,
        height=600,
        width=1000
    )

    return fig

# %% [markdown]
# Leb vs Non-Leb

# %%
def lebanese_non_lebanese_birth_graph(start_year, end_year):
    data_combined = {
        'Year': [2017, 2018, 2019, 2020, 2021, 2022],
        'Proportion of Lebanese Live Birth (%)': [55.6, 54.2, 56.5, 55.74, 55.42, 52.20],
        'Proportion of Non-Lebanese Live Birth (%)': [44.4, 45.8, 43.5, 44.26, 44.57, 47.80],
        'Neonatal MR per 1,000 Live Birth - Lebanese': [4.3, 4.5, 4.4, 4.61, 5.65, 4.37],
        'Neonatal MR per 1,000 Live Birth - Non-Lebanese': [6.7, 6.4, 6.3, 7.08, 7.89, 8.11],
        'Maternal MR per 100,000 Live Birth - Lebanese': [8.7, 10.2, 6.1, 15.66, 15.76, 43.15],
        'Maternal MR per 100,000 Live Birth - Non-Lebanese': [27.1, 17.2, 23.7, 19.73, 51.83, 21.99]
    }
    df_combined = pd.DataFrame(data_combined)
    df_births = df_combined[['Year', 'Proportion of Lebanese Live Birth (%)', 'Proportion of Non-Lebanese Live Birth (%)']]
    df_filtered = df_births[(df_births['Year'] >= start_year) & (df_births['Year'] <= end_year)]

    fig_births = go.Figure()
    fig_births.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Proportion of Lebanese Live Birth (%)'],
        mode='lines+markers',
        name='Lebanese Live Birth',
        line=dict(width=3, color='blue'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Proportion of Lebanese Live Birth was %{y:.1f}%.<extra></extra>'
    ))

    fig_births.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Proportion of Non-Lebanese Live Birth (%)'],
        mode='lines+markers',
        name='Non-Lebanese Live Birth',
        line=dict(width=3, color='red'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Proportion of Non-Lebanese Live Birth was %{y:.1f}%.<extra></extra>'
    ))

    fig_births.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Proportion of Lebanese Live Birth (%)'].iloc[-1] - 2,
        text='Lebanese Live Birth',
        showarrow=False,
        font=dict(color='blue', size=12),
        align='left',
        xanchor='left'
    )

    fig_births.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Proportion of Non-Lebanese Live Birth (%)'].iloc[-1] - 2,
        text='Non-Lebanese Live Birth',
        showarrow=False,
        font=dict(color='red', size=12),
        align='left',
        xanchor='left'
    )

    fig_births.update_layout(
        title={
            'text': 'Proportion of Lebanese and Non-Lebanese Live Births (2017-2022)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black', color='white')
        },
        hovermode="closest",
        plot_bgcolor='black',
        paper_bgcolor='black',
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color='white'),
            title=None
        ),
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            tickangle=0,
            tickfont=dict(size=12, color='white'),
            showgrid=False,
            range=[start_year - 0.5, end_year + 0.5]
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=False,
        height=600,
        width=1000
    )

    return fig_births

# %% [markdown]
# Neonatal

# %%
def neonatal_mr_graph(start_year, end_year):
    data_combined = {
        'Year': [2017, 2018, 2019, 2020, 2021, 2022],
        'Proportion of Lebanese Live Birth (%)': [55.6, 54.2, 56.5, 55.74, 55.42, 52.20],
        'Proportion of Non-Lebanese Live Birth (%)': [44.4, 45.8, 43.5, 44.26, 44.57, 47.80],
        'Neonatal MR per 1,000 Live Birth - Lebanese': [4.3, 4.5, 4.4, 4.61, 5.65, 4.37],
        'Neonatal MR per 1,000 Live Birth - Non-Lebanese': [6.7, 6.4, 6.3, 7.08, 7.89, 8.11],
        'Maternal MR per 100,000 Live Birth - Lebanese': [8.7, 10.2, 6.1, 15.66, 15.76, 43.15],
        'Maternal MR per 100,000 Live Birth - Non-Lebanese': [27.1, 17.2, 23.7, 19.73, 51.83, 21.99]
    }
    df_combined = pd.DataFrame(data_combined)
    df_neonatal_mr = df_combined[['Year', 'Neonatal MR per 1,000 Live Birth - Lebanese', 'Neonatal MR per 1,000 Live Birth - Non-Lebanese']]
    df_filtered = df_neonatal_mr[(df_neonatal_mr['Year'] >= start_year) & (df_neonatal_mr['Year'] <= end_year)]

    fig_neonatal_mr = go.Figure()
    fig_neonatal_mr.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Neonatal MR per 1,000 Live Birth - Lebanese'],
        mode='lines+markers',
        name='Lebanese Neonatal MR',
        line=dict(width=3, color='blue'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Lebanese Neonatal MR was %{y:.2f} per 1,000 live births.<extra></extra>'
    ))

    fig_neonatal_mr.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Neonatal MR per 1,000 Live Birth - Non-Lebanese'],
        mode='lines+markers',
        name='Non-Lebanese Neonatal MR',
        line=dict(width=3, color='red'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Non-Lebanese Neonatal MR was %{y:.2f} per 1,000 live births.<extra></extra>'
    ))

    fig_neonatal_mr.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Neonatal MR per 1,000 Live Birth - Lebanese'].iloc[-1] - 0.5,
        text='Lebanese Neonatal MR',
        showarrow=False,
        font=dict(color='blue', size=12),
        align='left',
        xanchor='left'
    )

    fig_neonatal_mr.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Neonatal MR per 1,000 Live Birth - Non-Lebanese'].iloc[-1] - 0.5,
        text='Non-Lebanese Neonatal MR',
        showarrow=False,
        font=dict(color='red', size=12),
        align='left',
        xanchor='left'
    )

    fig_neonatal_mr.update_layout(
        title={
            'text': 'Neonatal MR per 1,000 Live Birth - Lebanese/Non Lebanese',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black', color='white')
        },
        hovermode="closest",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color='white'),
            title=None
        ),
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            tickangle=0,
            tickfont=dict(size=12, color='white'),
            showgrid=False,
            range=[start_year - 0.5, end_year + 0.5]
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=False,
        height=600,
        width=1000
    )

    return fig_neonatal_mr

# %% [markdown]
# Maternal

# %%
def maternal_mr_graph(start_year, end_year):
    data_combined = {
        'Year': [2017, 2018, 2019, 2020, 2021, 2022],
        'Proportion of Lebanese Live Birth (%)': [55.6, 54.2, 56.5, 55.74, 55.42, 52.20],
        'Proportion of Non-Lebanese Live Birth (%)': [44.4, 45.8, 43.5, 44.26, 44.57, 47.80],
        'Neonatal MR per 1,000 Live Birth - Lebanese': [4.3, 4.5, 4.4, 4.61, 5.65, 4.37],
        'Neonatal MR per 1,000 Live Birth - Non-Lebanese': [6.7, 6.4, 6.3, 7.08, 7.89, 8.11],
        'Maternal MR per 100,000 Live Birth - Lebanese': [8.7, 10.2, 6.1, 15.66, 15.76, 43.15],
        'Maternal MR per 100,000 Live Birth - Non-Lebanese': [27.1, 17.2, 23.7, 19.73, 51.83, 21.99]
    }
    df_combined = pd.DataFrame(data_combined)
    df_maternal_mr = df_combined[['Year', 'Maternal MR per 100,000 Live Birth - Lebanese', 'Maternal MR per 100,000 Live Birth - Non-Lebanese']]
    df_filtered = df_maternal_mr[(df_maternal_mr['Year'] >= start_year) & (df_maternal_mr['Year'] <= end_year)]

    fig_maternal_mr = go.Figure()
    fig_maternal_mr.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Maternal MR per 100,000 Live Birth - Lebanese'],
        mode='lines+markers',
        name='Lebanese Maternal MR',
        line=dict(width=3, color='blue'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Lebanese Maternal MR was %{y:.2f} per 100,000 live births.<extra></extra>'
    ))

    fig_maternal_mr.add_trace(go.Scatter(
        x=df_filtered['Year'],
        y=df_filtered['Maternal MR per 100,000 Live Birth - Non-Lebanese'],
        mode='lines+markers',
        name='Non-Lebanese Maternal MR',
        line=dict(width=3, color='red'),
        marker=dict(size=6, symbol='circle'),
        hovertemplate='In %{x}, Non-Lebanese Maternal MR was %{y:.2f} per 100,000 live births.<extra></extra>'
    ))

    fig_maternal_mr.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Maternal MR per 100,000 Live Birth - Lebanese'].iloc[-1] + 5,
        text='Lebanese Maternal MR',
        showarrow=False,
        font=dict(color='blue', size=12),
        align='left',
        xanchor='left'
    )

    fig_maternal_mr.add_annotation(
        x=df_filtered['Year'].iloc[-1] - 0.5,
        y=df_filtered['Maternal MR per 100,000 Live Birth - Non-Lebanese'].iloc[-1] - 5,
        text='Non-Lebanese Maternal MR',
        showarrow=False,
        font=dict(color='red', size=12),
        align='left',
        xanchor='left'
    )

    fig_maternal_mr.update_layout(
        title={
            'text': 'Maternal Mortality Rate (per 100,000 Live Births) for Lebanese and Non-Lebanese (2017-2022)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black', color='white')
        },
        hovermode="closest",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color='white'),
            title=None
        ),
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            tickangle=0,
            tickfont=dict(size=12, color='white'),
            showgrid=False,
            range=[start_year - 0.5, end_year + 0.5]
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=False,
        height=600,
        width=1000
    )

    return fig_maternal_mr

# %% [markdown]
# Loading CSV

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# %%
def load_and_clean_data(file_path):
    data = pd.read_csv(file_path, skiprows=1)
    data.columns = ['GHO_CODE', 'GHO_DISPLAY', 'GHO_URL', 'YEAR_DISPLAY', 'STARTYEAR', 
                    'ENDYEAR', 'REGION_CODE', 'REGION_DISPLAY', 'COUNTRY_CODE', 
                    'COUNTRY_DISPLAY', 'DIMENSION_TYPE', 'DIMENSION_CODE', 
                    'DIMENSION_NAME', 'Numeric', 'Value', 'Low', 'High']

    data['YEAR_DISPLAY'] = pd.to_numeric(data['YEAR_DISPLAY'], errors='coerce')
    data['Numeric'] = pd.to_numeric(data['Numeric'], errors='coerce')
    data['Low'] = pd.to_numeric(data['Low'], errors='coerce')
    data['High'] = pd.to_numeric(data['High'], errors='coerce')

    data.dropna(subset=['YEAR_DISPLAY', 'Numeric'], inplace=True)
    return data

# %% [markdown]
# Anemia Trends

# %%
def plot_anemia_trends():
    file_path = "maternal_and_reproductive_health_indicators_lbn (1).csv"
    data = load_and_clean_data(file_path)
    indicator_code = 'NUTRITION_ANAEMIA_NONPREGNANT_NUM'
    filtered_data = data[data['GHO_CODE'] == indicator_code]
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='YEAR_DISPLAY', y='Numeric', data=filtered_data, marker='o')

    plt.xticks(ticks=filtered_data['YEAR_DISPLAY'].unique(), 
               labels=filtered_data['YEAR_DISPLAY'].unique().astype(int), 
               rotation=0, fontweight='bold')

    plt.yticks(fontweight='bold')

    plt.title('Trend of Number of Non-Pregnant Women with Anemia Over Years', fontweight='bold')
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Number of Women', fontweight='bold')
    plt.grid(False)

    sns.set(style="whitegrid")
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return plt

# %% [markdown]
# Anemia Comparison

# %%
def plot_anemia_comparison():
    file_path = "maternal_and_reproductive_health_indicators_lbn (1).csv"
    data = load_and_clean_data(file_path)
    
    indicator_code_1 = 'NUTRITION_ANAEMIA_NONPREGNANT_NUM'
    indicator_code_2 = 'NUTRITION_ANAEMIA_PREGNANT_NUM'

    filtered_data_1 = data[data['GHO_CODE'] == indicator_code_1]
    filtered_data_2 = data[data['GHO_CODE'] == indicator_code_2]

    comparison_data = pd.merge(filtered_data_1[['YEAR_DISPLAY', 'Numeric']], 
                               filtered_data_2[['YEAR_DISPLAY', 'Numeric']], 
                               on='YEAR_DISPLAY', 
                               suffixes=('_non_pregnant', '_pregnant'))
    
    fig, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(x='YEAR_DISPLAY', y='Numeric_non_pregnant', data=comparison_data, marker='o', ax=ax1, color='blue', label='Non-Pregnant Women')
    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Number of Non-Pregnant Women', fontweight='bold', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_xticks(comparison_data['YEAR_DISPLAY'].unique())
    ax1.set_xticklabels(comparison_data['YEAR_DISPLAY'].unique().astype(int), fontweight='bold')
    ax1.grid(False)

    ax2 = ax1.twinx()
    sns.lineplot(x='YEAR_DISPLAY', y='Numeric_pregnant', data=comparison_data, marker='o', ax=ax2, color='orange', label='Pregnant Women')
    ax2.set_ylabel('Number of Pregnant Women', fontweight='bold', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    ax2.grid(False)

    plt.title('Comparison of Number of Women with Anemia Over Years', fontweight='bold')

    # Combine legends from both plots
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize='large', title_fontsize='13')

    fig.tight_layout()
    return plt

# %% [markdown]
# ## Streamlit

# %%
st.markdown("""
    <style>
    .main {
        background-color: black;
        color: white;
    }
    .css-18e3th9 {
        padding-top: 2rem;
    }
    .stSelectbox label, .stSelectbox div {
        color: white;
    }
    .stSlider > div {
        color: white;
    }
    .css-10trblm {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# %%
placeholder = st.empty()

# %%
st.title("Lebanese Maternal and Reproductive Health Dashboard")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Graphs", "Recommendations", "Facts"])

if page == "Introduction":
    st.header("Introduction")
    st.image("Downpic.cc-2296723531.jpg", use_column_width=True)
    st.write("""
        Welcome to the **Lebanese Maternal and Reproductive Health Dashboard**. This interactive platform is dedicated to providing valuable insights into the maternal and reproductive health landscape in Lebanon. Through a comprehensive analysis of key health indicators, this dashboard aims to enhance our understanding of maternal and neonatal health trends, identify areas for improvement, and support data-driven decision-making for healthcare providers and policymakers.
    """)
    st.write("""
        The well-being of mothers and their children is paramount to the overall health of any society. In Lebanon, maternal and reproductive health services face unique challenges that require continuous monitoring and improvement. By exploring various statistics related to childbirth, neonatal mortality, and maternal mortality, this dashboard serves as a crucial tool for highlighting successes, uncovering gaps, and formulating targeted interventions to improve health outcomes.
    """)
    st.write("""
        Our project is guided by the belief that informed decisions lead to better health outcomes. We invite you to explore the data visualizations, understand the trends, and join us in advocating for a healthier future for mothers and children in Lebanon. Together, we can make a significant impact by addressing the critical aspects of maternal and reproductive health through evidence-based practices and policy recommendations.
    """)

elif page == "Graphs":
    st.sidebar.title("Graphs")
    option = st.sidebar.selectbox("Select a graph to display", (
        "Childbirth Attendance",
        "Place of Childbirth",
        "Private Hospital Deliveries",
        "Cesarean Delivery Rate",
        "Lebanese Births and Deaths",
        "Lebanese and Non-Lebanese Births",
        "Neonatal Mortality Rate",
        "Maternal Mortality Rate",
        "Anemia Trends",
        "Comparison of Anemia in Non-Pregnant and Pregnant Women"
    ))

    year_range = st.sidebar.slider("Select year range", min_value=2010, max_value=2022, value=(2010, 2022))

    if option == "Childbirth Attendance":
        st.plotly_chart(childbirth_attendance_graph())
    elif option == "Place of Childbirth":
        st.plotly_chart(place_of_birth_graph())
    elif option == "Private Hospital Deliveries":
        st.plotly_chart(private_hospital_deliveries_graph())
    elif option == "Cesarean Delivery Rate":
        st.plotly_chart(cesarean_delivery_rate_graph(year_range[0], year_range[1]))
    elif option == "Lebanese Births and Deaths":
        st.plotly_chart(births_and_deaths_graph(year_range[0], year_range[1]))
    elif option == "Lebanese and Non-Lebanese Births":
        st.plotly_chart(lebanese_non_lebanese_birth_graph(year_range[0], year_range[1]))
    elif option == "Neonatal Mortality Rate":
        st.plotly_chart(neonatal_mr_graph(year_range[0], year_range[1]))
    elif option == "Maternal Mortality Rate":
        st.plotly_chart(maternal_mr_graph(year_range[0], year_range[1]))
    elif option == "Anemia Trends":
        st.pyplot(plot_anemia_trends().gcf())
    elif option == "Comparison of Anemia in Non-Pregnant and Pregnant Women":
        st.pyplot(plot_anemia_comparison().gcf())

elif page == "Recommendations":
    st.header("Recommendations and Conclusion")
    st.write("""
        Based on the analysis of maternal and reproductive health statistics in Lebanon, we offer the following recommendations:
        
        1. **Increase Access to Skilled Birth Attendants**: Ensure that all childbirths are attended by skilled professionals to reduce risks associated with unskilled attendants.
        
        2. **Improve Healthcare Facilities**: Enhance the quality and availability of healthcare facilities, particularly in public hospitals and rural areas.
        
        3. **Promote Cesarean Delivery Awareness**: Educate expecting mothers about the implications of cesarean deliveries and provide necessary support and guidance.
        
        4. **Reduce Neonatal Mortality**: Implement targeted interventions to reduce neonatal mortality rates, focusing on high-risk groups and areas.
        
        5. **Address Maternal Mortality**: Strengthen maternal healthcare services, particularly for non-Lebanese populations, to reduce maternal mortality rates.

        These recommendations aim to improve maternal and reproductive health outcomes in Lebanon, ensuring better healthcare services and support for mothers and children.
    """)
    st.write("""
        In conclusion, our analysis highlights significant areas for improvement in maternal and reproductive health in Lebanon. 
        By implementing the recommended strategies, we can enhance healthcare services, reduce mortality rates, and ensure a healthier future for mothers and children.
    """)

elif page == "Facts":
    st.header("Facts about Maternal and Reproductive Health in Lebanon")
    
    st.markdown("""
        <style>
            .fact-table {
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1.1em;
                font-family: 'Times New Roman', serif;
                background-color: #f9f9f9;
                color: #333;
                border-radius: 5px 5px 0 0;
                overflow: hidden;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }
            .fact-table thead tr {
                background-color: #009879;
                color: #ffffff;
                text-align: left;
                font-weight: bold;
            }
            .fact-table th,
            .fact-table td {
                padding: 12px 15px;
            }
            .fact-table tbody tr {
                border-bottom: 1px solid #dddddd;
            }
            .fact-table tbody tr:nth-of-type(even) {
                background-color: #f3f3f3;
            }
            .fact-table tbody tr:last-of-type {
                border-bottom: 2px solid #009879;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <table class="fact-table">
            <thead>
                <tr>
                    <th>Aspect</th>
                    <th>Fact</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Maternal Mortality Rate</td>
                    <td>29 deaths per 100,000 live births (2020)</td>
                </tr>
                <tr>
                    <td>Skilled Birth Attendance</td>
                    <td>Over 98% of births attended by skilled health personnel</td>
                </tr>
                <tr>
                    <td>Antenatal Care Coverage</td>
                    <td>89% of women receive at least four antenatal care visits</td>
                </tr>
                <tr>
                    <td>Postnatal Care Coverage</td>
                    <td>85% of women receive postnatal care within two days of delivery</td>
                </tr>
                <tr>
                    <td>Contraceptive Prevalence Rate</td>
                    <td>Approximately 55% of women use modern contraceptive methods</td>
                </tr>
                <tr>
                    <td>Adolescent Birth Rate</td>
                    <td>22 births per 1,000 women aged 15-19</td>
                </tr>
                <tr>
                    <td>Total Fertility Rate</td>
                    <td>2.1 children per woman</td>
                </tr>
                <tr>
                    <td>C-Section Rate</td>
                    <td>Around 45%, higher than the recommended rate of 10-15%</td>
                </tr>
                <tr>
                    <td>Maternal Health Services</td>
                    <td>Widely available in urban areas; limited access in rural and remote areas</td>
                </tr>
                <tr>
                    <td>Government Initiatives</td>
                    <td>Various programs to improve maternal health, including subsidies and education</td>
                </tr>
                <tr>
                    <td>Challenges</td>
                    <td>Economic instability, refugee influx, and healthcare system strain</td>
                </tr>
            </tbody>
        </table>
    """, unsafe_allow_html=True)
