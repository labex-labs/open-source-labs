# 画像とパッチの例を示す関数の定義

`image_and_patch_example` という関数を定義します。この関数は軸オブジェクトを入力として受け取り、ランダムな画像を描画し、そのプロットにパッチを追加します。

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
