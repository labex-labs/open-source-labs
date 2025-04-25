# 関数から複数の値を返す

Python では、関数から複数の値を返す必要がある場合、便利な解決策があります。それはタプル (tuple) を返すことです。タプルは Python のデータ構造の一種で、不変のシーケンスです。つまり、タプルを作成すると、その要素を変更することはできません。タプルは、異なる型の複数の値を一つの場所にまとめることができるため便利です。

`name=value` 形式の設定行を解析する関数を作成してみましょう。この関数の目的は、この形式の行を受け取り、名前と値を別々の要素として返すことです。

1. まず、新しい Python ファイルを作成する必要があります。このファイルには、関数のコードとテストコードを記述します。プロジェクトディレクトリ内に `return_values.py` という名前のファイルを作成します。ターミナルで以下のコマンドを使用してこのファイルを作成できます。

```
touch ~/project/return_values.py
```

2. 次に、コードエディタで `return_values.py` ファイルを開きます。このファイル内に `parse_line` 関数を記述します。この関数は、行を入力として受け取り、最初の '=' 記号で分割し、名前と値をタプルとして返します。

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

この関数では、`split` メソッドを使用して、入力行を最初の '=' 記号で 2 つの部分に分割します。行が正しい `name=value` 形式であれば、名前と値を抽出し、タプルとして返します。

3. 関数を定義した後、関数が期待通りに動作するかどうかを確認するためのテストコードを追加する必要があります。テストコードは、サンプル入力で `parse_line` 関数を呼び出し、結果を出力します。

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

テストコードでは、まず `parse_line` 関数を呼び出し、返されたタプルを `result` 変数に格納します。そして、このタプルを出力します。次に、タプルのアンパッキングを使用して、タプルの要素を直接 `name` と `value` 変数に割り当て、それぞれを出力します。

4. 関数とテストコードを記述したら、`return_values.py` ファイルを保存します。その後、ターミナルを開き、以下のコマンドを実行して Python スクリプトを実行します。

```
python ~/project/return_values.py
```

以下のような出力が表示されるはずです。

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**解説：**

- `parse_line` 関数は、`split` メソッドを使用して入力文字列を '=' 文字で分割します。このメソッドは、指定された区切り文字に基づいて文字列を部分に分割します。
- `return (name, value)` という構文を使用して、両方の部分をタプルとして返します。タプルは、複数の値をまとめる方法です。
- 関数を呼び出すときには、2 つのオプションがあります。`result` 変数のように、タプル全体を 1 つの変数に格納することもできます。また、`name, value = parse_line(...)` という構文を使用して、タプルを直接別々の変数に「アンパッキング」することもできます。これにより、個々の値を扱いやすくなります。

複数の値をタプルとして返すこのパターンは、Python で非常に一般的です。これにより、関数は呼び出し元のコードに複数の情報を提供できるため、より汎用的になります。
