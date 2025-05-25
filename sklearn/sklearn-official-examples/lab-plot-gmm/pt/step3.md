# Implementar o Modelo de Mistura Gaussiana

Neste passo, iremos implementar o Modelo de Mistura Gaussiana utilizando a classe `GaussianMixture` do scikit-learn. Iremos ajustar o modelo aos nossos dados e prever as etiquetas de cluster para cada ponto de dados. Finalmente, iremos plotar os resultados.

```python
# Criar um objeto GMM com 5 componentes
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# Ajustar o GMM aos dados
gmm.fit(X)

# Prever as etiquetas de cluster
Y_ = gmm.predict(X)

# Plotar os resultados
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Modelo de Mistura Gaussiana")
plt.show()
```
