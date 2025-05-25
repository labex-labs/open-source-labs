# Carregar e Explorar o Conjunto de Dados

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

Baixamos o conjunto de dados usando a função `fetch_lfw_people()` do scikit-learn. Em seguida, exploramos o conjunto de dados obtendo o número de amostras, altura e largura das imagens. Também obtemos os dados de entrada `X`, o alvo `y`, os nomes dos alvos `target_names` e o número de classes `n_classes`.
