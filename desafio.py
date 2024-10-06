#importando a biblioteca pandas para fazer as analises de dados
import pandas as pd


#criando um dataframe com base no arquivo csv enviado para fazer o desafio
df = pd.read_csv("netflix_titles.csv")


"""Desafio 1.

    Quais colunas estão presentes no dataset?
"""


#usando a função print para mostrar as colunas do dataframe na tela
print(f'DESAFIO 1\nAs colunas presentes no dataframe "netflix_titles.csv": \n{df.columns}')

"""
    Resposta do desafio 1:

    Index(['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description'],
      dtype='object')
"""



#filtrando apenas as linhas aonde o "type" é "Movie"
df_filmes_netflix = df[(df["type"] == "Movie")]

#selecionando a coluna "type" do dataframe filtrado apenas com os filmes, e contando quantas linhas retornará
contagem_filmes = df_filmes_netflix.groupby("type").size()

#escrevendo na tela o retorno atribuido ao "contagem_filmes"
print(f"DESAFIO 2\nTotal de filmes no dataset: \n{contagem_filmes}")

