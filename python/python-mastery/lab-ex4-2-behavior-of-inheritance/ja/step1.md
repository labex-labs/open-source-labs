# 継承の方向

Python には 2 種類の異なる「方向」の継承があります。最初のものは、「単一継承」の概念に見られ、一連のクラスが単一の親から継承する場合です。たとえば、この例を試してみてください。

```python
>>> class A:
        def spam(self):
            print('A.spam')

>>> class B(A):
        def spam(self):
            print('B.spam')
            super().spam()

>>> class C(B):
        def spam(self):
            print('C.spam')
            super().spam()


>>> C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
>>> c = C()
>>> c.spam()
C.spam
B.spam
A.spam
>>>
```

クラス `C` の `__mro__` 属性が、そのすべての祖先を順序付けてエンコードしていることに注意してください。`spam()` メソッドを呼び出すと、階層構造をクラスごとに MRO を辿っていきます。

多重継承では、異なるクラスを組み合わせることができる別の種類の継承が得られます。この例を試してみてください。

```python
>>> class Base:
        def spam(self):
            print('Base.spam')

>>> class X(Base):
        def spam(self):
            print('X.spam')
            super().spam()

>>> class Y(Base):
        def spam(self):
            print('Y.spam')
            super().spam()

>>> class Z(Base):
        def spam(self):
            print('Z.spam')
            super().spam()

>>>
```

上記のすべてのクラスが共通の親 `Base` から継承していることに注意してください。ただし、クラス `X`、`Y`、および `Z` は互いに直接関係していません（それらのクラスを結び付ける継承チェーンはありません）。

ただし、多重継承で何が起こるか見てみましょう。

```python
>>> class M(X,Y,Z):
        pass

>>> M.__mro__
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
>>> m = M()
>>> m.spam()
X.spam
Y.spam
Z.spam
Base.spam
>>>
```

ここでは、サブクラスによって提供される順序ですべてのクラスが積み重なっていることがわかります。サブクラスがクラスの順序を並べ替えるとしましょう。

```python
>>> class N(Z,Y,X):
        pass

>>> N.__mro__
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
>>> n = N()
>>> n.spam()
Z.spam
Y.spam
X.spam
Base.spam
>>>
```

ここでは、親の順序が逆になっていることがわかります。両方の場合で `super()` が何をしているかに注意深く注目してください。それは各クラスの直近の親に委譲するのではなく、代わりに MRO 上の次のクラスに移動します。それだけでなく、正確な順序は子クラスによって制御されます。これはかなり奇妙です。

また、共通の親 `Base` が `super()` 操作のチェーンを終了させることにも注意してください。具体的には、`Base.spam()` メソッドはさらにメソッドを呼び出しません。また、すべてのクラスが一緒に組み合わされている親であるため、MRO の末尾にも表示されます。
