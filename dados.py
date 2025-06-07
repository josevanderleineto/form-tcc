# app.py
import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

# Carregando os dados
df = pd.read_csv('respostas.csv')  # ou pd.read_excel('respostas.xlsx')

# Iniciando o app com tema bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Análise do Formulário Quilombola"

# Gráfico 1: Gênero
fig_genero = px.pie(df, names='Gênero', title='Distribuição por Gênero', color_discrete_sequence=px.colors.sequential.RdBu)

# Gráfico 2: Universidade
fig_uni = px.bar(df['Universidade'].value_counts().reset_index(),
                 x='index', y='Universidade',
                 labels={'index': 'Universidade', 'Universidade': 'Quantidade'},
                 title='Universidade de Origem',
                 color='Universidade')

# Gráfico 3: Dificuldade de acesso
fig_dificuldade = px.histogram(df, x='Dificuldade de Acesso', title='Dificuldade de Acesso à Universidade')

# Gráfico 4: Apoio institucional
fig_apoio = px.pie(df, names='Tem apoio institucional?', title='Recebe Apoio Institucional?')

# Layout do Dashboard
app.layout = dbc.Container([
    html.H1("📊 Análise das Respostas - Jovens Universitários Quilombolas", className="text-center my-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_genero), md=6),
        dbc.Col(dcc.Graph(figure=fig_uni), md=6)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_dificuldade), md=6),
        dbc.Col(dcc.Graph(figure=fig_apoio), md=6)
    ]),

    html.Footer("Desenvolvido por Vanderlei Neto", className="text-center mt-4 text-muted")
], fluid=True)

# Executando o app
if __name__ == '__main__':
    app.run_server(debug=True)
