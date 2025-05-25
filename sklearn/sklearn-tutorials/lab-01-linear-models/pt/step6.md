# Perceptron

O Perceptron é um algoritmo de classificação linear simples, adequado para aprendizado em larga escala. Ele atualiza seu modelo apenas em erros, tornando-o mais rápido de treinar do que o gradiente descendente estocástico (SGD) com perda de dobradiça. Os modelos resultantes também são mais esparsos.

Vamos ajustar um modelo perceptron.

```python
clf = linear_model.Perceptron(alpha=0.1)
clf.fit(X, y)

print(clf.coef_)
```

- Criamos uma instância de `Perceptron` com o parâmetro de regularização `alpha` definido como 0,1.
- Usamos o método `fit` para ajustar o modelo aos dados de treinamento.
- Imprimimos os coeficientes do modelo perceptron.
