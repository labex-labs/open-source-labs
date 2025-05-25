# Executar PCA

Em seguida, executaremos PCA em nosso conjunto de dados. Primeiro, concatenamos `x`, `y` e `z` para formar uma matriz 3D `Y`. Em seguida, criamos uma instância da classe PCA e a ajustamos aos nossos dados. Podemos então acessar os componentes principais usando o atributo `components_` do objeto PCA.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
