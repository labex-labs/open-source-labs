# Visualizar Dados

Vamos plotar a função verdadeira e as amostras geradas.

```python
plt.figure(figsize=(6, 4))
plt.plot(np.linspace(0, 1, 100), true_fun(np.linspace(0, 1, 100)), label="Função verdadeira")
plt.scatter(X, y, edgecolor="b", s=20, label="Amostras")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")
plt.show()
```
