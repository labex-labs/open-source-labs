# より複雑なパターンの扱い

現在の関数はキャメルケースに対しては機能しますが、以下のような追加のパターンを扱うように強化する必要があります。

1. パスカルケース（PascalCase）（例: `HelloWorld`）
2. ハイフンを含む文字列（例: `hello-world`）
3. すでにアンダースコアを含む文字列（例: `hello_world`）

これらのケースを扱うように関数を更新しましょう。

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

行った改良点は以下の通りです。

1. まず、ハイフンをすべて空白に置き換えます。
2. 新しい正規表現 `re.sub('([A-Z]+)', r' \1', s)` は、連続する大文字の前に空白を追加します。これはパスカルケースの処理に役立ちます。
3. キャメルケースを扱う正規表現はそのままにしています。
4. 最後に、文字列を空白で分割し、アンダースコアで結合し、小文字に変換します。これにより、残りの空白を処理し、出力を一貫性のあるものにします。

様々な入力形式でテストするために、スクリプトを実行しましょう。

```bash
python3 ~/project/snake_case.py
```

次のような出力が表示されるはずです。

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

私たちの関数は現在、より堅牢になり、様々な入力形式を扱うことができるようになりました。次のステップでは、最終的な改良を行い、完全なテストセットに対してテストを行います。
