# 编写测试

既然你已经设置好了测试环境，就可以开始为你的 Flask 应用程序编写测试了。以下是一些你可能想要编写的常见测试示例：

1. 测试一个路由：

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   此测试向根路由（“/”）发送一个 GET 请求，并检查响应状态码是否为 200，以及响应数据中是否包含字符串“Hello, World!”。

2. 测试一个 POST 请求：

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   此测试向登录路由（“/login”）发送一个包含用户名和密码的表单数据的 POST 请求。它检查响应状态码是否为 200，以及响应数据中是否包含字符串“Logged in successfully”。

3. 测试一个命令：

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   此测试调用一个名为“hello”的命令，并检查该命令是否以代码 0 退出，以及输出中是否包含字符串“Hello, World!”。
