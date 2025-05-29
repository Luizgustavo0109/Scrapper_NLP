import stanza
import polars as pl

#stanza.download('pt')
nlp = stanza.Pipeline(lang='pt', processors='tokenize,pos,lemma')

def tokens(text: str) -> int:

    doc = nlp(text)
    return int(len([
        word.text for sentence in doc.sentences for word in sentence.words
        if word.upos != "PUNCT"
    ]))

def types(text: str) -> int:

    doc = nlp(text)
    return len (set([
        word.text for sentence in doc.sentences for word in sentence.words
        if word.upos != "PUNCT"
    ]))

def ttr(cols) -> float:
    """Type-token ratio."""
    return (cols['types'] / cols['tokens']) * 100

def lemmas(text: str) -> int:

    doc = nlp(text)
    return len (set([
        word.text for sentence in doc.sentences for word in sentence.words
        if word.upos != "PUNCT"
    ]))

df = pl.read_csv('matue_tratado.csv')

new_df = df.with_columns(
    (
        pl.col('letra')
        .map_elements(tokens, return_dtype=int)
        .alias('tokens')
    ),
    (
        pl.col('letra')
        .map_elements(types, return_dtype=int)
        .alias('types')
    ),
    (
        pl.col('letra')
        .map_elements(lemmas, return_dtype=int)
        .alias('lemmas')
    ),
).with_columns([
    pl.struct(['types', 'tokens'])
      .map_elements(
          lambda cols: (cols['types'] or 0) / (cols['tokens'] or 1) * 100,
          return_dtype=float
      ).alias('ttr'),

    pl.struct(['lemmas', 'tokens'])
      .map_elements(
          lambda cols: (cols['lemmas'] or 0) / (cols['tokens'] or 1) * 100,
          return_dtype=float
      ).alias('ltor'),

    pl.struct(['lemmas', 'types'])
      .map_elements(
          lambda cols: (cols['lemmas'] or 0) / (cols['types'] or 1) * 100,
          return_dtype=float
      ).alias('ltyr')
])

#print(new_df)

new_df.write_csv('matue_stats.csv')