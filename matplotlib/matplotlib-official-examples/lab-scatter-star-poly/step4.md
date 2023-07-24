# Customize markers

We will customize markers in the following ways:

#### Method 1: Matplotlib marker symbol

We will use the `marker` parameter to specify a Matplotlib marker symbol.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### Method 2: Marker from TeX

We will use the `marker` parameter to specify a marker from TeX by enclosing a TeX symbol name in $-signs.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### Method 3: Marker from path

We will use the `marker` parameter to specify a custom path of N vertices as a (N, 2) array-like.

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### Method 4: Regular polygon marker

We will use the `marker` parameter to specify a regular polygon marker using a tuple (N, 0).

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### Method 5: Regular star marker

We will use the `marker` parameter to specify a regular star marker using a tuple (N, 1).

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### Method 6: Regular asterisk marker

We will use the `marker` parameter to specify a regular asterisk marker using a tuple (N, 2).

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
