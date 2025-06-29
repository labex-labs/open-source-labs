# 継承の代替手段としての委譲

オブジェクト指向プログラミングにおいて、コードの再利用と拡張は一般的なタスクです。これを達成する主な方法は 2 つあります。継承と委譲です。

**継承** は、サブクラスが親クラスからメソッドと属性を継承するメカニズムです。サブクラスは、これらの継承されたメソッドの一部をオーバーライドして、独自の実装を提供することができます。

一方、**委譲** は、あるオブジェクトが別のオブジェクトを含み、特定のメソッド呼び出しをそのオブジェクトに転送することを伴います。

このステップでは、継承の代替手段として委譲を探索します。あるクラスの振る舞いの一部を別のオブジェクトに委譲するクラスを実装します。

## 委譲の例をセットアップする

まず、委譲するクラスが相互作用するベースクラスをセットアップする必要があります。

1. `/home/labex/project` ディレクトリに `base_class.py` という名前の新しいファイルを作成します。このファイルは、`method_a`、`method_b`、`method_c` の 3 つのメソッドを持つ `Spam` という名前のクラスを定義します。各メソッドはメッセージを印刷し、結果を返します。`base_class.py` に入れるコードは次のとおりです。

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

次に、委譲するクラスを作成します。

2. `delegator.py` という名前の新しいファイルを作成します。このファイルでは、`Spam` クラスのインスタンスに振る舞いの一部を委譲する `DelegatingSpam` という名前のクラスを定義します。

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

`__init__` メソッドでは、`Spam` クラスのインスタンスを作成します。`method_a` メソッドは元のメソッドをオーバーライドしますが、`Spam` クラスの `method_a` も呼び出します。`method_c` メソッドは元のメソッドを完全にオーバーライドします。`__getattr__` メソッドは、`DelegatingSpam` クラスに存在しない属性またはメソッドにアクセスしたときに呼び出される Python の特殊メソッドです。その後、呼び出しを `Spam` インスタンスに委譲します。

では、実装を検証するためのテストファイルを作成しましょう。

3. `test_delegation.py` という名前のテストファイルを作成します。このファイルは、`DelegatingSpam` クラスのインスタンスを作成し、そのメソッドを呼び出します。

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

最後に、テストスクリプトを実行します。

4. ターミナルで次のコマンドを使用してテストスクリプトを実行します。

```bash
cd /home/labex/project
python3 test_delegation.py
```

次のような出力が表示されるはずです。

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## 委譲と継承の比較

では、委譲と従来の継承を比較してみましょう。

1. `inheritance_example.py` という名前のファイルを作成します。このファイルでは、`Spam` クラスを継承する `InheritingSpam` という名前のクラスを定義します。

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

`InheritingSpam` クラスは `method_a` と `method_c` メソッドをオーバーライドします。`method_a` メソッドでは、`super()` を使用して親クラスの `method_a` を呼び出します。

次に、継承の例のテストファイルを作成します。

2. `test_inheritance.py` という名前のテストファイルを作成します。このファイルは、`InheritingSpam` クラスのインスタンスを作成し、そのメソッドを呼び出します。

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

最後に、継承のテストを実行します。

3. ターミナルで次のコマンドを使用して継承のテストを実行します。

```bash
cd /home/labex/project
python3 test_inheritance.py
```

次のような出力が表示されるはずです。

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## 主な違いと考慮事項

委譲と継承の類似点と相違点を見てみましょう。

1. **メソッドのオーバーライド**: 委譲と継承の両方でメソッドをオーバーライドできますが、構文は異なります。
   - 委譲では、独自のメソッドを定義し、ラップされたオブジェクトのメソッドを呼び出すかどうかを決定します。
   - 継承では、独自のメソッドを定義し、`super()` を使用して親のメソッドを呼び出します。

2. **メソッドのアクセス**:
   - 委譲では、未定義のメソッドは `__getattr__` メソッドを介して転送されます。
   - 継承では、未定義のメソッドは自動的に継承されます。

3. **型の関係**:
   - 委譲では、`isinstance(delegating_spam, Spam)` は `False` を返します。なぜなら、`DelegatingSpam` オブジェクトは `Spam` クラスのインスタンスではないからです。
   - 継承では、`isinstance(inheriting_spam, Spam)` は `True` を返します。なぜなら、`InheritingSpam` クラスは `Spam` クラスを継承しているからです。

4. **制限事項**: `__getattr__` による委譲は、`__getitem__`、`__len__` などの特殊メソッドでは機能しません。これらのメソッドは、委譲するクラスで明示的に定義する必要があります。

委譲は、次のような状況で特に有用です。

- オブジェクトの階層に影響を与えずに、オブジェクトの振る舞いをカスタマイズしたい場合。
- 共通の親を持たない複数のオブジェクトの振る舞いを組み合わせたい場合。
- 継承よりも柔軟性が必要な場合。

継承は、次の場合に一般的に好まれます。

- 「is-a」の関係が明確な場合（例えば、自動車は車両である）。
- コード全体で型の互換性を維持する必要がある場合。
- 特殊メソッドを継承する必要がある場合。
