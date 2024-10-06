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

"""
    Desafio 2.

    Quantos filmes estão disponíveis na Netflix?

"""

#filtrando apenas as linhas aonde o "type" é "Movie"
df_filmes_netflix = df[(df["type"] == "Movie")]


# Verificar se há valores ausentes na coluna "type"
#print(df['type'].isnull().sum())


#selecionando a coluna "type" do dataframe filtrado apenas com os filmes, e contando quantas linhas retornará
contagem_filmes = df_filmes_netflix.groupby("type").size()


#escrevendo na tela o retorno atribuido ao "contagem_filmes"
print(f"\nDESAFIO 2\nTotal de filmes no dataset: \n{contagem_filmes}")
"""
    Resposta do desafio 2:

    type
    Movie    6131
    dtype: int64
"""





"""
    Desafio3.
    Quem são os 5 diretores com mais filmes e séries na plataforma?
"""

#remover linhas aonde não há diretor (NaN)
df_valido = df.dropna(subset=['director'])


#agrupar por diretor e tipo de conteúdo, e em seguida contar
diretores_por_tipo = df_valido.groupby(['director','type']).size().unstack(fill_value=0)

#Somar filmes e series para cada diretor
diretores_total = diretores_por_tipo.sum(axis=1).sort_values(ascending=False)

#pegar os primeiros 5 diretores
top_5_diretores = diretores_total.head(5)


#exibir na tela
print(f"\nDESAFIO 3\nOs top 5 diretores: \n{top_5_diretores}")
"""
    RESPOSTA DESAFIO 3:

    Os top 5 diretores: 
director
Rajiv Chilaka             19
Raúl Campos, Jan Suter    18
Suhas Kadav               16
Marcus Raboy              16
Jay Karas                 14
dtype: int64
"""


"""
    Desafio 4.
    Quais diretores também atuaram como atores em suas próprias produções?
"""

#filtrando as colunas de diretor e elenco, para garantir que apenas serão considerados dados relevantes para a 
#análise
df_validos = df.dropna(subset=["director","cast"])

#fazendo uma função para checar quais diretores também estão no elenco das produções
def diretor_atuou(row):
    #Vefirica se o nome do diretor aparece na lista de atores
    return any(diretor in row["cast"] for diretor in row['director'].split(', '))


#aplicando a função para checar quais diretores também estão entre os atores em suas produções
df_diretor_ator = df_validos[df_validos.apply(diretor_atuou, axis=1)]

df_diretor_ator_exibir = df_diretor_ator[["title", "director", "cast"]]

#Exibir os diretores que também atuaram atores em suas próprias produções
print(f"\nDESAFIO 4\n{df_diretor_ator_exibir}")


