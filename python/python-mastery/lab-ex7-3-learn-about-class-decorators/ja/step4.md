# 行変換機能の追加

プログラミングにおいて、特にCSVファイルなどのデータソースからのデータを扱う際に、データ行からクラスのインスタンスを作成することはしばしば便利です。このセクションでは、データ行から `Structure` クラスのインスタンスを作成する機能を追加します。これを実現するために、`Structure` クラスに `from_row` クラスメソッドを実装します。

1. まず、`structure.py` ファイルを開く必要があります。ここでコードの変更を行います。ターミナルで以下のコマンドを使用します。

```bash
code ~/project/structure.py
```

2. 次に、`validate_attributes` 関数を変更します。この関数は、`Validator` インスタンスを抽出し、`_fields` と `_types` リストを自動的に構築するクラスデコレータです。型情報も収集するように更新します。

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

この更新された関数では、各バリデータから `expected_type` 属性を収集し、`_types` クラス変数に格納しています。これは、後でデータ行のデータを正しい型に変換する際に役立ちます。

3. 次に、`Structure` クラスに `from_row` クラスメソッドを追加します。このメソッドにより、リストまたはタプルであるデータ行からクラスのインスタンスを作成することができます。

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

このメソッドの動作は以下の通りです。

- リストまたはタプルの形式のデータ行を受け取ります。
- `_types` リストから対応する関数を使用して、行内の各値を期待される型に変換します。
- 変換された値を使用して、クラスの新しいインスタンスを作成して返します。

4. これらの変更を行った後、`structure.py` ファイルを保存します。これにより、コードの変更が保存されます。

5. `from_row` メソッドが期待通りに動作することを確認するためにテストしましょう。`Stock` クラスを使用して簡単なテストを作成します。ターミナルで以下のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

以下のような出力が表示されるはずです。

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

文字列値 '100' と '490.1' が自動的に正しい型（整数と浮動小数点数）に変換されたことに注意してください。これは、`from_row` メソッドが正しく動作していることを示しています。

6. 最後に、`reader.py` モジュールを使用してCSVファイルからデータを読み取ってみましょう。ターミナルで以下のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

CSVファイルの株式情報を示す出力が表示されるはずです。

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

`from_row` メソッドにより、CSVデータを `Stock` クラスのインスタンスに簡単に変換することができます。`read_csv_as_instances` 関数と組み合わせることで、構造化データをロードして操作する強力な方法が得られます。
