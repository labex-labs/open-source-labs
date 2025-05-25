# Gerar um Polígono Preenchido

Agora, podemos gerar um polígono preenchido usando a função `fill()`. Usaremos a função do floco de neve de Koch para gerar as coordenadas do polígono.

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
