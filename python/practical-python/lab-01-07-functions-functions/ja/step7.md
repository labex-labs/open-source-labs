# 演習 1.30：スクリプトを関数に変換する

演習 1.27 で `pcost.py` プログラムとして書いたコードを取り出し、関数 `portfolio_cost(filename)` に変換しましょう。この関数はファイル名を入力として受け取り、そのファイル内のポートフォリオデータを読み取り、ポートフォリオの合計コストを浮動小数点数として返します。

関数を使用するには、プログラムを変更して以下のようになるようにします：

```python
# pcost.py
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```

プログラムを実行すると、以前と同じ出力が表示されるはずです。プログラムを実行した後は、次のように入力することで対話的に関数を呼び出すこともできます：

```bash
$ python3 -i pcost.py
```

これにより、対話モードから関数を呼び出すことができます。

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

コードを対話的に試すことができることは、テストとデバッグに役立ちます。
