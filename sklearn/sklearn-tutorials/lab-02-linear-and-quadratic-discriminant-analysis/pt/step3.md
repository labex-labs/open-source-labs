# Treinar e visualizar os classificadores

Agora, treinaremos os classificadores LDA e QDA nos dados sintéticos e visualizaremos as fronteiras de decisão.

```python
# Treinar o classificador LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Treinar o classificador QDA
qda = QuadraticDiscriminantAnalysis()
qda.fit(X, y)

# Plotar as fronteiras de decisão
def plot_decision_boundary(classifier, title):
    h = 0.02  # tamanho do passo na malha
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.title(title)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plot_decision_boundary(lda, 'Análise Discriminante Linear')

plt.subplot(1, 2, 2)
plot_decision_boundary(qda, 'Análise Discriminante Quadrática')

plt.tight_layout()
plt.show()
```
