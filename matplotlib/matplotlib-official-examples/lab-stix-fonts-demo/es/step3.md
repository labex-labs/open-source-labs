# Graficar el Texto

Ahora que hemos definido el texto, podemos graficarlo usando Matplotlib. En este paso, creamos una figura y agregamos el texto a ella usando el método `fig.text()`.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i +.5) / len(tests), s, fontsize=32)

plt.show()
```
