# Ajustar o Regressor Huber

Agora, ajustaremos o HuberRegressor ao conjunto de dados. Ajustaremos o modelo em uma gama de valores de epsilon para mostrar como a função de decisão se aproxima da regressão Ridge à medida que o valor de epsilon aumenta.

```python
# Defina a faixa de valores para epsilon
epsilon_values = [1, 1.5, 1.75, 1.9]

# Defina os valores de x para plotagem
x = np.linspace(X.min(), X.max(), 7)

# Defina as cores para plotagem
colors = ["r-", "b-", "y-", "m-"]

# Ajuste o regressor huber em uma série de valores de epsilon.
for k, epsilon in enumerate(epsilon_values):
    huber = HuberRegressor(alpha=0.0, epsilon=epsilon)
    huber.fit(X, y)
    coef_ = huber.coef_ * x + huber.intercept_
    plt.plot(x, coef_, colors[k], label="perda huber, %s" % epsilon)

# Adicione uma legenda ao gráfico
plt.legend(loc=0)

# Exiba o gráfico
plt.title("HuberRegressor com Diferentes Valores de Epsilon")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
