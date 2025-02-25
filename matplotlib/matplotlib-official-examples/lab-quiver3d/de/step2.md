# Das Gitter erstellen

Als nächstes erstellen wir ein Gitter von Punkten, auf dem wir das Vektorfeld anzeigen werden. In diesem Beispiel erstellen wir ein Gitter von Punkten mit der `meshgrid`-Funktion von NumPy. Die `arange`-Funktion wird verwendet, um ein Array von gleichmäßig verteilten Punkten innerhalb eines angegebenen Intervalls zu erstellen.

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```
