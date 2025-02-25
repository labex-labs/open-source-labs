# Variierende Linienbreite

In diesem Schritt werden wir einen Streamplot mit variierender Linienbreite erstellen. Der Parameter `linewidth` steuert die Breite der Strömungslinien. Hier verwenden wir das zuvor berechnete `speed`-Array, um die Linienbreite zu variieren.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
