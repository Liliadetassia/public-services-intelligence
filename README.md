# Public Services Intelligence Map

Aplicação de inteligência artificial e visualização geoespacial desenvolvida para apoio à gestão pública. O sistema opera de forma independente de APIs privadas, consumindo dados públicos estruturados em arquivos brutos (raw) e processados (processed), garantindo replicabilidade, soberania dos dados e operação offline.

## Objetivo
Apoiar gestores públicos na identificação de áreas com déficit de serviços essenciais, utilizando análise baseada em dados populacionais e demandas classificadas automaticamente.

## Tecnologias
- Python 3.10
- Streamlit
- Deck.GL + Mapbox
- IBGE API
- Brasil.io
- Machine Learning 

## Funcionalidades
- Mapa interativo de serviços públicos
- Classificação automática de demandas
- Heatmap de áreas críticas
- Normalização por população

## Aplicação em Políticas Públicas
Planejamento urbano, alocação de recursos, análise de impacto social e tomada de decisão baseada em evidências.

## Observações
Os dados geoespaciais seguem o padrão GeoJSON (RFC 7946). 
As dependências do projeto foram mantidas no mínimo necessário, reduzindo superfície de falhas, custos de infraestrutura e complexidade operacional.E o requests, pandas, sklearn, spacy?
Entram depois, se e somente se:
você adicionar IA (classificação / NLP),
consumir APIs,
análise estatística
