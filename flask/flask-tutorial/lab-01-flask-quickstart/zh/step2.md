# 创建基本路由

Flask 中的路由定义了应用程序的 URL 模式。让我们创建一个显示“Hello, World!”消息的基本路由。

1. 将以下代码添加到你的 `app.py` 文件中：

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. 保存文件。
