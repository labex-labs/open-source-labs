# リストと数学

_注意：リストは数学演算用に設計されていません。_

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

具体的には、MATLAB、Octave、R などのように、リストはベクトルや行列を表しません。ただし、それを支援するパッケージもいくつかあります (たとえば、[numpy](https://numpy.org))。

このチャレンジでは、Python のリストデータ型を実験します。前のセクションでは、株価シンボルを含む文字列を扱いました。

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

文字列を `split()` 演算子を使って名前のリストに分割します。

```python
>>> symlist = symbols.split(',')
```
