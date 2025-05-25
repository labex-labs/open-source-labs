# Visualizar as fronteiras de decisão

Criaremos uma malha de pontos que cobre o espaço de características de entrada e usaremos cada classificador para prever as etiquetas dos pontos na malha. Em seguida, plotaremos as fronteiras de decisão e os pontos de dados rotulados.

```python
# Criar uma malha para plotar
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Definir uma tabela de cores para as etiquetas
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}

# Configurar os classificadores
classifiers = (ls30, st30, ls50, st50, ls100, rbf_svc)

# Plotar as fronteiras de decisão e os pontos de dados rotulados para cada classificador
for i, (clf, y_train, title) in enumerate(classifiers):
    # Plotar a fronteira de decisão
    plt.subplot(3, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Colocar o resultado num gráfico de cores
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis("off")

    # Plotar os pontos de dados rotulados
    colors = [color_map[y] for y in y_train]
    plt.scatter(X[:, 0], X[:, 1], c=colors, edgecolors="black")

    plt.title(title)

plt.suptitle("Os pontos não rotulados são coloridos de branco", y=0.1)
plt.show()
```
