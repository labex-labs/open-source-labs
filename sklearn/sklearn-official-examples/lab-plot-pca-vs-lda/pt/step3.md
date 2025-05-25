# Executar LDA

Agora, executaremos a Análise Discriminante Linear (LDA) no conjunto de dados para identificar atributos que explicam a maior variação entre as classes. Ao contrário da PCA, o LDA é um método supervisionado que utiliza rótulos de classe conhecidos.

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("LDA do Conjunto de Dados Iris")
plt.show()
```
