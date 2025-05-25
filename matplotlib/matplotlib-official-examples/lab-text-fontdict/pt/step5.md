# Adicionar Texto ao Gráfico

Podemos adicionar texto ao nosso gráfico usando a função `text()`. Neste exemplo, adicionaremos uma expressão LaTeX ao gráfico, utilizando o dicionário de fontes para personalizar o estilo.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```
