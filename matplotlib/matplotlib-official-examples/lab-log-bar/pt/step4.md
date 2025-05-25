# Personalizando o Gráfico

Podemos personalizar a aparência do nosso gráfico adicionando rótulos ao eixo x e ao eixo y, e definindo a escala do eixo y como logarítmica.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
