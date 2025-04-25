# 演習 6.7：あなたのポートフォリオを監視する

`follow.py` プログラムを変更して、株価データのストリームを監視し、ポートフォリオ内の特定の株に関する情報を表示する株価情報表示を行うようにします。たとえば：

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

注：これが機能するには、`Portfolio` クラスが `in` 演算子をサポートする必要があります。演習 6.3 を参照して、`__contains__()` 演算子を実装してください。
