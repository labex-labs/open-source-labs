# Preparar o Conjunto de Dados

Precisamos achatá-las imagens para transformar cada matriz bidimensional de valores em escala de cinza da forma `(8, 8)` em forma `(64,)`. Isto fornecerá um conjunto de dados com a forma `(n_amostras, n_características)`, onde `n_amostras` é o número de imagens e `n_características` é o número total de pixels em cada imagem.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```
