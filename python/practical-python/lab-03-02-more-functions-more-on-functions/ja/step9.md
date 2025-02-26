# グローバル変数

関数は、同じファイル内で定義されたグローバル変数の値に自由にアクセスできます。

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # `name` グローバル変数を使用
```

ただし、関数はグローバル変数を変更できません。

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # 'Dave' と表示されます
```

**覚えておいてください: 関数内のすべての代入はローカルです。**
