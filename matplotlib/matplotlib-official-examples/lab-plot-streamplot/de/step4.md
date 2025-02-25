# Variierende Farbe

In diesem Schritt werden wir einen Streamplot mit variierender Farbe erstellen. Der Parameter `color` nimmt ein 2D-Array entgegen, das die Größe des Vektorfelds repräsentiert. Hier verwenden wir die `U`-Komponente des Vektorfelds als Farbe.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
