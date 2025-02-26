# 準備

この演習では、ライブラリモジュールのより厄介な詳細について扱います。非常に単純なライブラリモジュールを作成することでこの演習を始めましょう。

```python
# simplemod.py

x = 42        # グローバル変数

# 単純な関数
def foo():
    print('x is', x)

# 単純なクラス
class Spam:
    def yow(self):
        print('Yow!')

# スクリプト文
print('Loaded simplemod')
```
