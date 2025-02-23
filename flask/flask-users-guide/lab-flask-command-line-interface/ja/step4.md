# カスタムコマンドの作成

Flask CLI を使うと、コマンドラインから実行できるカスタムコマンドを作成できます。引数として名前を受け取り、挨拶メッセージを表示する `greet` というカスタムコマンドを作成しましょう。

`commands.py` という名前の新しい Python ファイルを作成し、次のコードを追加します。

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

ファイルを保存し、次のコマンドを使って実行します。

```
python commands.py John
```

ターミナルに「Hello, John!」というメッセージが表示されるはずです。
