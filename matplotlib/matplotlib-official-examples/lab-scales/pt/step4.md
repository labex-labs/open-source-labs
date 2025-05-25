# Criar um Gráfico de Escala Logarítmica Simétrica

O terceiro tipo de transformação de escala que exploraremos é a logarítmica simétrica. Este tipo de escala é útil ao lidar com dados que contêm valores positivos e negativos. Para criar um gráfico de escala logarítmica simétrica, usamos o método `set_yscale()` e passamos a string `'symlog'`. Também definimos o parâmetro `linthresh` para `0.02` para especificar a faixa de valores em torno de zero que serão escalados linearmente. Também adicionamos um título e uma grelha ao gráfico.

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
