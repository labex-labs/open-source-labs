# Visualizar a Função Prevista Otimizada

Finalmente, vamos visualizar a função prevista utilizando os hiperparâmetros otimizados.

```python
# Prever os valores-alvo usando o modelo otimizado
y_pred_opt = best_krr.predict(X_test)

# Visualizar os dados e a função prevista otimizada
plt.scatter(X, y, color='blue', label='Dados')
plt.plot(X_test, y_pred_opt, color='green', label='Função Prevista Otimizada')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
