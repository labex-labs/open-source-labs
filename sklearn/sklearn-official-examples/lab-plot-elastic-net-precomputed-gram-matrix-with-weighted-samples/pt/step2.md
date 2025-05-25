# Pré-calculando a Matriz Gram com Amostras Ponderadas

Para ajustar a rede elástica usando a opção `precompute` juntamente com os pesos de amostra, primeiro devemos centralizar a matriz de projeto e redimensioná-la pelos pesos normalizados antes de calcular a matriz Gram. Centralizamos a matriz de projeto subtraindo a média ponderada de cada coluna de característica de cada linha. Em seguida, redimensionamos a matriz de projeto centralizada multiplicando cada linha pela raiz quadrada do peso normalizado correspondente. Finalmente, calculamos a matriz Gram tomando o produto escalar da matriz de projeto redimensionada com sua transposta.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
