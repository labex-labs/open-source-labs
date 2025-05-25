# Sombreamento Plano (Flat Shading)

A função `pcolormesh` em Matplotlib pode visualizar grades 2D. A especificação da grade com o mínimo de suposições é `shading='flat'` e se a grade for uma unidade maior que os dados em cada dimensão, ou seja, tiver a forma `(M+1, N+1)`. Nesse caso, `X` e `Y` especificam os cantos dos quadriláteros que são coloridos com os valores em `Z`. Podemos visualizar a grade usando o seguinte bloco de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
