# 行変換機能の追加

プログラミングでは、特に CSV ファイルのようなソースからのデータを扱う場合、データ行からクラスのインスタンスを作成することがよくあります。このセクションでは、`Structure` クラスのインスタンスをデータ行から作成する機能を追加します。`Structure` クラスに `from_row` クラスメソッドを実装することでこれを行います。

1. まず、エディタで `structure.py` ファイルを開きます。ここでコードの変更を行います。

2. 次に、`validate_attributes` 関数を変更します。この関数は、`Validator` インスタンスを抽出し、`_fields` および `_types` リストを自動的に構築するクラスデコレータです。型情報も収集するように更新します。

```python
def validate_attributes(cls):
    """
    Validator インスタンスを抽出し、_fields および_types リストを自動的に構築する
    クラスデコレータ
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # バリデータ名に基づいて _fields を設定します
    cls._fields = [val.name for val in validators]

    # バリデータの expected_types に基づいて _types を設定します
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # 初期化メソッドを作成します
    cls.create_init()

    return cls
```

この更新された関数では、各バリデータから `expected_type` 属性を収集し、`_types` クラス変数に格納しています。これは、後で行からデータを正しい型に変換する際に役立ちます。

3. 次に、`Structure` クラスに `from_row` クラスメソッドを追加します。このメソッドにより、リストまたはタプルのいずれかであるデータ行からクラスのインスタンスを作成できます。

```python
@classmethod
def from_row(cls, row):
    """
    データ行（リストまたはタプル）からインスタンスを作成します
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

このメソッドの仕組みは次のとおりです。

- リストまたはタプルの形式のデータ行を受け取ります。
- `_types` リストの対応する関数を使用して、行の各値を期待される型に変換します。
- 次に、変換された値を使用してクラスの新しいインスタンスを作成して返します。

4. これらの変更を行った後、`structure.py` ファイルを保存します。これにより、コードの変更が保持されます。

5. `from_row` メソッドが期待どおりに機能することを確認するためにテストしましょう。`Stock` クラスを使用して簡単なテストを作成します。ターミナルで次のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

次のような出力が表示されるはずです。

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

文字列値 '100' と '490.1' が自動的に正しい型（整数と浮動小数点数）に変換されたことに注意してください。これは、`from_row` メソッドが正しく機能していることを示しています。

6. 最後に、`reader.py` モジュールを使用して CSV ファイルからデータを読み込んでみましょう。ターミナルで次のコマンドを実行します。

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

CSV ファイルから株が表示される出力が表示されるはずです。

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 82391.5
```

`from_row` メソッドを使用すると、CSV データを `Stock` クラスのインスタンスに簡単に変換できます。`read_csv_as_instances` 関数と組み合わせると、構造化データをロードして操作するための強力な方法が得られます。
