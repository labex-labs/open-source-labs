# Predições e Intervalos de Confiança

Após ajustar o nosso modelo, vemos que os hiperparâmetros do kernel foram otimizados. Agora, usaremos o nosso kernel para calcular a previsão média de todo o conjunto de dados e traçar o intervalo de confiança de 95%.

```python
mean_prediction, std_prediction = gaussian_process.predict(X, return_std=True)

plt.plot(X, y, label=r"$f(x) = x \sin(x)$", linestyle="dotted")
plt.scatter(X_train, y_train, label="Observações")
plt.plot(X, mean_prediction, label="Previsão média")
plt.fill_between(
    X.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    alpha=0.5,
    label=r"Intervalo de confiança de 95%",
)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
_ = plt.title("Regressão por processo gaussiano em conjunto de dados sem ruído")
```
