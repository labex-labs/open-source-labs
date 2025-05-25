# Definindo os Rótulos dos Ticks

Por padrão, os rótulos dos ticks em valores negativos são renderizados usando um sinal de menos Unicode em vez de um hífen ASCII. No entanto, podemos alterar esse comportamento definindo `axes.unicode_minus` como `False`.

```python
plt.rcParams['axes.unicode_minus'] = False
```
