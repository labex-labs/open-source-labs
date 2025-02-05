# 添加动态内容

Flask 允许我们将动态内容传递到模板中。让我们修改路由以传递一个名字参数并显示个性化问候语。

1. 修改你的 `app.py` 文件，以便在路由中接受一个名字参数：

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. 打开 `index.html` 文件并修改 `<h1>` 标签以显示个性化问候语：

   ```html
   <h1>你好，{{ name }}！</h1>
   ```
