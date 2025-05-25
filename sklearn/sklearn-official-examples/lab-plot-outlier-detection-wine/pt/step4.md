# Detecção de Valores Discrepantes em Dados Complexos

Vamos realizar a detecção de valores discrepantes no conjunto de dados "em forma de banana" Wine. Usaremos os mesmos três classificadores anteriores e plotaremos os resultados.

```python
# Treinar uma fronteira para detecção de valores discrepantes com vários classificadores
xx2, yy2 = np.meshgrid(np.linspace(-1, 5.5, 500), np.linspace(-2.5, 19, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(2)
    clf.fit(X2)
    Z2 = clf.decision_function(np.c_[xx2.ravel(), yy2.ravel()])
    Z2 = Z2.reshape(xx2.shape)
    plt.contour(
        xx2, yy2, Z2, levels=[0], linewidths=2, colors=colors[i]
    )

# Plotar os resultados (= forma da nuvem de pontos de dados)
plt.figure(2)  # forma "banana"
plt.title("Detecção de valores discrepantes em um conjunto de dados real (reconhecimento de vinho)")
plt.scatter(X2[:, 0], X2[:, 1], color="black")
plt.xlim((xx2.min(), xx2.max()))
plt.ylim((yy2.min(), yy2.max()))
plt.ylabel("intensidade_cor")
plt.xlabel("flavanoides")
plt.show()
```
