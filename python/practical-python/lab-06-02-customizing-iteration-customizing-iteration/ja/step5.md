# 演習6.6：データ生成にジェネレータを使用する

演習6.5のコードを見ると、コードの最初の部分はデータの行を生成していますが、`while` ループの末尾の文はデータを消費しています。ジェネレータ関数の主な特徴は、すべてのデータ生成コードを再利用可能な関数に移動できることです。

演習6.5のコードを変更して、ファイル読み取りをジェネレータ関数 `follow(filename)` で行うようにします。以下のコードが機能するようにします。

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... ここで出力の行が表示されるはずです...
```

株価情報表示のコードを変更して、次のようになるようにします。

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
