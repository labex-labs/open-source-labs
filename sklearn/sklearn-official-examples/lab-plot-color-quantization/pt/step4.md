# Prever Índices de Cores Usando um Livro de Códigos Aleatório

Preveremos os índices de cores na imagem completa usando um livro de códigos aleatório.

```python
# Obter um livro de códigos aleatório
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# Prever índices de cores na imagem completa usando o livro de códigos aleatório
print("Prevendo índices de cores na imagem completa (aleatório)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"feito em {time() - t0:0.3f}s.")
```
