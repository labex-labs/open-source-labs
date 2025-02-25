# ハイパーリンク付きの散布図を作成する

このステップでは、散布図を作成し、マーカーにハイパーリンクを追加します。散布図を作成するコードは次のとおりです。

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

ハイパーリンクを追加するには、散布図オブジェクトの`set_urls()`メソッドを使用します。このメソッドは、URLのリストを引数として取ります。更新されたコードは次のとおりです。

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

最初の2つのマーカーはそれぞれ`https://www.bbc.com/news`と`https://www.google.com/`へのハイパーリンクを持ちます。3番目のマーカーはハイパーリンクを持ちません。最後に、`fig.savefig()`を使用してプロットをSVGファイルとして保存できます。

```python
fig.savefig('scatter.svg')
```
