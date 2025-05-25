# Melhorando o Modelo

Se a precisão do nosso modelo não for satisfatória, podemos tentar melhorá-lo ajustando os hiperparâmetros do algoritmo SVM. Por exemplo, podemos tentar alterar o valor do parâmetro `C`:

```python
# Criar o classificador SVM com um valor diferente de C
clf = SVC(kernel='linear', C=0.1)

# Treinar o classificador nos dados de treinamento
clf.fit(X_train, y_train)

# Predizer as etiquetas do conjunto de teste
y_pred = clf.predict(X_test)

# Calcular a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir a precisão do modelo
print("Precisão:", accuracy)
```
