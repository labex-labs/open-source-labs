# Sombreamento Gouraud (Gouraud Shading)

O `Gouraud shading` também pode ser especificado, onde a cor nos quadriláteros é interpolada linearmente entre os pontos da grade. Os formatos de `X`, `Y` e `Z` devem ser os mesmos. Podemos visualizar a grade usando o seguinte bloco de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
