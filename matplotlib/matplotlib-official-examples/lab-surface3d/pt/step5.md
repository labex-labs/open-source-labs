# Personalizar o Eixo Z

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

Personalizamos o eixo z usando a função `set_zlim()` para definir os limites do eixo z de -1.01 a 1.01. Em seguida, usamos a função `set_major_locator()` para definir o número de marcas (ticks) no eixo z para 10, usando `LinearLocator(10)`. Finalmente, usamos a função `set_major_formatter()` para formatar os rótulos das marcas do eixo z usando um `StrMethodFormatter`.
