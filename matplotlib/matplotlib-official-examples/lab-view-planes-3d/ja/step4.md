# 3D プロットのレイアウトを定義する

3D プロットのレイアウトをリストのリストを使って定義します。リスト内の `'.'` は空のサブプロットを表します。

```python
layout = [['XY',  '.',   'L',   '.'],
          ['XZ', 'YZ', '-XZ', '-YZ'],
          ['.',   '.', '-XY',   '.']]
```
