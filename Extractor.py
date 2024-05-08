import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from mpl_toolkits.mplot3d import Axes3D



'''
como eu nao tenho cabeçalhos e não posso editar o excel no formato real dele, pois não  estou com 
a versao atualizada, isso geraria mais problemas. Não irei agrupar dados para correlações
dados.pairplot(dados, hue = 'eixo_x')
'''

# Caminho completo do arquivo
caminho_arquivo = r'C:\Users\Marce\Desktop\PID-Controller-Python-main\a1.csv'

# Lê o arquivo CSV usando ponto e vírgula como delimitador
dados = pd.read_csv(caminho_arquivo, delimiter=';', header=None) # eu precisei passar o cabeçalho como None
dados.replace(',', '.', regex=True, inplace=True)
#print(dados.head())
#print(dados['nome'].value_counts()) #isso é uma estrutura caso eu tivesse o nome da coluna
#print(dados.keys())
#dados.drop(dados.columns[0], axis = 1))  # eu consigo remover uma coluna



print(dados.index) #ele me retorna um start, stop e ums step
dados.index == 1
print(dados[dados.index ==1]

'''
isso foi uma forma de fazer:
'''
coluna_0 = dados.iloc[:,0]
coluna_0 = pd.to_numeric(coluna_0, errors='coerce')

eixo_x = dados.value_counts().keys()
eixo_y = dados.value_counts().values

#nao posso usar meu grafico de barras pois não há strings, não há rotulos.

coluna_1 = dados.iloc[:,1]
coluna_1 = pd.to_numeric(coluna_1, errors='coerce')
coluna_2 = dados.iloc[:,2]
coluna_2 = pd.to_numeric(coluna_2, errors='coerce')
coluna_3 = dados.iloc[:,3]
coluna_3 = pd.to_numeric(coluna_3, errors='coerce')

media_coluna_1 = coluna_1.mean()
mediana_coluna_1 = coluna_1.median()


#x,y
#primeiramente, plotar 3d. tempo, saida, entrada.
#preciso adicionar os titulos agora.
'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Adiciona os pontos ao gráfico 3D
ax.plot(coluna_0, coluna_1, coluna_2)
ax.set_xlabel('Tempo')
ax.set_ylabel('Saida')
ax.set_zlabel('Entrada')
plt.show()


plt.plot(coluna_0,coluna_1)
plt.xlabel('Tempo')
plt.ylabel('Saida')
plt.show()

plt.plot(coluna_0,coluna_2)
plt.xlabel('Tempo')
plt.ylabel('Entrada')
plt.show()

plt.plot(coluna_2,coluna_1)
plt.xlabel('Entrada')
plt.ylabel('Saida')
plt.show()

'''


#dados[coluna_1] = pd.to_numeric(dados[coluna_1])
#media = coluna_1.mean()

#quero fazer uns testes de validação primeiramente.
#dados.groupby([coluna_1]).agg(['mean', 'median'])
#dados.groupby([coluna_1]).agg(['mean'])




#depois eu quero plotar tudo
#depois dividir em segmentos a partir de uma regra, pra não tem erro.

""" poso dividir pra fazer uma checagem de valores antigos e valores futuros. se o salto for grande e constante, é pq o degrau vai mudar se não é apenas ruido."""

def verifica_futuro(indice_tempo, valor):
    return

def verifica_passado(indice_tempo, valor):
    return

def separa_seção1(entrada, tempo):
    '''
    preciso verificar quando que ele muda de estado
    '''
    dataframes_divididos = []
    #instantes separados
    mudanca_estado = np.where(np.diff(entrada))[0] + 2
    mudanca_estado
    instantes = np.append(0,mudanca_estado)

    print(instantes)
    #separar em 10 dataframes. porém eu preciso salvar os 10 dataframes em variaveis diferentes.

    for i in range(len(instantes) - 1):
        inicio = instantes[i]
        fim = instantes[i + 1]
        dataframe_temp = dados.iloc[inicio:fim]
        dataframes_divididos.append(dataframe_temp)


    df1 = dataframes_divididos[0]

    return mudanca_estado, df1


def separa_seção(entrada, tempo):
    '''
    Preciso verificar quando que ele muda de estado
    '''
    dataframes_divididos = []
    mudanca_estado = np.where(np.diff(entrada))[0] + 2
    instantes = np.append(0, mudanca_estado)

    print(instantes)

    # Separar em 10 dataframes
    for i in range(len(instantes) - 1):
        inicio = instantes[i]
        fim = instantes[i + 1]
        dataframe_temp = dados.iloc[inicio:fim]
        dataframes_divididos.append(dataframe_temp)

    # Armazenar os dataframes em um dicionário
    df_dict = {f"df{i+1}": df for i, df in enumerate(dataframes_divididos)}

    return mudanca_estado, df_dict

posicao_mudanca, df_dict = separa_seção(dados.iloc[:, 1], dados.iloc[:, 0])

# Acesse os dataframes por meio do dicionário
df1 = df_dict['df1']
df2 = df_dict['df2']
# ... df3, df4, ..., df10

print(df1)
# Imprima ou faça o que quiser com os dataframes individuais

posicao_mudança,df1 = separa_seção(coluna_2, coluna_0)
print(df1)
#print(datafff)




""" 
# Iterar sobre as linhas do DataFrame
for indice, linha in dados.iterrows():
    posicao = linha.iloc[0]  # Primeira coluna
    saida = linha.iloc[1]    # Segunda coluna
    valor_degrau = linha.iloc[2]  # Terceira coluna

    # Adicionar os valores à lista
    lista_resultados.append([posicao, saida, valor_degrau])

# Exibir a lista de resultados
"""

