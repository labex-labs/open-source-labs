# Jupyter Notebook の作成と必要なライブラリのインポート

Notebook の最初のセルに、必要なライブラリをインポートするための以下のコードを入力します。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

これらのライブラリそれぞれの機能を理解しましょう。

- `matplotlib.pyplot`（`plt` としてエイリアス付けされています）: matplotlib を MATLAB のように動作させる関数のコレクションで、グラフを作成するための便利なインターフェイスを提供します。
- `numpy`（`np` としてエイリアス付けされています）: Python での科学計算のための基本的なパッケージで、データ操作に使用します。
- `matplotlib.cbook`: matplotlib のユーティリティ関数のコレクションで、サンプルデータを取得する関数も含まれています。
- `matplotlib.image`: matplotlib の画像関連の機能を提供するモジュールで、画像の読み込みと表示に使用します。

Notebook の上部にある「Run」ボタンをクリックするか、Shift + Enter キーを押してセルを実行します。

![libraries-imported](../assets/screenshot-20250306-18gJ6FRZ@2x.png)

このセルの実行は何も出力せずに完了するはずで、これはすべてのライブラリが正常にインポートされたことを示します。
