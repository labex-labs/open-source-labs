# Пишение тестов

Теперь, когда вы настроили тестовую среду, вы можете начать писать тесты для вашего приложения Flask. Вот некоторые примеры общих тестов, которые вы, возможно, захотите написать:

1. Тестирование маршрута:

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   Этот тест отправляет GET-запрос на корневой маршрут ("/") и проверяет, что код статуса ответа равен 200 и в данных ответа содержится строка "Hello, World!".

2. Тестирование POST-запроса:

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   Этот тест отправляет POST-запрос на маршрут входа ("/login") с данными формы, содержащими имя пользователя и пароль. Он проверяет, что код статуса ответа равен 200 и в данных ответа содержится строка "Logged in successfully".

3. Тестирование команды:

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   Этот тест вызывает команду с именем "hello" и проверяет, что команда завершается с кодом 0 и в выводе содержится строка "Hello, World!".
