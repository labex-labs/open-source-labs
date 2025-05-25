# Avaliando o Modelo

Para avaliar o desempenho do nosso modelo, podemos usar um conjunto de teste separado. Podemos carregar o conjunto de teste usando o mesmo processo do conjunto de treinamento.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

Agora podemos pré-processar o conjunto de teste e extrair os vetores de recursos.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

Finalmente, podemos usar nosso modelo treinado para fazer previsões no conjunto de teste e calcular a precisão.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
