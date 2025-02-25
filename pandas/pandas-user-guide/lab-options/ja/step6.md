# 起動時のオプション設定

Python/IPython環境で起動スクリプトを作成して、pandasをインポートしてオプションを設定することができます。これにより、pandasの作業が効率的になります。

```python
# This is an example of a startup script
# Place this in a.py file in the startup directory of IPython profile
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
