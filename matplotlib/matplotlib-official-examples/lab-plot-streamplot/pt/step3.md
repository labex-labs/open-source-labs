# Densidade Variável

Nesta etapa, criaremos um streamplot com densidade variável. O parâmetro `density` controla o número de linhas de fluxo (streamlines) a serem plotadas. Valores mais altos resultarão em mais linhas de fluxo.

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
