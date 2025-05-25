# Implementar o Modelo de Mistura Gaussiana Bayesiano

Neste passo, iremos implementar o Modelo de Mistura Gaussiana Bayesiano utilizando a classe `BayesianGaussianMixture` do scikit-learn. Este modelo possui uma priori de processo de Dirichlet que adapta automaticamente o número de clusters com base nos dados. Iremos ajustar o modelo aos nossos dados e prever as etiquetas de cluster para cada ponto de dados. Finalmente, iremos plotar os resultados.

```python
# Criar um objeto GMM Bayesiano com 5 componentes
dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type="full")

# Ajustar o GMM Bayesiano aos dados
dpgmm.fit(X)

# Prever as etiquetas de cluster
Y_ = dpgmm.predict(X)

# Plotar os resultados
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Modelo de Mistura Gaussiana Bayesiano com uma priori de processo de Dirichlet")
plt.show()
```
