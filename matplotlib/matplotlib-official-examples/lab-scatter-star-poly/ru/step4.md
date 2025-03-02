# Настраиваем маркеры

Мы будем настраивать маркеры следующими способами:

#### Метод 1: Символ маркера Matplotlib

Мы будем использовать параметр `marker` для указания символа маркера Matplotlib.

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### Метод 2: Маркер из TeX

Мы будем использовать параметр `marker` для указания маркера из TeX, заключая имя символа TeX в знаки $.

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### Метод 3: Маркер из пути

Мы будем использовать параметр `marker` для указания пользовательского пути из N вершин в виде массива, подобного (N, 2).

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### Метод 4: Маркер правильного многоугольника

Мы будем использовать параметр `marker` для указания маркера правильного многоугольника с использованием кортежа (N, 0).

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### Метод 5: Маркер правильной звезды

Мы будем использовать параметр `marker` для указания маркера правильной звезды с использованием кортежа (N, 1).

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### Метод 6: Маркер правильного звездочки

Мы будем использовать параметр `marker` для указания маркера правильной звездочки с использованием кортежа (N, 2).

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
