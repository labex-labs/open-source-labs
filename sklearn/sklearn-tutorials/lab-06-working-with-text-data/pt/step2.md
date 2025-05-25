# Pré-processamento dos Dados de Texto

Antes de usar os dados de texto para aprendizado de máquina, precisamos pré-processá-los. Isso envolve várias etapas, como remover pontuação, converter todo o texto para minúsculas e tokenizar o texto em palavras individuais. Podemos realizar essas etapas de pré-processamento usando o `CountVectorizer` e o `TfidfTransformer` do scikit-learn.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Pré-processar os dados de texto
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

Agora, nossos dados de texto estão pré-processados e prontos para extração de recursos.
