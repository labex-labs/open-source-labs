# ドキュメント文字列

関数のドキュメント文字列を含めるのは良い慣例です。ドキュメント文字列は、関数名の直後に書かれる文字列です。これらは `help()`、統合開発環境（IDE）、その他のツールに提供されます。

```python
def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

ドキュメント文字列の良い慣例としては、関数が何を行うかを1文で簡潔にまとめることです。もっと詳細な情報が必要な場合は、使用例の短いサンプルと引数のより詳細な説明を含めてください。
