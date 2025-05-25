# Criar um Gráfico de Escala Linear

O primeiro tipo de transformação de escala que exploraremos é a linear. Esta é a escala padrão utilizada no Matplotlib. Para criar um gráfico de escala linear, usamos o método `set_yscale()` e passamos a string `'linear'`. Também adicionamos um título e uma grelha ao gráfico.

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
