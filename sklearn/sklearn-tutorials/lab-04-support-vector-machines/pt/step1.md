# Classificação com SVM

- Comece importando as bibliotecas necessárias:

```python
from sklearn import svm
```

- Defina as amostras de treino `X` e as etiquetas das classes `y`:

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- Crie uma instância do classificador `SVC` e ajuste os dados:

```python
clf = svm.SVC()
clf.fit(X, y)
```

- Utilize o modelo treinado para prever novos valores:

```python
clf.predict([[2., 2.]])
```
