# Plotar a Estimativa de Densidade

Agora, plotaremos a estimativa de densidade da mistura de gaussianas. Criaremos uma malha de pontos sobre o intervalo do conjunto de dados e calcularemos a probabilidade logarítmica negativa prevista pelo GMM para cada ponto. Em seguida, exibiremos as pontuações previstas como um gráfico de contorno e dispersaremos os dados de treinamento.

```python
# exibir as pontuações previstas pelo modelo como um gráfico de contorno
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Estimativa de Densidade com Modelos de Mistura Gaussiana")
plt.axis("tight")
plt.show()
```
