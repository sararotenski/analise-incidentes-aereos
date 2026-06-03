import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ocorrencias/ocorrencia.csv', encoding='iso-8859-1', sep=';')
df2 = pd.read_csv('ocorrencias/ocorrencia_tipo.csv', encoding='iso-8859-1', sep=';')

#listando os aeródromos que tiveram incidentes graves
incidentes_graves = df[df['ocorrencia_classificacao'] == 'INCIDENTE GRAVE']
aeroportos = incidentes_graves['ocorrencia_aerodromo'].unique()
print(aeroportos)

#tabela mostrando quantos incidentes graves cada aeródromo teve
incidentes_graves = df[df['ocorrencia_classificacao'] == 'INCIDENTE GRAVE']
resultado = (incidentes_graves['ocorrencia_aerodromo'].value_counts().reset_index())
resultado.columns = ['Aeroporto', 'Quantidade de incidentes graves']
print(resultado)

#listando a frequência dos tipos de incidentes que ocorreram
frequencia = (df['ocorrencia_classificacao'].value_counts().reset_index())
frequencia.columns = ['Classificação', 'Quantidade']
print(frequencia)

#listando os tipos de ocorrências que aparecem nos incidentes graves
tipos_incidentes_graves = pd.merge(incidentes_graves, df2, on='codigo_ocorrencia1')
print('Tipo de ocorrência encontrados:')
print(tipos_incidentes_graves['ocorrencia_tipo'].unique())

print("\nQuantidade de cada tipo:")
print(tipos_incidentes_graves['ocorrencia_tipo'].value_counts())

#gráfico dos 10 tipos de ocorrência mais frequentes em acidentes graves
tipos_incidentes_graves_dez = (tipos_incidentes_graves['ocorrencia_tipo'].value_counts().head(10))
tipos_incidentes_graves_dez.plot(kind='bar', color='pink')
plt.title('10 tipos de ocorrência mais frequentes')
plt.xlabel('tipo de ocorrência')
plt.ylabel('quantidade')
plt.tight_layout()
plt.show()