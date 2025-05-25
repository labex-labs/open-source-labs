# Sombreamento Mais Próximo (Nearest Shading), Grade de Mesmo Formato

Normalmente, descartar uma linha e coluna de dados não é o que o usuário pretende quando define `X`, `Y` e `Z` com o mesmo formato. Para este caso, o Matplotlib permite `shading='nearest'` e centraliza os quadriláteros coloridos nos pontos da grade. Se uma grade que não tem o formato correto for passada com `shading='nearest'`, um erro será gerado. Podemos visualizar a grade usando o seguinte bloco de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
