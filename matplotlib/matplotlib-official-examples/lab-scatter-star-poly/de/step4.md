# Marker anpassen

Wir werden Marker auf folgende Weise anpassen:

#### Methode 1: Matplotlib-Markersymbol

Wir werden das `marker`-Parameter verwenden, um ein Matplotlib-Markersymbol anzugeben.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### Methode 2: Marker aus TeX

Wir werden das `marker`-Parameter verwenden, um einen Marker aus TeX anzugeben, indem wir einen TeX-Symbolnamen in $-Zeichen einschließen.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### Methode 3: Marker aus Pfad

Wir werden das `marker`-Parameter verwenden, um einen benutzerdefinierten Pfad von N Eckpunkten als (N, 2) array-ähnlich anzugeben.

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### Methode 4: Regelmäßiges Polygonmarker

Wir werden das `marker`-Parameter verwenden, um einen regelmäßigen Polygonmarker mit einem Tupel (N, 0) anzugeben.

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### Methode 5: Regelmäßiger Sternmarker

Wir werden das `marker`-Parameter verwenden, um einen regelmäßigen Sternmarker mit einem Tupel (N, 1) anzugeben.

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### Methode 6: Regelmäßiger Sternchenmarker

Wir werden das `marker`-Parameter verwenden, um einen regelmäßigen Sternchenmarker mit einem Tupel (N, 2) anzugeben.

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
