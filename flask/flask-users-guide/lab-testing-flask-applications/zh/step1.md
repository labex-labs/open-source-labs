# 设置测试环境

在开始为 Flask 应用程序编写测试之前，你需要设置测试环境。以下是设置步骤：

1. 通过运行以下命令安装 `pytest` 框架：

   ```bash
   pip install pytest
   ```

2. 在 Flask 应用程序的 `tests` 文件夹中创建一个名为 `conftest.py` 的新文件。

3. 在 `conftest.py` 文件中，导入必要的模块：

   ```python
   import pytest
   from my_app import create_app
   ```

4. 定义一个名为 `app` 的 fixture，用于创建和配置应用程序实例：

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   注意，如果你使用的是应用程序工厂模式，应相应地修改 fixture。

5. 为测试客户端和 CLI 运行器定义 fixture：

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
