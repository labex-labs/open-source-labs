# Criar uma Figura e Eixos

Criaremos uma figura e um objeto de eixos usando `plt.subplots()`. A função `imshow()` é usada para exibir os dados aleatórios como uma imagem.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
