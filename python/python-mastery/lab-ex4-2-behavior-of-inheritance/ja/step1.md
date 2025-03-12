# 単一継承と多重継承の理解

このステップでは、Pythonにおける2つの主要な継承の種類、単一継承と多重継承について学びます。継承はオブジェクト指向プログラミングにおける基本的な概念で、クラスが他のクラスから属性とメソッドを継承することを可能にします。また、複数の候補がある場合にPythonがどのメソッドを呼び出すかを決定する方法、つまりメソッド解決（method resolution）についても見ていきます。

## 単一継承

単一継承とは、クラスが単一の祖先の列を形成する場合です。各クラスが1つの直接の親を持つ家族の木のようなものだと考えてください。それがどのように機能するかを理解するために、例を作成しましょう。

まず、WebIDEで新しいターミナルを開きます。ターミナルが開いたら、以下のコマンドを入力してEnterキーを押すことでPythonインタープリタを起動します。

```bash
python3
```

Pythonインタープリタに入ったら、単一の継承チェーンを形成する3つのクラスを作成します。以下のコードを入力してください。

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

このコードでは、クラス`B`はクラス`A`から継承し、クラス`C`はクラス`B`から継承しています。`super()`関数は親クラスのメソッドを呼び出すために使用されています。

これらのクラスを定義した後、Pythonがメソッドを検索する順序を調べることができます。この順序はメソッド解決順序（Method Resolution Order, MRO）と呼ばれます。クラス`C`のMROを見るには、以下のコードを入力します。

```python
C.__mro__
```

以下のような出力が表示されるはずです。

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

この出力は、Pythonがまずクラス`C`、次にクラス`B`、次にクラス`A`、最後に基底の`object`クラスでメソッドを検索することを示しています。

では、クラス`C`のインスタンスを作成し、その`spam()`メソッドを呼び出しましょう。以下のコードを入力します。

```python
c = C()
c.spam()
```

以下のような出力が表示されるはずです。

```
C.spam
B.spam
A.spam
```

この出力は、単一の継承チェーンにおいて`super()`がどのように機能するかを示しています。`C.spam()`が`super().spam()`を呼び出すと、`B.spam()`が呼び出されます。次に、`B.spam()`が`super().spam()`を呼び出すと、`A.spam()`が呼び出されます。

## 多重継承

多重継承は、クラスが複数の親クラスから継承することを可能にします。これにより、クラスはすべての親クラスの属性とメソッドにアクセスすることができます。この場合のメソッド解決がどのように機能するかを見てみましょう。

Pythonインタープリタに以下のコードを入力します。

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

次に、複数の親クラス`X`、`Y`、`Z`から継承するクラス`M`を作成します。以下のコードを入力します。

```python
class M(X, Y, Z):
    pass

M.__mro__
```

以下のような出力が表示されるはずです。

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

この出力は、クラス`M`のメソッド解決順序を示しています。Pythonはこの順序でメソッドを検索します。

クラス`M`のインスタンスを作成し、その`spam()`メソッドを呼び出しましょう。

```python
m = M()
m.spam()
```

以下のような出力が表示されるはずです。

```
X.spam
Y.spam
Z.spam
Base.spam
```

`super()`は直近の親クラスのメソッドを呼び出すだけではなく、子クラスによって定義されたメソッド解決順序（MRO）に従うことに注意してください。

親クラスの順序が異なる別のクラス`N`を作成しましょう。

```python
class N(Z, Y, X):
    pass

N.__mro__
```

以下のような出力が表示されるはずです。

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

では、クラス`N`のインスタンスを作成し、その`spam()`メソッドを呼び出しましょう。

```python
n = N()
n.spam()
```

以下のような出力が表示されるはずです。

```
Z.spam
Y.spam
X.spam
Base.spam
```

これは重要な概念を示しています。Pythonの多重継承では、クラス定義における親クラスの順序がメソッド解決順序を決定します。`super()`関数は、どのクラスから呼び出された場合でもこの順序に従います。

これらの概念を探索し終えたら、以下のコードを入力してPythonインタープリタを終了することができます。

```python
exit()
```
