# Carregar os Dados

O primeiro passo é carregar o conjunto de dados de rostos Olivetti, que contém 400 imagens em tons de cinza de 64x64 pixels cada. Os dados são divididos em conjuntos de treino e teste. O conjunto de treino contém os rostos de 30 pessoas, e o conjunto de teste contém os rostos das pessoas restantes. Neste laboratório, vamos testar os algoritmos num subconjunto de cinco pessoas.

```python
# Carregar os conjuntos de dados de rostos
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Teste em pessoas independentes

# Teste num subconjunto de pessoas
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Metade superior dos rostos
X_train = train[:, : (n_pixels + 1) // 2]
# Metade inferior dos rostos
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
