# Treinar e Avaliar o Classificador Gaussian Naive Bayes

Agora, treinaremos o classificador Gaussian Naive Bayes no conjunto de treino e avaliaremos seu desempenho no conjunto de teste. Usaremos a classe `GaussianNB` do módulo `sklearn.naive_bayes`.

```python
from sklearn.naive_bayes import GaussianNB

# Criar um classificador Gaussian Naive Bayes
gnb = GaussianNB()

# Treinar o classificador
gnb.fit(X_train, y_train)

# Prever a variável alvo para o conjunto de teste
y_pred = gnb.predict(X_test)

# Calcular a precisão do classificador
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Precisão:", accuracy)
```
