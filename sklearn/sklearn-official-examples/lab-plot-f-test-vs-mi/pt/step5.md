# Plotar os resultados

Agora, plotaremos a dependência do alvo em relação a cada característica e as pontuações do teste F e da informação mútua para cada característica.

```python
plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.scatter(X[:, i], y, edgecolor="black", s=20)
    plt.xlabel("$x_{}$".format(i + 1), fontsize=14)
    if i == 0:
        plt.ylabel("$y$", fontsize=14)
    plt.title("Teste F={:.2f}, MI={:.2f}".format(f_test[i], mi[i]), fontsize=16)
plt.show()
```
