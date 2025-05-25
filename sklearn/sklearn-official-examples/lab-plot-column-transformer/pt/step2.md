# Criando Transformadores

Criaremos transformadores que extraem características do conjunto de dados. Definiremos duas funções que realizam a transformação de dados e, em seguida, usaremos o `FunctionTransformer` do Scikit-Learn para criar os transformadores.

```python
def subject_body_extractor(posts):
    # constrói um array de tipo objeto com duas colunas
    # primeira coluna = 'assunto' e segunda coluna = 'corpo'
    features = np.empty(shape=(len(posts), 2), dtype=object)
    for i, text in enumerate(posts):
        # variável temporária `_` armazena '\n\n'
        headers, _, body = text.partition("\n\n")
        # armazena o texto do corpo na segunda coluna
        features[i, 1] = body

        prefix = "Subject:"
        sub = ""
        # salva o texto após 'Subject:' na primeira coluna
        for line in headers.split("\n"):
            if line.startswith(prefix):
                sub = line[len(prefix) :]
                break
        features[i, 0] = sub

    return features

subject_body_transformer = FunctionTransformer(subject_body_extractor)

def text_stats(posts):
    return [{"length": len(text), "num_sentences": text.count(".")} for text in posts]

text_stats_transformer = FunctionTransformer(text_stats)
```
