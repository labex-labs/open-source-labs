# Visualizar a Função Prevista

Após o treinamento do modelo, vamos visualizar a função prevista juntamente com os pontos de dados originais.

```python
# Gerar pontos de dados de teste
X_test = np.linspace(0, 5, 100)[:, None]

# Prever os valores-alvo
y_pred = krr.predict(X_test)

# Visualizar os dados e a função prevista
plt.scatter(X, y, color='blue', label='Dados')
plt.plot(X_test, y_pred, color='red', label='Função Prevista')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
