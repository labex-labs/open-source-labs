# Avaliar a Importância das Características

Avaliamos a importância das características com base na diminuição média da impureza (MDI). As importâncias das características são fornecidas pelo atributo ajustado `feature_importances_` e são calculadas como a média e o desvio padrão da acumulação da diminuição da impureza em cada árvore.

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("Importâncias dos pixels usando valores de impureza")
plt.colorbar()
plt.show()
```
