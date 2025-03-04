# Запустить Docker-образ

Теперь, когда вы собрали образ, вы можете запустить его, чтобы убедиться, что он работает.

Запустите Docker-образ

```bash
docker run -p 5001:5000 -d python-hello-world
```

Флаг `-p` отображает порт, работающий внутри контейнера, на ваш хост. В этом случае мы отображаем приложение на Python, работающее на порту 5000 внутри контейнера, на порт 5001 на вашем хосте. Обратите внимание, что если порт 5001 уже занят другой программой на вашем хосте, вы можете придется заменить 5001 на другое значение, например, 5002.

Перейдите на вкладку **PORTS** в окне терминала и нажмите на ссылку, чтобы открыть приложение в новой вкладке браузера.

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

В терминале выполните `curl localhost:5001`, который возвращает `hello world!`.

Проверьте вывод журнала контейнера.

Если вы хотите увидеть логи из вашего приложения, вы можете использовать команду `docker container logs`. По умолчанию `docker container logs` выводит то, что отправляется в стандартный вывод вашим приложением. Используйте `docker container ls`, чтобы найти идентификатор для вашего запущенного контейнера.

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

Dockerfile - это то, как вы создаете воспроизводимые сборки для вашего приложения. Общий рабочий процесс заключается в том, чтобы ваша автоматизация CI/CD выполняла `docker image build` в качестве части своего процесса сборки. Как только образовы будут собраны, они будут отправлены в центральный реестр, откуда их могут получить все среда (например, тестовая среда), которые нуждаются в запуске экземпляров этого приложения. В следующем шаге мы отправим наш собственный образ в публичный Docker-реестр: Docker Hub, где его могут использовать другие разработчики и операторы.
