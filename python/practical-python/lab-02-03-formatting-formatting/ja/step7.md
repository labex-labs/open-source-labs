# 演習 2.9：データの収集

演習 2.7 では、株式ポートフォリオの損益を計算する`report.py`というプログラムを書きました。この演習では、これを次のような表を生成するように修正し始めます。

| 名前 | 株数 | 価格   | 変動   |
| ---- | ---- | ------ | ------ |
| AA   | 100  | 9.22   | -22.98 |
| IBM  | 50   | 106.28 | 15.18  |
| CAT  | 150  | 35.46  | -47.98 |
| MSFT | 200  | 20.89  | -30.34 |
| GE   | 95   | 13.48  | -26.89 |
| MSFT | 50   | 20.89  | -44.21 |
| IBM  | 100  | 106.28 | 35.84  |

このレポートでは、「価格」は株式の現在の株価であり、「変動」は初期購入価格からの株価の変動です。

上記のレポートを生成するには、まず表に表示されるすべてのデータを収集する必要があります。株式のリストと価格の辞書を入力として受け取り、上記の表の行を含むタプルのリストを返す`make_report()`関数を書きます。

この関数を`report.py`ファイルに追加します。対話的に試した場合の動作方法は次のとおりです。

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> report = make_report(portfolio, prices)
>>> for r in report:
        print(r)

('AA', 100, 9.22, -22.980000000000004)
('IBM', 50, 106.28, 15.180000000000007)
('CAT', 150, 35.46, -47.98)
('MSFT', 200, 20.89, -30.339999999999996)
('GE', 95, 13.48, -26.889999999999997)
...
>>>
```
