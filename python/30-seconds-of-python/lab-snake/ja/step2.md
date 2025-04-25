# 正規表現を使ったパターンマッチング

文字列をスネークケースに変換するために、正規表現（regular expressions, regex）を使って単語の境界を特定します。Python の `re` モジュールは、このタスクに利用できる強力なパターンマッチング機能を提供しています。

キャメルケースの文字列を扱うように関数を更新しましょう。

1. まず、小文字の後に大文字が続くパターン（「camelCase」のような）を特定する必要があります。
2. 次に、それらの間に空白を挿入します。
3. 最後に、すべてを小文字に変換し、空白をアンダースコアに置き換えます。

この改良版の関数で `snake_case.py` ファイルを更新します。

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

この関数が行っていることを分解してみましょう。

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` は、小文字 `([a-z])` の後に大文字 `([A-Z])` が続くパターンを探します。そして、このパターンを同じ文字に置き換えるが、キャプチャされたグループを参照する `\1` と `\2` を使ってそれらの間に空白を追加します。
- その後、`lower()` ですべてを小文字に変換し、空白をアンダースコアに置き換えます。

キャメルケースに対して機能するかどうかを確認するために、スクリプトを再度実行しましょう。

```bash
python3 ~/project/snake_case.py
```

出力は次のようになるはずです。

```
Original: helloWorld
Snake case: hello_world
```

素晴らしい！私たちの関数はキャメルケースの文字列を扱えるようになりました。次のステップでは、より複雑なケースを扱うように関数を強化します。
