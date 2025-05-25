# Plotar o Texto

Agora que definimos o texto, podemos plotá-lo usando Matplotlib. Nesta etapa, criamos uma figura e adicionamos o texto a ela usando o método `fig.text()`.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i + .5) / len(tests), s, fontsize=32)

plt.show()
```
