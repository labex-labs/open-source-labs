# Classificar as Características

Após ajustar os dados ao objeto RFE, podemos classificar as características com base em sua importância. Usaremos o atributo `ranking_` do objeto RFE para obter as classificações das características. Também redimensionaremos as classificações para corresponder à forma das imagens originais.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
