# Definiere die explode-Funktion

Als nächstes definieren wir eine Funktion namens `explode`, die verwendet werden soll, um das Voxelbild des NumPy-Logos aufzuschließen. Diese Funktion nimmt ein NumPy-Array als Eingabe entgegen und gibt ein neues NumPy-Array zurück, das doppelt so groß wie das Eingabe-Array ist.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
