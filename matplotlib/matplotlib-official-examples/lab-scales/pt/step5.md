# Criar um Gráfico de Escala Logit

O quarto tipo de transformação de escala que exploraremos é a logit. Este tipo de escala é útil ao lidar com dados que são limitados por 0 e 1. Para criar um gráfico de escala logit, usamos o método `set_yscale()` e passamos a string `'logit'`. Também adicionamos um título e uma grelha ao gráfico.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
