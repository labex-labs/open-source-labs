# Plotar Resultados

Plotamos os dígitos originais e os dígitos reamostrados lado a lado em uma grade de 4x11.

```python
import matplotlib.pyplot as plt

# transformar os dados em uma grade 4x11
new_data = new_data.reshape((4, 11, -1))
real_data = digits.data[:44].reshape((4, 11, -1))

# plotar os dígitos reais e os dígitos reamostrados
fig, ax = plt.subplots(9, 11, subplot_kw=dict(xticks=[], yticks=[]))
for j in range(11):
    ax[4, j].set_visible(False)
    for i in range(4):
        im = ax[i, j].imshow(
            real_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)
        im = ax[i + 5, j].imshow(
            new_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)

ax[0, 5].set_title("Seleção dos dados de entrada")
ax[5, 5].set_title('"Novos" dígitos extraídos do modelo de densidade do kernel')

plt.show()
```
