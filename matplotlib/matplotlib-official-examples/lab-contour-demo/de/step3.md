# Erstellen eines einfachen Konturplots mit Beschriftungen

Jetzt, wo wir unsere Daten haben, können wir einen einfachen Konturplot mit Beschriftungen in Standardfarben erstellen.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
