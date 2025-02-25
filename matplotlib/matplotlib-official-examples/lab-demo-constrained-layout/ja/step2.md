# サンプルプロットの定義

x と y のラベルとタイトル付きの単純な折れ線グラフを作成する関数を定義します。

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
