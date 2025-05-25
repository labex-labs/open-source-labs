# Plotar Imagens de Teste

Definimos uma função auxiliar para plotar as imagens de teste. Usamos esta função para plotar as imagens de teste não corrompidas e ruidosas.

```python
import matplotlib.pyplot as plt

def plot_digits(X, title):
    fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize=24)

plot_digits(X_test, "Imagens de teste não corrompidas")
plot_digits(
    X_test_noisy, f"Imagens de teste ruidosas\nMSE: {np.mean((X_test - X_test_noisy) ** 2):.2f}"
)
```
