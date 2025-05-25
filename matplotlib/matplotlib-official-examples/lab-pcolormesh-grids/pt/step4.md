# Sombreamento Plano (Flat Shading), Grade de Mesmo Formato

Se a grade tiver o mesmo formato que os dados em cada dimensão, não podemos usar `shading='flat'`. Historicamente, o Matplotlib descartava silenciosamente a última linha e coluna de `Z` neste caso, para corresponder ao comportamento do Matlab. Se este comportamento ainda for desejado, basta descartar a última linha e coluna manualmente. Podemos visualizar a grade usando o seguinte bloco de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
