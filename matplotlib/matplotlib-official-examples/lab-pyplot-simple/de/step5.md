# Speichern des Plots

Sie können den Plot als Bilddatei mithilfe der `savefig`-Methode speichern. Der folgende Code speichert den Plot als PNG-Bild:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Einfacher Plot')
plt.xlabel('Index')
plt.ylabel('Zahlen')
plt.savefig('simple_plot.png')
```
