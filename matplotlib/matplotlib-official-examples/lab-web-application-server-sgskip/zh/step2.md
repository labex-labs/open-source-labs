# 导入依赖项

在这一步中，我们将导入必要的依赖项。我们将使用`base64`对图像数据进行编码，使用`BytesIO`将图像数据存储在内存中，使用`Flask`创建 Web 应用服务器，并使用`Figure`创建图形。

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
