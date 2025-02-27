# Graficar imágenes de prueba

Definimos una función auxiliar para graficar las imágenes de prueba. Utilizamos esta función para graficar las imágenes de prueba sin ruido y con ruido.

```python
import matplotlib.pyplot as plt

def plot_digits(X, title):
    fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize=24)

plot_digits(X_test, "Imágenes de prueba sin ruido")
plot_digits(
    X_test_noisy, f"Imágenes de prueba con ruido\nMSE: {np.mean((X_test - X_test_noisy) ** 2):.2f}"
)
```
