# リスト操作

リストは任意の型の要素を保持できます。`append()` を使用して新しい要素を追加します。

```python
names.append('Murphy')    # 末尾に追加
names.insert(2, 'Aretha') # 中央に挿入
```

`+` を使用してリストを連結します。

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

リストは整数でインデックス付けされます。0から始まります。

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

負のインデックスは末尾から数えます。

```python
names[-1] # 'Curtis'
```

リスト内の任意の要素を変更できます。

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

リストの長さ。

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

メンバーシップテスト (`in`, `not in`)。

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

複製 (`s * n`)。

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
