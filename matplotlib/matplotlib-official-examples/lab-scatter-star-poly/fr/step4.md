# Personnaliser les marqueurs

Nous allons personnaliser les marqueurs de la manière suivante :

#### Méthode 1 : Symbole de marqueur Matplotlib

Nous allons utiliser le paramètre `marker` pour spécifier un symbole de marqueur Matplotlib.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### Méthode 2 : Marqueur issu de TeX

Nous allons utiliser le paramètre `marker` pour spécifier un marqueur issu de TeX en entourant le nom d'un symbole TeX entre des signes $.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### Méthode 3 : Marqueur issu d'un chemin

Nous allons utiliser le paramètre `marker` pour spécifier un chemin personnalisé de N sommets sous forme d'un tableau semblable à un tableau (N, 2).

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### Méthode 4 : Marqueur de polygone régulier

Nous allons utiliser le paramètre `marker` pour spécifier un marqueur de polygone régulier en utilisant un tuple (N, 0).

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### Méthode 5 : Marqueur d'étoile régulière

Nous allons utiliser le paramètre `marker` pour spécifier un marqueur d'étoile régulière en utilisant un tuple (N, 1).

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### Méthode 6 : Marqueur d'astérisque régulier

Nous allons utiliser le paramètre `marker` pour spécifier un marqueur d'astérisque régulier en utilisant un tuple (N, 2).

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
