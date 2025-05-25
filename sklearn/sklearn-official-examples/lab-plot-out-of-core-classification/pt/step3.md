# Configurar o vetorizador e reservar um conjunto de teste

```python
# Criar o vetorizador e limitar o número de recursos a um máximo razoável
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# Iterador sobre arquivos SGML Reuters analisados.
data_stream = stream_reuters_documents()

# Aprendemos uma classificação binária entre a classe "acq" e todas as outras.
# "acq" foi escolhida porque está mais ou menos distribuída uniformemente nos arquivos Reuters.
# Para outros conjuntos de dados, deve-se ter cuidado para criar um conjunto de teste com uma porção realista de instâncias positivas.
all_classes = np.array([0, 1])
positive_class = "acq"

# Aqui estão alguns classificadores que suportam o método `partial_fit`
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# Estatísticas dos dados de teste
test_stats = {"n_test": 0, "n_test_pos": 0}

# Primeiro, reservamos um número de exemplos para estimar a precisão
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("O conjunto de teste é de %d documentos (%d positivos)" % (len(y_test), sum(y_test)))
```
