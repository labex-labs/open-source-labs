# 深い考え方：「ダックタイピング」

[ダックタイピング](https://en.wikipedia.org/wiki/Duck_typing) は、オブジェクトが特定の目的に使用できるかどうかを判断するコンピュータプログラミングの概念です。これは、[ダックテスト](https://en.wikipedia.org/wiki/Duck_test) の応用です。

> 見た目がアヒルで、泳ぎ方がアヒルで、鳴き声がアヒルなら、おそらくそれはアヒルです。

上の `read_data()` の2番目のバージョンでは、関数は任意の反復可能オブジェクトを期待します。ファイルの行だけでなくです。

```python
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records
```

これは、他の _行_ と一緒に使用できることを意味します。

```python
# CSVファイル
lines = open('data.csv')
data = read_data(lines)

# 圧縮ファイル
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# 標準入力
lines = sys.stdin
data = read_data(lines)

# 文字列のリスト
lines = ['ACME,50,91.1','IBM,75,123.45',... ]
data = read_data(lines)
```

この設計にはかなりの柔軟性があります。

_質問：この柔軟性を受け入れるべきか、抵抗するべきか？_
