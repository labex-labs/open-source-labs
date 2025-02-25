# Copy-On-Write の有効化

まず、pandas で CoW を有効にしましょう。これは、pandas の `copy_on_write` コンフィグレーション オプションを使用して行うことができます。以下に、グローバルに CoW を有効にする 2 つの方法を示します。

```python
# pandas と numpy ライブラリをインポート
import pandas as pd

# set_option を使用して CoW を有効にする
pd.set_option("mode.copy_on_write", True)

# または直接代入を使用する
pd.options.mode.copy_on_write = True
```
