# 2 番目のセットのハッチパターンを作成する

密度を高めるために、各パターンを 2 回繰り返して、2 番目のセットのハッチパターンを作成します。以下のリストを使用します。

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

四角形を作成するために、以前と同じループを使用します。

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
