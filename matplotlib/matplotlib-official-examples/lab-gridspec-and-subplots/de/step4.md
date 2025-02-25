# Entfernen der zugrunde liegenden Achsen

Wir entfernen die zugrunde liegenden Achsen, die von den größeren Achsen bedeckt werden, die wir im nächsten Schritt erstellen werden.

```python
for ax in axs[1:, -1]:
    ax.remove()
```
