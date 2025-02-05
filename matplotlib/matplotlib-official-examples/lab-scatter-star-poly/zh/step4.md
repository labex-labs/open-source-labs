# 自定义标记

我们将通过以下方式自定义标记：

#### 方法一：Matplotlib标记符号

我们将使用 `marker` 参数来指定一个Matplotlib标记符号。

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### 方法二：来自TeX的标记

我们将使用 `marker` 参数，通过在 $ 符号中括住一个TeX符号名称来指定一个来自TeX的标记。

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### 方法三：来自路径的标记

我们将使用 `marker` 参数，通过一个 (N, 2) 数组形式指定一个由N个顶点组成的自定义路径。

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### 方法四：正多边形标记

我们将使用 `marker` 参数，通过一个元组 (N, 0) 指定一个正多边形标记。

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### 方法五：正星形标记

我们将使用 `marker` 参数，通过一个元组 (N, 1) 指定一个正星形标记。

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### 方法六：正星号标记

我们将使用 `marker` 参数，通过一个元组 (N, 2) 指定一个正星号标记。

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
