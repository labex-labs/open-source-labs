# フォントパスを設定する

`mpl.get_data_path()` メソッドを使ってデータディレクトリのパスを取得し、そこに `pathlib` モジュールの `Path()` メソッドを使ってフォントファイル `cmr10.ttf` のパスを追加することで、フォントパスを設定します。

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```
