# Настройка тестовой среды

Прежде чем начать писать тесты для вашего приложения Flask, вам нужно настроить тестовую среду. Вот шаги по выполнению этого:

1. Установите фреймворк `pytest`, выполнив следующую команду:

   ```bash
   pip install pytest
   ```

2. Создайте новый файл с именем `conftest.py` в папке `tests` вашего приложения Flask.

3. В файле `conftest.py` импортируйте необходимые модули:

   ```python
   import pytest
   from my_app import create_app
   ```

4. Определите фикстуру под названием `app`, которая создает и настраивает экземпляр приложения:

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   Обратите внимание, что если вы используете паттерн фабрики приложений, вы должны соответствующим образом изменить фикстуру.

5. Определите фикстуры для тестового клиента и запускатора CLI:

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
