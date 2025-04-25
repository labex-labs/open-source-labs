# 出力

`print` 関数は、渡された値とともに 1 行の文字列を生成します。

```python
print('Hello world!') # 文字列'Hello world!' を出力します
```

変数を使用することができます。出力される文字列は、変数の値であり、名前ではありません。

```python
x = 100
print(x) # 文字列'100' を出力します
```

`print` に複数の値を渡す場合、それらはスペースで区切られます。

```python
name = 'Jake'
print('My name is', name) # 文字列'My name is Jake' を出力します
```

`print()` は常に末尾に改行を挿入します。

```python
print('Hello')
print('My name is', 'Jake')
```

これは以下のように出力されます。

```code
Hello
My name is Jake
```

余分な改行を抑制することができます。

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

このコードは以下のように出力されます。

```code
Hello My name is Jake
```
