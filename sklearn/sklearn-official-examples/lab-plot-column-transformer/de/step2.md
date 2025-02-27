# Erstellen von Transformatoren

Wir werden Transformatoren erstellen, die Features aus dem Dataset extrahieren. Wir werden zwei Funktionen definieren, die die Datenumwandlung ausführen, und dann Scikit-Learn's `FunctionTransformer` verwenden, um Transformatoren zu erstellen.

```python
def subject_body_extractor(posts):
    # construct object dtype array with two columns
    # first column = 'subject' and second column = 'body'
    features = np.empty(shape=(len(posts), 2), dtype=object)
    for i, text in enumerate(posts):
        # temporary variable `_` stores '\n\n'
        headers, _, body = text.partition("\n\n")
        # store body text in second column
        features[i, 1] = body

        prefix = "Subject:"
        sub = ""
        # save text after 'Subject:' in first column
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
