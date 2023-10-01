import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import mysql.connector
import plotly.express as px

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='data_cars'
)

# Consulta SQL para obter os dados
query = "SELECT marca.nome AS Marca, carro.nome AS Carro, ano, preco FROM carro INNER JOIN marca ON carro.marca_id = marca.marca_id;"
df = pd.read_sql_query(query, conn)

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da interface
app.layout = html.Div([
    dcc.Dropdown(
        id='marca-dropdown',
        options=[{'label': marca, 'value': marca} for marca in df['Marca'].unique()],
        value=df['Marca'].unique()[0],  # Valor inicial
        clearable=False
    ),
    dcc.Graph(id='carros-preco-grafico'),
    dcc.Graph(id='carros-quantidade-grafico')
])

# Função para calcular a quantidade de carros por marca
def calcular_quantidade_por_marca(df, marca_selecionada):
    filtered_df = df[df['Marca'] == marca_selecionada]
    return len(filtered_df)

# Atualizar os gráficos com base na marca selecionada
@app.callback(
    [Output('carros-preco-grafico', 'figure'),
     Output('carros-quantidade-grafico', 'figure')],
    [Input('marca-dropdown', 'value')]
)
def update_graph(selected_marca):
    filtered_df = df[df['Marca'] == selected_marca]
    
    # Gráfico de barras para o preço dos carros
    fig_preco = px.bar(filtered_df, x='Carro', y='preco', title=f'Preço dos carros da marca {selected_marca}')
    fig_preco.update_xaxes(title='Carro')
    fig_preco.update_yaxes(title='Preço')
    
    # Calcular a quantidade de carros por marca
    quantidade_por_marca = calcular_quantidade_por_marca(df, selected_marca)
    fig_quantidade = px.bar(
        x=[selected_marca],
        y=[quantidade_por_marca],
        title=f'Quantidade de carros para a marca {selected_marca}'
    )
    fig_quantidade.update_xaxes(title='Marca')
    fig_quantidade.update_yaxes(title='Quantidade de Carros')

    return fig_preco, fig_quantidade

if __name__ == '__main__':
    app.run_server(debug=True)
