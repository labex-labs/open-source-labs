# break 文

`break` 文を使うと、ループを早期に抜けることができます。

```python
for name in namelist:
    if name == 'Jake':
        break
  ...
  ...
statements
```

`break` 文が実行されると、ループを抜けて次の `statements` に進みます。`break` 文は最内側のループにのみ適用されます。このループが別のループ内にある場合、外側のループを抜けることはありません。
