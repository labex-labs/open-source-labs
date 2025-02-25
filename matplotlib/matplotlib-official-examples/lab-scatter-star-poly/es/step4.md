# Personalizar marcadores

Personalizaremos los marcadores de las siguientes maneras:

#### Método 1: Símbolo de marcador de Matplotlib

Utilizaremos el parámetro `marker` para especificar un símbolo de marcador de Matplotlib.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### Método 2: Marcador de TeX

Utilizaremos el parámetro `marker` para especificar un marcador de TeX al encerrar el nombre de un símbolo de TeX entre signos de dólar $.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### Método 3: Marcador de ruta

Utilizaremos el parámetro `marker` para especificar una ruta personalizada de N vértices como una matriz similar a (N, 2).

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### Método 4: Marcador de polígono regular

Utilizaremos el parámetro `marker` para especificar un marcador de polígono regular utilizando una tupla (N, 0).

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### Método 5: Marcador de estrella regular

Utilizaremos el parámetro `marker` para especificar un marcador de estrella regular utilizando una tupla (N, 1).

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### Método 6: Marcador de asterisco regular

Utilizaremos el parámetro `marker` para especificar un marcador de asterisco regular utilizando una tupla (N, 2).

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
