# Analise de Criminalidade no Brasil (SINESP)

Este projeto aplica tecnicas de Ciencia de Dados em indicadores reais de seguranca publica brasileira, focando na analise de ocorrencias e vitimas por estado.

## Integrantes
* **Giovani Andreoli** - RA: 251020738
* **Pablo Henrique Alves Pereira** - RA: 251023575

## Acesso ao Projeto
O desenvolvimento completo esta sendo realizado atraves do Google Colab.

> **Link para o Notebook:** https://colab.research.google.com/drive/1RfnN_eiZcWa04Z9D5ObVfPe5fy_3UWMQ?usp=sharing

---

## Estrutura do Projeto

O projeto esta dividido conforme as etapas solicitadas até o momento:

### 1. Aquisicao de Dados (Grupo 1)
* **Titulo:** Analise Temporal e Regional da Criminalidade no Brasil: Um Estudo sobre Ocorrencias de Crimes contra o Patrimonio e a Vida (2015-2022).
* **Dataset:** Dados Nacionais de Seguranca Publica - Unidade da Federacao (.xlsx).
* **Fonte:** SINESP / Ministerio da Justica e Seguranca Publica (MJSP).
* **Objetivo:** Identificar padroes sazonais e disparidades regionais para auxiliar no planejamento de operacoes e politicas de prevencao baseadas em evidencias.
* **Perguntas Analiticas:** O projeto busca responder questoes sobre sazonalidade mensal, variacao percentual entre estados, correlacao entre diferentes tipos penais e o impacto da pandemia de COVID-19 nos registros.

### 2. Limpeza e Preparacao (Grupo 2)
Nesta etapa, as bases de "Ocorrencias" e "Vitimas" passaram por:
* **Verificacao de Integridade:** Identificacao de dados nulos e analise dos tipos de dados (Dtypes).
* **Padronizacao:** Criacao de funcao para remocao de espacos em branco (strip) e conversao de textos para caixa alta (upper) em todas as colunas do tipo objeto.
* **Deduplicacao:** Verificacao e confirmacao de ausencia de linhas repetidas nas duas bases de dados.
* **Exportacao:** Geracao de arquivos finais no formato .csv (ocorrencias_limpo.csv e vitimas_limpo.csv).

---

## Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Ambiente:** Google Colab
* **Bibliotecas:**
    * Pandas: Manipulacao e analise de dados.
    * Numpy: Operacoes matematicas e arrays.
    * Matplotlib e Seaborn: Visualizacao de dados e graficos.

## Como rodar localmente
1. Clone este repositorio: `git clone https://github.com/claytontey/Aulas_Git-DS.git`
2. O dataset original encontra-se no caminho: `./Aulas_Git-DS/TP-1/Giovani_Pablo/dados/indicadoressegurancapublicauf.xlsx`
3. Instale as dependencias necessarias:
```bash
pip install pandas numpy matplotlib seaborn openpyxl