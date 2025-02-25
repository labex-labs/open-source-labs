# Crear la figura

El último paso es crear la figura utilizando la función `plt.figure`. Estableceremos el tamaño de la figura en (7, 4) y llamaremos a la función `curvelinear_test1` creada en los Pasos 2-4.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
