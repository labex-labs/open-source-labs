# Personalizar o Gráfico

Podemos personalizar o gráfico adicionando rótulos, um título e ajustando os rótulos do eixo x e a legenda. Também definiremos o limite do eixo y para garantir que todos os nossos dados sejam visíveis.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
