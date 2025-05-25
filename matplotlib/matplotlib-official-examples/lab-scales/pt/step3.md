# Criar um Gráfico de Escala Logarítmica

O próximo tipo de transformação de escala que exploraremos é a logarítmica. Para criar um gráfico de escala logarítmica, usamos o método `set_yscale()` e passamos a string `'log'`. Também adicionamos um título e uma grelha ao gráfico.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
