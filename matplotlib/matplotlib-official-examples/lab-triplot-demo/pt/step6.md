# Plotar a Triangulação Especificada pelo Usuário

Vamos plotar a triangulação especificada pelo usuário usando a função `triplot`.

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
ax2.triplot(x, y, triangles, 'go-', lw=1.0)
ax2.set_title('Triplot da Triangulação Especificada pelo Usuário')
ax2.set_xlabel('Longitude (graus)')
ax2.set_ylabel('Latitude (graus)')
```
