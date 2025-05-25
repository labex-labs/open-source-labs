# Visualizar as Classificações das Características

Finalmente, plotaremos as classificações das características usando a biblioteca Matplotlib. Usaremos a função `matshow()` para exibir as classificações como uma imagem. Também adicionaremos uma barra de cores e um título ao gráfico.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Classificação de pixels com RFE")
plt.show()
```
