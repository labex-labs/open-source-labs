# Criar uma figura e um objeto `ImageGrid`

Em seguida, criamos um objeto `figure` usando a função `plt.figure` e passamos o argumento `figsize` para definir o tamanho da figura. Em seguida, criamos um objeto `ImageGrid` usando a função `ImageGrid` e passamos a `figure`, `111` como o argumento de subplot, `(2, 2)` como o argumento `nrows_ncols` para criar uma grade de eixos 2x2 e `0.1` como o argumento `axes_pad` para definir o preenchimento entre os eixos.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
