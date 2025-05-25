# Visualizando o Conjunto de Dados

Para uma melhor compreensão do conjunto de dados, podemos visualizar uma imagem de amostra usando matplotlib. O código a seguir exibe o último dígito do conjunto de dados:

```python
import matplotlib.pyplot as plt

# Exibir o último dígito
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```
