# App  
# Sebastian Larsen, KEA, Delivery 1

############################## Imports #####################

import dash
from dash import html
from dash import dcc 


# Div.
import pandas as pd

# Plotly
import plotly.express as px

############################## Get data #####################
#import databaseconnect as thisDatabase




import mysql.connector

#this function will work as our personal connector, with the users own SQL information. We will use dbconnect() multiple times thourgh our program
def dbconnect():
	connection = mysql.connector.connect(
		host="sela-mysql-4semester.mysql.database.azure.com",
		user="sela",
		password="2021q3-Opmedkop30",
		database="delivery1")
	return connection

thisConn = dbconnect()

### DATA###

SQL_data_empsales = pd.read_sql_query("select * from empolyee_sale", thisConn)
SQL_data_prosales = pd.read_sql_query("select * from product_sale", thisConn)

##### FIGURES######

fig_employee=px.histogram(SQL_data_empsales,x='employee_id', y='sold',title='Employees sales' ) # BAR  SKAL LAVES OM TIL ET ANDET DIAGRAM
fig_employee.update_layout(bargap=0.2)
fig_product=px.histogram(SQL_data_prosales,x='productname', y='sold', title='Products sales' )

dash_app=dash.Dash(__name__)
app=dash_app.server

### LAYOUT ####


dash_app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Sales report for employees'),

        html.Div(children='''
            Total sales by each employee.
        '''),

        dcc.Graph(
            id='sales_employee',
            figure=fig_employee
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Sales report for products'),

        html.Div(children='''
            Total sale for each product.
        '''),

        dcc.Graph(
            id='sales_product',
            figure=fig_product
        ),  
    ]),
])


if __name__ == '__main__':
    dash_app.run_server(debug=True)