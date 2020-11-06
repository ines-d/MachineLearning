import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import dash_table
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#app = dash.Dash()


#impoter le fichier carData.csv
car_data = pd.read_csv("/home/ines/Documents/Projet_1_achat_voiture/carData.csv")

text = '''
        Ce projet a pour but la determination du prix d'une voiture à partir de no données et on cherchant quels
        types de données a une influence sur son prix. 
        '''

def Header ():
    return html.Div([
        html.H1("Projet 1 : Achat de voiture"),
        dcc.Markdown(text, style={'font-size':'18px'})
        
    ])


# Generate Table
def generate_table(dataframe):
    return html.Div([   
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dataframe.columns],
            data=dataframe.to_dict('records'),
            editable=True,
            css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
            style_table={'overflowX': 'scroll',
                         'maxHeight': '1000px',
                         'maxWidth': '100%',
                         'overflowY': 'scroll',
                         'maxHeight': '300px',
                         'maxWidth': '1500px',
                         'width': '100%',
                         'Height' : '49%',
                         'display': 'inline-block',
                         'vertical-align': 'middle'},
            style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'center'},
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Date', 'Region']
            ],
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#a2cdf2',
                    'color': 'white'
                }
            ],
            style_header={
                'backgroundColor': '#C33544',
                'color' : 'white',
                'fontWeight': 'bold'
            },
        )
    ],className="twelve columns")


#fig = px.bar(car_data, x="Year", y="Selling_Price", barmode="group")
fig1 = px.bar(car_data, x="Year", y="Selling_Price", color="Fuel_Type", title="Long-Form Input")
fig2 = px.scatter(car_data, x='Year', y='Selling_Price', opacity=0.65,trendline='ols', trendline_color_override='red')
fig3 = go.Figure(data=[
    go.Bar(name='SF Zoo', x=car_data.Year, y= car_data.Selling_Price),
    go.Bar(name='LA Zoo', x=car_data.Year, y=car_data.Selling_Price)
])
# Change the bar mode
fig3.update_layout(barmode='stack')

fig4 = px.scatter_matrix(car_data,
    dimensions=["Car_Name","Year","Selling_Price", "Present_Price", "Kms_Driven","Fuel_Type","Seller_Type","Transmission","Owner"]
    ,color="Fuel_Type")

fig5 = px.histogram(car_data, x="Year", color="Fuel_Type")

text1 = '''
On exploite les données afin de pouvoir trouver une correllation entre elles.
'''
text2 = '''
On remarque une petite correlation entre les Années et le prix de vente des voitures, afin de mieux visualiser on trace un histogramme. 
'''
text3 = '''
Afin de pouvoir prédir le prix d'une voiture, on faire appliquer l'algorithme de la regression lineaire univariée.
'''
text4 = '''
Pour notre jeux de données, on a pas une grande correlation entre l'âge  et le prix de vente des voitres car le coeficient de correlation est
 de 0.23, en plus sur les graphiques on remarque que les nuages de point sont assés dispersés
'''
app.layout = html.Div([
    Header(),
    html.Div([ 
        #html.H4("Votre employeur a-t-il discuté officiellement de la santé mentale dans le cadre d'un programme de bien-être des employés ?"),
        html.H6("Tableau des données"),
        generate_table(car_data),
        html.Div([
            html.H3("Expolration des données"),
            dcc.Markdown(text1, style={'font-size':'18px'}),
            dcc.Graph(
                figure = fig4
                #fig.update_traces(marker=dict(size=5))
                #fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
            )
        ]),
        html.Div([
            html.H3("Histogramme"),
            dcc.Markdown(text2, style={'font-size':'18px'}),
            dcc.Graph(
                figure = fig5
                #fig.update_traces(marker=dict(size=5))
                #fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
            )
        ]),
        html.Div([
            html.H3("Regression linéaire univarié"),
            dcc.Markdown(text3, style={'font-size':'18px'}),
            dcc.Graph(
                figure = fig2
            )
        ], className="nine columns"),
        html.Div([
            dcc.Markdown(text4, style={'font-size':'18px'}),
        ])
        

    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
