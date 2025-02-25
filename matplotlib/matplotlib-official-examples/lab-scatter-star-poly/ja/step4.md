# マーカーのカスタマイズ

以下の方法でマーカーをカスタマイズします。

#### 方法1：Matplotlibマーカーシンボル

Matplotlibマーカーシンボルを指定するために`marker`パラメータを使用します。

```python
axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
axs[0, 0].set_title("marker='>'")
```

#### 方法2：TeXからのマーカー

TeXのシンボル名を$-記号で囲むことで、TeXからのマーカーを指定するために`marker`パラメータを使用します。

```python
axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")
```

#### 方法3：パスからのマーカー

N頂点のカスタムパスを(N, 2)の配列のように指定するために`marker`パラメータを使用します。

```python
verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
axs[0, 2].set_title("marker=verts")
```

#### 方法4：正多角形マーカー

タプル(N, 0)を使用して正多角形マーカーを指定するために`marker`パラメータを使用します。

```python
axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
axs[1, 0].set_title("marker=(5, 0)")
```

#### 方法5：正星型マーカー

タプル(N, 1)を使用して正星型マーカーを指定するために`marker`パラメータを使用します。

```python
axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
axs[1, 1].set_title("marker=(5, 1)")
```

#### 方法6：正のアスタリスクマーカー

タプル(N, 2)を使用して正のアスタリスクマーカーを指定するために`marker`パラメータを使用します。

```python
axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
axs[1, 2].set_title("marker=(5, 2)")
```
