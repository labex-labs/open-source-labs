# Treinar o Classificador

Agora podemos criar e treinar o classificador SGD usando a classe SGDClassifier do scikit-learn. Usaremos a função de perda 'hinge', comumente utilizada para classificadores lineares.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
