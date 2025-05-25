# Fazer previsões usando o modelo

Após ajustar o modelo, podemos usá-lo para fazer previsões em novos dados. Vamos criar um novo array `X_new` e prever os valores-alvo correspondentes.

```python
# Criar novos dados para previsão
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```
