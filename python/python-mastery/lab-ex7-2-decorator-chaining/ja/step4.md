# 検証（再訪）

前回のエクササイズでは、型アノテーションを強制する `@validated` デコレータを書きました。たとえば：

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

代わりに、デコレータにキーワード引数で指定された型を強制する新しいデコレータ `@enforce()` を作成します。たとえば：

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

デコレートされた関数の結果としての動作は同じでなければなりません。注：`return_` キーワードで戻り値の型を指定します。`return` はPythonの予約語なので、少し異なる名前を選ぶ必要があります。

**考察**

堅牢なデコレータを書くことは、見た目よりもはるかに難しいことが多いです。推奨読書：
