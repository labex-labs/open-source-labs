# 设置字体路径

我们通过使用`mpl.get_data_path()`方法来获取数据目录的路径，从而设置字体路径，然后使用`pathlib`模块中的`Path()`方法将字体文件`cmr10.ttf`的路径追加到该路径上。

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```
