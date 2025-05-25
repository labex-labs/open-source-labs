# Adicionando Texto Multilinha ao Segundo Subgráfico

No segundo subgráfico, adicionaremos texto multilinha usando a função `text`. Podemos especificar a posição, tamanho, alinhamento vertical e horizontal, e `bbox` do texto.

```python
ax1.text(0.29, 0.4, "Mat\nTTp\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.34, 0.4, "Mag\nTTT\n123", size=18,
         va="baseline", ha="left", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.95, 0.4, "Mag\nTTT$^{A^A}$\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))
```
