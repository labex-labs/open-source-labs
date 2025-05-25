# Destacando Extensões de um Eixo com `axhspan` e `axvspan`

Outro uso útil de regiões preenchidas é destacar extensões horizontais ou verticais de um Eixo (Axes). Para isso, o Matplotlib tem as funções auxiliares `axhspan` e `axvspan`. Consulte a galeria `axhspan_demo` para mais informações.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
