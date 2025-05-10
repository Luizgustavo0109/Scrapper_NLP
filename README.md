# Análise NLP das Letras do Matuê

Este projeto realiza uma análise de Processamento de Linguagem Natural (NLP) nas letras das músicas do artista brasileiro Matuê. Através de técnicas de web scraping, coleta-se dados do site Genius para posterior aplicação de algoritmos de NLP.

## Visão Geral

O projeto se divide em duas etapas principais:

1. **Coleta de Dados**: Extração automática das letras, nomes das músicas, álbuns e datas de lançamento.
2. **Processamento NLP**: Análise linguística das letras coletadas para identificação de padrões, temas recorrentes e evolução do estilo lírico do artista.

## Funcionalidades do Web Scraper

O código base fornecido realiza as seguintes operações:

- Extrai informações de todos os álbuns de Matuê na plataforma Genius
- Coleta metadados como nome do álbum e data de lançamento
- Para cada álbum, extrai todas as faixas e suas respectivas URLs
- Para cada faixa, obtém a letra completa da música
- Organiza todos os dados em formato CSV estruturado

## Análise NLP Planejada

Com base nos dados coletados, serão aplicadas as seguintes técnicas de NLP:

### 1. Pré-processamento Textual
- Normalização de texto (minúsculas, remoção de acentos)
- Remoção de stopwords (palavras comuns sem valor semântico)
- Tokenização (divisão do texto em unidades menores)
- Stemming/Lemmatização (redução de palavras à sua forma base)

### 2. Análise de Frequência
- Identificação das palavras e expressões mais utilizadas
- Análise de N-gramas (combinações frequentes de palavras)
- Evolução do vocabulário ao longo do tempo

### 3. Modelagem de Tópicos
- Aplicação de algoritmos como LDA (Latent Dirichlet Allocation)
- Identificação dos principais temas abordados nas músicas
- Visualização da distribuição de tópicos por álbum/período

### 4. Análise de Sentimentos
- Classificação do tom emocional das letras
- Identificação de mudanças de sentimento entre álbuns
- Correlação entre sentimento e fase da carreira

### 5. Análise Estilística
- Identificação de padrões rítmicos e estruturais
- Análise de complexidade linguística
- Estudo de figuras de linguagem e recursos estilísticos

## Considerações Éticas

Este projeto é desenvolvido apenas para fins acadêmicos e de pesquisa. Todo o conteúdo coletado permanece com seus direitos autorais pertencentes aos respectivos proprietários (Matuê e demais compositores). A utilização dos dados segue princípios de uso justo para análise científica.

## Contribuições

Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, abra uma issue ou envie um pull request.
