# カスタムディスクリプタの作成

このステップでは、独自のディスクリプタクラスを作成します。まず、ディスクリプタとは何かを理解しましょう。ディスクリプタは、`__get__`、`__set__`、`__delete__` メソッドから構成されるディスクリプタプロトコルを実装した Python オブジェクトです。これらのメソッドにより、ディスクリプタは属性のアクセス、設定、削除方法を管理できます。独自のディスクリプタクラスを作成することで、このプロトコルがどのように動作するかをより深く理解できます。

プロジェクトディレクトリに `descrip.py` という新しいファイルを作成します。このファイルにはカスタムディスクリプタクラスを記述します。以下がコードです。

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

`Descriptor` クラスでは、`__init__` メソッドがディスクリプタを名前で初期化します。`__get__` メソッドは属性がアクセスされたときに呼び出され、`__set__` メソッドは属性が設定されたときに呼び出され、`__delete__` メソッドは属性が削除されたときに呼び出されます。

次に、カスタムディスクリプタを試すためのテストファイルを作成しましょう。これにより、さまざまなシナリオでディスクリプタがどのように動作するかを確認できます。以下のコードを持つ `test_descrip.py` というファイルを作成します。

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

`test_descrip.py` ファイルでは、`descrip.py` から `Descriptor` クラスをインポートします。次に、3 つの属性 `a`、`b`、`c` を持つ `Foo` クラスを作成し、それぞれがディスクリプタによって管理されます。`Foo` のインスタンスを作成し、属性のアクセス、設定、削除などの操作を行い、ディスクリプタメソッドがどのように呼び出されるかを確認します。

では、このテストファイルを実行して、ディスクリプタの動作を確認しましょう。ターミナルを開き、プロジェクトディレクトリに移動し、以下のコマンドを使用してテストファイルを実行します。

```bash
cd ~/project
python3 test_descrip.py
```

以下のような出力が表示されるはずです。

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

ご覧のように、ディスクリプタによって管理される属性をアクセス、設定、または削除するたびに、対応するマジックメソッド (`__get__`、`__set__`、または `__delete__`) が呼び出されます。

また、ディスクリプタを対話的に調べてみましょう。これにより、ディスクリプタをリアルタイムでテストし、すぐに結果を確認できます。ターミナルを開き、プロジェクトディレクトリに移動し、`descrip.py` ファイルを使用して対話型 Python セッションを開始します。

```bash
cd ~/project
python3 -i descrip.py
```

次に、対話型 Python セッションで以下のコマンドを入力して、ディスクリプタプロトコルがどのように動作するかを確認します。

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

ここでの重要なポイントは、ディスクリプタが属性アクセスをインターセプトしてカスタマイズする方法を提供することです。これにより、データ検証、計算属性、その他の高度な動作の実装に強力な手段となります。ディスクリプタを使用することで、クラス属性のアクセス、設定、削除方法をより細かく制御できます。
