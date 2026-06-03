# ✈️ Análise de Incidentes Aéreos

Projeto de análise exploratória de dados utilizando Python, Pandas e Matplotlib para investigar ocorrências aeronáuticas registradas no Brasil.

## Objetivo

Analisar os registros de ocorrências aeronáuticas e identificar padrões relacionados a incidentes graves, aeródromos envolvidos e tipos de ocorrência.

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub

## Base de Dados

Foram utilizados os seguintes conjuntos de dados:

- `ocorrencia.csv`
- `ocorrencia_tipo.csv`

## Análises Realizadas

- Identificação dos aeródromos que registraram incidentes graves.
- Quantificação de incidentes graves por aeródromo.
- Relacionamento entre ocorrências e seus respectivos tipos.
- Exploração e filtragem de dados utilizando Pandas.

## Principais Resultados

- Foram identificados **313 aeródromos** com registros de incidentes graves.
- Foi gerada uma tabela com a quantidade de incidentes graves por aeródromo.
- Foram identificados os tipos de ocorrência associados aos incidentes graves.
- Foi gerado um gráfico dos 10 tipos de ocorrência mais frequentes em incidentes graves.

## Estrutura do Projeto

```text
incidentes-aereos-analysis/
│
├── ocorrencias/
│   ├── ocorrencia.csv
│   └── ocorrencia_tipo.csv
│
├── analysis.py
├── README.md
└── .gitignore
```

## Como Executar

1. Clone o repositório:

```bash
git clone <https://github.com/sararotenski/analise-incidentes-aereos.git>
```

2. Instale as dependências:

```bash
pip install pandas matplotlib
```

3. Execute o projeto:

```bash
python analysis.py
```

## Autora

Sara Rotenski Pereira
