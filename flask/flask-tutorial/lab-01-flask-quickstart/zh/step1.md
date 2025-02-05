# 安装 Flask

要开始使用 Flask，你需要安装它并设置一个新项目。请按照以下说明操作：

1. 在终端或命令提示符中运行以下命令来安装 Flask：

   ```bash
   pip install flask
   ```

2. 打开一个新文件并将其保存为 `app.py`。

   ```bash
   cd ~/project
   touch app.py
   ```

3. 导入 Flask 模块并创建 Flask 类的实例：

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
