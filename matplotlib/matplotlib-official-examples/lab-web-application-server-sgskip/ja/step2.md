# 依存関係のインポート

このステップでは、必要な依存関係をインポートします。画像データをエンコードするために `base64` を、画像データをメモリに保存するために `BytesIO` を、Web アプリケーションサーバーを作成するために `Flask` を、グラフを作成するために `Figure` を使用します。

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
