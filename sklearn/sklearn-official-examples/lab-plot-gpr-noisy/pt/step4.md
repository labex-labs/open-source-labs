# Visualização de Dados

Nesta etapa, visualizaremos o conjunto de dados de treinamento ruidoso juntamente com o sinal esperado.

```python
plt.plot(X, y, label="Sinal esperado")
plt.scatter(
    x=X_train[:, 0],
    y=y_train,
    color="black",
    alpha=0.4,
    label="Observações",
)
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
