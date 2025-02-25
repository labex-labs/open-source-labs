# Anpassen des Plots

Du kannst den Plot anpassen, indem du die Farben, die Linienstile und die Marker ändern. Hier ist ein Beispiel:

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
