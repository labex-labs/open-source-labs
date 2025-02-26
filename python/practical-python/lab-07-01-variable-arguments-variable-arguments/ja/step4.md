# タプルと辞書の渡し方

タプルは可変長引数に展開できます。

```python
numbers = (2,3,4)
f(1, *numbers)      # f(1,2,3,4) と同じ
```

辞書もキーワード引数に展開できます。

```python
options = {
    'color' :'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# f(data, color='red', delimiter=',', width=400) と同じ
```
