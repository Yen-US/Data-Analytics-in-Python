#Data Analysis imports
import pandas as pd
import pandas_profiling as pp

# Visualization Imports
import seaborn as sns
color = sns.color_palette()
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.express as px

#Data analysis report creation
df = pd.read_csv('DataSet.csv') #Import the CSV dataset file
#With pandas profilling creete the Data report
profile = pp.ProfileReport(df, title="Pandas Profiling Report", minimal=True, explorative=True) 
profile.to_file("CRCovidReport.html") #Save the date report in a HTML file

#From the analysis report, creation of the variables
def df_to_plotly(df):
    #Take the dataset information and assign it to the Plotly axes
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist()}

#Creation of the correlation matrix graphic with pandas
dfNew = df.corr() 
fig1 = go.Figure(data=go.Heatmap(df_to_plotly(dfNew))) 
with open('CorrelationMatrix.html', 'w') as f1: #Exporting the graphic to a HTML
    print(fig1.to_html(), file=f1)

#Dot graphic creation total_deaths vs total_cases
fig2 = px.scatter(df, x='total_deaths', y='total_cases')
fig2.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig2.update_layout(title_text='Total Covid cases vs Total Covid deaths in Costa Rica')
with open('DeathsvsCases.html', 'w') as f2:
    print(fig2.to_html(), file=f2)

#Dot graphic creation total_deaths vs total_vaccinations
fig3 = px.scatter(df, x='total_deaths', y='total_vaccinations')
fig3.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig3.update_layout(title_text='Total Covid deaths vs Total Covid vaccinations in Costa Rica')
with open('DeathsvsVaccines.html', 'w') as f3:
    print(fig3.to_html(), file=f3)