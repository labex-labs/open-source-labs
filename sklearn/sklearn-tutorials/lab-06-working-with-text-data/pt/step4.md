# Treinando o Modelo

Agora que temos nossos vetores de recursos, podemos treinar um modelo para classificar os dados de texto. Neste exemplo, usaremos o algoritmo Multinomial Naive Bayes, um algoritmo popular para classificação de texto.

```python
from sklearn.naive_bayes import MultinomialNB

# Treinar o modelo
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

Agora, nosso modelo está treinado e pronto para previsão.
