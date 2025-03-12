# クラスメソッドにデコレータを適用する

ここでは、デコレータがクラスメソッドとどのように相互作用するかを探っていきます。Python にはインスタンスメソッド、クラスメソッド、静的メソッド、プロパティといった異なる種類のメソッドがあるため、これは少しトリッキーな場合があります。デコレータは、別の関数を受け取り、その関数の振る舞いを明示的に変更することなく拡張する関数です。クラスメソッドにデコレータを適用する際には、これらの異なるメソッドタイプとの相互作用に注意する必要があります。

## チャレンジの理解

`@logged` デコレータを異なるタイプのメソッドに適用したときに何が起こるかを見てみましょう。`@logged` デコレータは、メソッド呼び出しに関する情報をログに記録するために使用される可能性があります。

1. WebIDE で新しいファイル `methods.py` を作成します。このファイルには、`@logged` デコレータで装飾された異なるタイプのメソッドを持つクラスが含まれます。

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

このコードでは、4 種類の異なるメソッドを持つ `Spam` クラスがあります。各メソッドは `@logged` デコレータで装飾されており、一部は `@classmethod`、`@staticmethod`、`@property` などの他の組み込みデコレータでも装飾されています。

2. 動作をテストしてみましょう。ターミナルで Python コマンドを実行して、これらのメソッドを呼び出し、出力を確認します。

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

このコマンドを実行すると、いくつかの問題に気づくかもしれません。

- `@property` デコレータは、`@logged` デコレータと正しく動作しない可能性があります。`@property` デコレータはメソッドをプロパティとして定義するために使用され、特定の動作方法があります。`@logged` デコレータと組み合わせると、競合が発生する可能性があります。
- `@classmethod` と `@staticmethod` の場合、デコレータの適用順序が重要です。デコレータの適用順序によって、メソッドの振る舞いが変わることがあります。

## デコレータの適用順序

複数のデコレータを適用する場合、下から上に適用されます。つまり、メソッド定義に最も近いデコレータが最初に適用され、その後、上にあるデコレータが順番に適用されます。例えば：

```python
@decorator1
@decorator2
def func():
    pass
```

これは次と等価です。

```python
func = decorator1(decorator2(func))
```

この例では、`decorator2` が `func` に最初に適用され、次に `decorator1` が `decorator2(func)` の結果に適用されます。

## デコレータの順序を修正する

`methods.py` ファイルを更新して、デコレータの順序を修正しましょう。デコレータの順序を変更することで、各メソッドが期待通りに動作するようにできます。

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

この更新版では：

- `instance_method` の場合、順序は関係ありません。インスタンスメソッドはクラスのインスタンスで呼び出され、`@logged` デコレータは基本的な機能に影響を与えることなく任意の順序で適用できます。
- `class_method` の場合、`@logged` の後に `@classmethod` を適用します。`@classmethod` デコレータはメソッドの呼び出し方法を変更し、`@logged` の後に適用することで、ログ記録が正しく機能することが保証されます。
- `static_method` の場合、`@logged` の後に `@staticmethod` を適用します。`@classmethod` と同様に、`@staticmethod` デコレータには独自の振る舞いがあり、`@logged` デコレータとの順序が正しくなければなりません。
- `property_method` の場合、`@logged` の後に `@property` を適用します。これにより、プロパティの振る舞いが維持されると同時に、ログ記録機能も得られます。

3. 更新したコードをテストしてみましょう。前と同じコマンドを実行して、問題が解決したかどうかを確認します。

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

これで、すべてのメソッドタイプに対して適切なログ記録が行われるはずです。

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## メソッドデコレータのベストプラクティス

メソッドデコレータを使用する際には、次のベストプラクティスに従ってください。

1. メソッドを変換するデコレータ（`@classmethod`、`@staticmethod`、`@property`）は、カスタムデコレータの**後**に適用します。これにより、カスタムデコレータがログ記録やその他の操作を最初に実行でき、その後、組み込みデコレータがメソッドを意図した通りに変換できます。
2. デコレータの実行は、メソッド呼び出し時ではなく、クラス定義時に行われることに注意してください。これは、デコレータ内のセットアップまたは初期化コードが、メソッドが呼び出されるのではなく、クラスが定義されたときに実行されることを意味します。
3. より複雑なケースでは、異なるメソッドタイプに対して専用のデコレータを作成する必要があるかもしれません。異なるメソッドタイプには異なる振る舞いがあり、ワンサイズフィットオールのデコレータはすべての状況で機能するとは限りません。
