# Variierende Dichte

In diesem Schritt werden wir einen Streamplot mit variierender Dichte erstellen. Der Parameter `density` steuert die Anzahl der zu zeichnenden Strömungslinien. Höhere Werte führen zu mehr Strömungslinien.

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
