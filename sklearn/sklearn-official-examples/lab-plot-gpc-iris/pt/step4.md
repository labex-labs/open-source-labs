# Plotando as probabilidades previstas

Agora, plotaremos as probabilidades previstas para cada ponto na malha. Criaremos dois subplots: um para o kernel RBF isotrópico e outro para o kernel RBF anisotrópico. Usaremos o método `predict_proba` para obter as probabilidades previstas para cada ponto na malha. Em seguida, plotaremos as probabilidades previstas como um gráfico de cores na malha. Também plotaremos os pontos de treinamento para cada espécie de flor Iris.

```python
titles = ["RBF Isotrópico", "RBF Anisotrópico"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # Plota as probabilidades previstas. Para isso, atribuiremos uma cor a
    # cada ponto na malha [x_min, m_max]x[y_min, y_max].
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # Coloca o resultado em um gráfico de cores
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # Plota também os pontos de treinamento
    plt.scatter(X[:, 0], X[:, 1], c=np.array(["r", "g", "b"])[y], edgecolors=(0, 0, 0))
    plt.xlabel("Comprimento da sépala")
    plt.ylabel("Largura da sépala")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(
        "%s, LML: %.3f" % (titles[i], clf.log_marginal_likelihood(clf.kernel_.theta))
    )

plt.tight_layout()
plt.show()
```
