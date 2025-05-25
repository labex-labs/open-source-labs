# Personalizando os Rótulos do Eixo X

Para personalizar os rótulos do eixo x, podemos usar a função `set_xticks`. Podemos especificar as posições e os rótulos dos ticks.

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```
