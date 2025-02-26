# ポートフォリオの読み込み

`stock.py` プログラムに `read_portfolio()` という関数を追加して、ポートフォリオデータのファイルを `Stock` オブジェクトのリストに読み込むようにします。動作方法は以下の通りです。

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

演習2.3の一部として、既に似た関数を書いています。デザインに関する議論: `read_portfolio()` は別の関数として、またはクラス定義の一部としてすべきでしょうか。

## 注:

`stock.py` ファイルに `read_portfolio()` 関数を追加します。
