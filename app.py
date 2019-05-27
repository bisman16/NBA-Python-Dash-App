import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table_experiments as dt


import pandas as pd
import plotly.graph_objs as go

df = pd.read_excel(
    'https://s3.amazonaws.com/programmingforanalytics/NBA_data.xlsx')

# These are for all plots except the last one
size = [i for i in (df['Salary']/1000000)]
age = [i for i in df['Age']]
win_rate = [i for i in (df['Wins']*100/df['Games_played'])]
games = [i for i in df['Games_played']]
ppgame = [i for i in df['Points_per_game']]
salary = [i for i in df['Salary']]

# This is for the last plot
age_ranges = ((20, 25), (25, 30), (30, 40))


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    
    html.H1(children='NBA Basketball Dashboard', style={'font-family': 'Dosis', 'color': '#4D637F', 'text-align': 'center'}),
                                                        
    html.H2(children='This dashboard gives interesting insights about the salary of NBA Basketball players\
            with the help of table and plots. You can scroll down to see all plots and \
            interact with them by choosing the variables.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    html.Br(),
            
                                                        
    html.H2(children='1. Table', style={'font-family': 'Dosis', 'color': '#4D637F', 'text-align': 'center'}),
    html.H2(children='Let us start visualizing the dataset by generating a table.', style={'font-family': 'Dosis', 'color': '#4D637F'}),                                 
                                                        
    generate_table(df),
    html.Br(),
    
    html.H2(children='Observations: From the table above, we can see that there are 17 columns (variables)\
            in the dataset. It will be interesting to see how Salary of these players vary with Age, Wins, Points per game etc.\
            We will get those insgihts by plotting the graphs as below.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    
    html.Br(),
    
    html.H2(children='2. Box and Whisker Plot', style={'font-family': 'Dosis', 'color': '#4D637F', 'text-align': 'center'}),

        html.H2(children='Now, let us see the descriptive analysis of some key variables such as Age, Points \
            per game, losses and Salary with the help of Box and Whisker plot. You can choose the variable from the dropdown option below.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    html.Br(),
                                                       
    dcc.Dropdown(
        id='box-option',
        options=[
            {'label': 'Age', 'value': 'Age'},
            {'label': 'Points per game', 'value': 'Points_per_game'},
            {'label': 'Losses', 'value': 'Losses'},
            {'label': 'Salary', 'value': 'Salary'}
        ],
        value='Age',
        style={'marginBottom': 10, 'marginTop': 100, 'width': 300}
    ),
    dcc.Graph(id='graph-box'),
    

     
    html.H2(children='Observations: Median age of players is 27.5 years and 50% of the players are between 24.5 and 29.5 years old. \
            Median points per game were 25.85 and 50% of the players scored between 24.1 and 27.35 points. \
            Median losses per player were 29 matches and 50% of the players lost between 23.5 and 39.5 matches. \
            Median salary of players was $25.43 Million (M) and 50% of the players earned between $19.24M and $30.56M. ', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    html.Br(),
    

    
    html.H2(children='3. Scatter Plots', style={'font-family': 'Dosis', 'color': '#4D637F', 'text-align': 'center'}),
    
        
    html.H2(children='Let us find the relation between different variables by plotting scatter graphs. ', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    
     html.Br(),
        
    html.H2(children='A) Plot of Salary as Dependent variable & Age, Games played as Independent variables. Salary is represented as bubble size.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    
     html.Br(),
     
     # plot 1 age~games played
             html.Div(children=[
            dcc.Graph(
                    id = 'age-gameplayed',
                    figure = {
                            'data': [{'x': age,
                                     'y': games,
                                     'name': 'age-gameplayed',
                                     'mode': 'markers',
                                     'marker': {'size':size,
                                                'color':'purple'}
                                     }],
                            'layout': {
                                    'xaxis':{'title':'Age'},
                                    'yaxis':{'title':'Games Played'},
                                    'title': 'Age ~ Games Played (Salary as Bubble Size)'
                                    
                                    #'margin':{'l': 40, 'b': 40, 't': 10, 'r': 10}
                                    }                              
                            }),
             html.H2(children='Observations: There is a high correlation between Age and Salary. The older the player is \
                     higher the salary he gets. It sounds logical as higher the age, higher the experience in the game. However, there seems to be \
                     no correlation between games played and Salary. Thus, Salary is dependent on Age.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
             html.Br(),

                ]),
     html.Br(),
     
     html.H2(children='B) Plot of Salary as Dependent variable & Points per game, Win rate as Independent variables. Salary is represented as bubble size.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    
     html.Br(),
     
     # plot 2-  ppg ~ win rate
        html.Div(children=[
            dcc.Graph(
                    id = 'ppg-winrate',
                    figure = {
                            'data': [{'x': ppgame,
                                     'y': win_rate,
                                     'name': 'ppg-winrate',
                                     'mode': 'markers',
                                     'marker': {'size':size,
                                                'color':'blue'}
                                     }],
                            'layout': {
                                    'xaxis':{'title':'Point per Game'},
                                    'yaxis':{'title':'Win Rate'},
                                    'title': 'Point Per Game ~ Win Rate (Salary as Bubble Size)'
                                    
                                    #'margin':{'l': 40, 'b': 40, 't': 10, 'r': 10}
                                    }
                                    
                            }),
    
]),
                    html.H2(children='Observations: There is a high correlation between Win rate and Salary. The player with higher \
                     win rate has higher salary. However, there seems to be \
                     no correlation between Points per game and Salary. Thus, Salary is dependent on Win rate.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
             html.Br(),
                                 html.H2(children='Now, we want to know what factors influence Win rate, which further influences Salary. We \
                                         did a linear regression for feature selection and found that Field goal and 3-point percentage\
                                         are correlated with Win rate. So, we will now plot these two factors below.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
            html.Br(),
                
   
        # plot 3
        html.Div(children=[
                # plot 3 field goal/3p percentage as drop-down, win rate as y, age as slider
                 html.H2(children='C) Plot of Win rate as Dependent variable & Field goal, 3 point percentage as Independent variables.\
                        You can choose these 2 factors from the drop-down below and use age range as slider.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
    
     html.Br(),
            dcc.Dropdown(
                    id='p3-dropdown',
                    options=[
                        {'label': 'Goal Percenage', 'value': 'Field_goal_percentage'},
                        {'label': '3-Point Made', 'value': '3P_made_per_game'}
                            ],
                    value='Field_goal_percentage',
                    style={'width': '40%'}
                    ),
            
            dcc.Graph(id='final-plot'),
              html.Br(),
              html.Br(),
            
            dcc.Slider(
                    id='age-slider',
                    min=0,
                    max=len(age_ranges),
                    value=0,
                    marks={
                        i: f'from {x[0]} to {x[1]}' for i, x in enumerate(age_ranges)},
                    step=None                        
                    ),
                     html.H2(children='Observations: There is a high correlation between Win rate and 3-point percentage Field goal. The player with higher \
                     3-pointers and field goals has higher wins, thus higher salary.', style={'font-family': 'Dosis', 'color': '#4D637F'}),
             html.Br(), 
            
                ]),

           
])


@app.callback(
    Output('graph-box', 'figure'),
    [Input('box-option', 'value')]
    )
def box_plot(box_option):
    return {
        'data': [
            go.Box(x=df[box_option])
        ],
        'layout': {
            'xaxis': {'title': 'Age range'},
            'title': box_option.replace('_', ' ')
        }
    }



# define final plot function
@app.callback(
        Output('final-plot', 'figure'),
        [Input('p3-dropdown', 'value'),
         Input('age-slider','value')]
        )
def update_graph(dropdown_option, age_selected):
    age_range = age_ranges[age_selected]
    sub_df = df[(df.Age >= age_range[0]) & (df.Age < age_range[1])]
    Y=(sub_df['Wins']*100/sub_df['Games_played'])
    X=sub_df[dropdown_option]
    size=sub_df['Salary']/1000000    
    
    return { 
            'data': [go.Scatter(
                    x=X,
                    y=Y,
                    mode='markers',
                    marker={'size':size, 'opacity':0.5, 'color':'red'}
                    )],
            
            'layout': go.Layout(
                    xaxis={'title': str(dropdown_option)},
                    yaxis={'title': 'Win Rate'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 0}
                    )
            }

if __name__ == '__main__':
    app.run_server(debug=True)
