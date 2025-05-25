# Personalizar marcadores

Personalizaremos marcadores das seguintes maneiras:

#### Método 1: Símbolo de marcador Matplotlib

Usaremos o parâmetro `marker` para especificar um símbolo de marcador Matplotlib.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### Método 2: Marcador do TeX

Usaremos o parâmetro `marker` para especificar um marcador do TeX, envolvendo o nome de um símbolo TeX em sinais de $.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### Método 3: Marcador de caminho

Usaremos o parâmetro `marker` para especificar um caminho personalizado de N vértices como um array-like (N, 2).

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### Método 4: Marcador de polígono regular

Usaremos o parâmetro `marker` para especificar um marcador de polígono regular usando uma tupla (N, 0).

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### Método 5: Marcador de estrela regular

Usaremos o parâmetro `marker` para especificar um marcador de estrela regular usando uma tupla (N, 1).

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### Método 6: Marcador de asterisco regular

Usaremos o parâmetro `marker` para especificar um marcador de asterisco regular usando uma tupla (N, 2).

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
