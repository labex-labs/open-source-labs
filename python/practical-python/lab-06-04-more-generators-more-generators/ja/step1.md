# ジェネレータ式

リスト内包表記のジェネレータ版です。

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

リスト内包表記との違い

- リストを構築しません。
- 唯一の有用な目的は反復処理です。
- 一度消費すると、再利用できません。

一般的な構文

```python
(<式> for i in s if <条件>)
```

関数の引数としても使用できます。

```python
sum(x*x for x in a)
```

任意の反復可能オブジェクトに適用できます。

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

ジェネレータ式の主な用途は、シーケンスに対して何らかの計算を行い、結果を一度だけ使用するコードにあります。たとえば、ファイルからすべてのコメントを取り除きます。

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
  ...
f.close()
```

ジェネレータを使用すると、コードが高速に実行され、メモリを少なく使用します。ストリームに適用されるフィルタのようなものです。
