# Carregar e Exibir a Imagem Original

Começaremos carregando a imagem do rosto do guaxinim a partir do Scipy. Vamos exibir a imagem e verificar as suas dimensões, tipo de dados e utilização de memória.

```python
from scipy.misc import face
import matplotlib.pyplot as plt

raccoon_face = face(gray=True)

print(f"As dimensões da imagem são {raccoon_face.shape}")
print(f"O tipo de dados usados para codificar a imagem é {raccoon_face.dtype}")
print(f"O número de bytes usados na RAM é {raccoon_face.nbytes}")

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(raccoon_face, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Imagem Original")
ax[1].hist(raccoon_face.ravel(), bins=256)
ax[1].set_xlabel("Valor do Pixel")
ax[1].set_ylabel("Contagem de Pixels")
ax[1].set_title("Distribuição dos valores dos pixels")
_ = fig.suptitle("Imagem Original de um Rosto de Guaxinim")
```
