# Etapa 2 – Tratamento e Preparação dos Dados
## Detecção de dados ausentes

Primeiramente, foi feita a verificação de dados ausentes no conjunto de dados.
Notou-se que certos valores estavam indicados por símbolos como "-", os quais não são considerados valores numéricos.

## Correção de inconsistências

Foram detectadas discrepâncias nos dados, tais como:

Existência de valores não numéricos em colunas de dados quantitativos
Colunas com nomes repetidos ou pouco informativos
Informações guardadas em formato textual ao invés de numérico

As seguintes medidas foram tomadas para resolver esses problemas:

Troca de valores inválidos por NaN
Transformação das colunas em tipos numéricos
Renomeação das colunas para facilitar a compreensão

## Padronização de variáveis

Para evitar inconsistências, as variáveis categóricas foram normalizadas, incluindo:

Eliminação de espaços em branco
Uniformização de letras minúsculas e maiúsculas

Isso assegura uma maior consistência nas análises subsequentes.

## Verificação de consistência dos dados

Foi feita uma verificação para assegurar que os valores totais estivessem de acordo com a soma de homens e mulheres.

Essa fase é crucial para confirmar a integridade dos dados.

## Preparação dos dados para análise

Os dados foram organizados e estruturados de maneira apropriada para a análise, incluindo:

Geração de novas variáveis (ex: percentual de homens)
Filtragem de informações significativas

# Análise da desigualdade educacional

Os gráficos mostram que a distribuição da escolaridade no Brasil não é homogênea. É possível concluir perceber que:

Existem diferenças notáveis entre as regiões, sendo que as regiões Sudeste e Sul apresentam uma maior proporção de pessoas com níveis mais altos de escolaridade em relação às regiões Norte e Nordeste.
A análise por cor ou raça mostra diferenças significativas, apontando que grupos como pessoas pretas e pardas têm, em média, menor acesso a graus mais altos de escolaridade.
No que diz respeito ao gênero, apesar das variações nas diferenças, persistem desigualdades que refletem padrões sociais históricos.

Esses resultados destacam que o acesso à educação no Brasil é afetado por fatores estruturais, mostrando que, embora seja um direito universal, sua distribuição é desigual entre diferentes grupos da população.