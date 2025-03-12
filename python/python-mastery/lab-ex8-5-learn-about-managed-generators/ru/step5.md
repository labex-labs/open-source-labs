# Реализация эхо-сервера

Теперь мы добавим реализацию эхо-сервера в наш файл `server.py`. Эхо-сервер - это тип сервера, который просто отправляет обратно любые данные, которые он получает от клиента. Это отличный способ понять, как серверы обрабатывают входящие данные и общаются с клиентами.

Добавьте следующий код в конец файла `server.py`. Этот код настроит наш эхо-сервер и обработает клиентские подключения.

```python
# TCP Server implementation
def tcp_server(address, handler):
    # Create a TCP socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Set the socket option to reuse the address
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Bind the socket to the given address
    sock.bind(address)
    # Start listening for incoming connections, with a backlog of 5
    sock.listen(5)

    while True:
        # Yield to pause the function until a client connects
        yield 'recv', sock        # Wait for a client connection
        # Accept a client connection
        client, addr = sock.accept()
        # Add a new handler task for this client to the tasks list
        tasks.append(handler(client, addr))  # Start a handler task for this client

# Echo handler - echoes back whatever the client sends
def echo_handler(client, address):
    print('Connection from', address)

    while True:
        # Yield to pause the function until the client sends data
        yield 'recv', client      # Wait until client sends data
        # Receive up to 1000 bytes of data from the client
        data = client.recv(1000)

        if not data:              # Client closed connection
            break

        # Yield to pause the function until the client can receive data
        yield 'send', client      # Wait until client can receive data
        # Send the data back to the client with 'GOT:' prefix
        client.send(b'GOT:' + data)

    print('Connection closed')
    # Close the client connection
    client.close()

# Start the server
if __name__ == '__main__':
    # Add the tcp_server task to the tasks list
    tasks.append(tcp_server(('', 25000), echo_handler))
    # Start the scheduler
    run()
```

Поймем этот код пошагово:

1. Функция `tcp_server`:

   - Сначала она настраивает сокет для прослушивания входящих подключений. Сокет - это конечная точка для связи между двумя машинами.
   - Затем она использует `yield 'recv', sock`, чтобы приостановить функцию до подключения клиента. Это ключевой элемент нашего асинхронного подхода.
   - Наконец, она создает новую задачу-обработчик для каждого клиентского подключения. Это позволяет серверу обрабатывать несколько клиентов одновременно.

2. Функция `echo_handler`:

   - Она возвращает `'recv', client`, чтобы ждать, пока клиент отправит данные. Это приостанавливает функцию до появления данных.
   - Она возвращает `'send', client`, чтобы ждать, пока можно будет отправить данные обратно клиенту. Это гарантирует, что клиент готов принять данные.
   - Она обрабатывает данные клиента до тех пор, пока клиент не закроет соединение.

3. Когда мы запускаем сервер, он добавляет задачу `tcp_server` в очередь и запускает планировщик. Планировщик отвечает за управление всеми задачами и гарантирует, что они выполняются асинхронно.

Чтобы протестировать сервер, запустите его в одном терминале:

```bash
python3 /home/labex/project/server.py
```

Вы должны увидеть сообщение, указывающее, что сервер запущен. Это означает, что сервер теперь прослушивает входящие подключения.

Откройте другой терминал и подключитесь к серверу с помощью `nc` (netcat). Netcat - это простая утилита, которая позволяет подключиться к серверу и отправлять данные.

```bash
nc localhost 25000
```

Теперь вы можете вводить сообщения и видеть их возвращаться с префиксом "GOT:":

```
Hello
GOT:Hello
World
GOT:World
```

Если `nc` не установлен, вы можете использовать встроенную библиотеку Python `telnetlib`. Telnetlib - это библиотека, которая позволяет подключиться к серверу с использованием протокола Telnet.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

Вы можете открыть несколько окон терминала и подключить несколько клиентов одновременно. Сервер будет обрабатывать все подключения одновременно, несмотря на то, что он однопоточный. Это благодаря нашему планировщику задач на основе генераторов, который позволяет серверу приостанавливать и возобновлять задачи по мере необходимости.

## Как это работает

В этом примере показано мощное применение генераторов для асинхронного ввода-вывода:

1. Сервер возвращает управление, когда он бы иначе блокировался, ожидая ввода-вывода. Это означает, что вместо бесконечного ожидания данных сервер может приостановиться и дать возможность другим задачам выполняться.
2. Планировщик перемещает его в область ожидания до готовности ввода-вывода. Это гарантирует, что сервер не тратит ресурсы на ожидание ввода-вывода.
3. Другие задачи могут выполняться, пока ожидается завершение ввода-вывода. Это позволяет серверу обрабатывать несколько задач одновременно.
4. Когда ввод-вывод готов, задача продолжает выполнение с того места, где она была приостановлена. Это ключевая особенность асинхронного программирования.

Этот шаблон составляет основу современных асинхронных фреймворков Python, таких как `asyncio`, который был добавлен в стандартную библиотеку Python в версии 3.4.
