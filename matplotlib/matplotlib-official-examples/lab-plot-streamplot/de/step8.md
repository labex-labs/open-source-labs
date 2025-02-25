# Ununterbrochene Strömungslinien

In diesem Schritt werden wir einen Streamplot mit ununterbrochenen Strömungslinien erstellen. Der Parameter `broken_streamlines` steuert, ob die Strömungslinien abgebrochen werden sollen, wenn sie die Grenze der Linien innerhalb einer einzelnen Gitze-Zelle überschreiten.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
