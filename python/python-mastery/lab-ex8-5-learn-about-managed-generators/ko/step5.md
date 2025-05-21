# 에코 서버 구현

이제 `server.py` 파일에 에코 서버의 구현을 추가해 보겠습니다. 에코 서버는 클라이언트로부터 수신한 모든 데이터를 그대로 다시 보내는 유형의 서버입니다. 이는 서버가 들어오는 데이터를 처리하고 클라이언트와 통신하는 방식을 이해하는 좋은 방법입니다.

`server.py` 파일의 끝에 다음 코드를 추가합니다. 이 코드는 에코 서버를 설정하고 클라이언트 연결을 처리합니다.

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

이 코드를 단계별로 이해해 보겠습니다.

1. `tcp_server` 함수:

   - 먼저 들어오는 연결을 수신 대기하기 위해 소켓을 설정합니다. 소켓은 두 머신 간의 통신을 위한 엔드포인트입니다.
   - 그런 다음 `yield 'recv', sock`을 사용하여 클라이언트가 연결될 때까지 함수를 일시 중지합니다. 이는 비동기적 접근 방식의 핵심 부분입니다.
   - 마지막으로 각 클라이언트 연결에 대해 새로운 핸들러 작업을 생성합니다. 이를 통해 서버는 여러 클라이언트를 동시에 처리할 수 있습니다.

2. `echo_handler` 함수:

   - 클라이언트가 데이터를 보낼 때까지 대기하기 위해 `'recv', client`를 yield 합니다. 이는 데이터가 사용 가능할 때까지 함수를 일시 중지합니다.
   - 클라이언트에게 데이터를 다시 보낼 수 있을 때까지 대기하기 위해 `'send', client`를 yield 합니다. 이는 클라이언트가 데이터를 수신할 준비가 되었는지 확인합니다.
   - 연결이 클라이언트에 의해 닫힐 때까지 클라이언트 데이터를 처리합니다.

3. 서버를 실행하면 `tcp_server` 작업을 큐에 추가하고 스케줄러를 시작합니다. 스케줄러는 모든 작업을 관리하고 비동기적으로 실행되도록 하는 역할을 합니다.

서버를 테스트하려면 한 터미널에서 실행합니다.

```bash
python3 /home/labex/project/server.py
```

서버가 실행 중임을 나타내는 메시지가 표시됩니다. 이는 서버가 이제 들어오는 연결을 수신 대기하고 있음을 의미합니다.

다른 터미널을 열고 `nc` (netcat) 를 사용하여 서버에 연결합니다. Netcat 은 서버에 연결하여 데이터를 보낼 수 있는 간단한 유틸리티입니다.

```bash
nc localhost 25000
```

이제 메시지를 입력하면 "GOT:" 접두사가 붙어 에코되는 것을 볼 수 있습니다.

```
Hello
GOT:Hello
World
GOT:World
```

`nc`가 설치되어 있지 않은 경우 Python 의 내장 `telnetlib`를 사용할 수 있습니다. Telnetlib 는 Telnet 프로토콜을 사용하여 서버에 연결할 수 있는 라이브러리입니다.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

여러 터미널 창을 열고 여러 클라이언트를 동시에 연결할 수 있습니다. 서버는 단일 스레드임에도 불구하고 모든 연결을 동시에 처리합니다. 이는 제너레이터 기반 작업 스케줄러 덕분이며, 필요에 따라 서버가 작업을 일시 중지하고 재개할 수 있습니다.

## 작동 방식

이 예제는 비동기 I/O 를 위한 제너레이터의 강력한 응용 프로그램을 보여줍니다.

1. 서버는 I/O 를 기다리는 동안 블로킹될 때 yield 합니다. 즉, 데이터를 무한정 기다리는 대신 서버는 일시 중지하고 다른 작업이 실행되도록 할 수 있습니다.
2. 스케줄러는 I/O 가 준비될 때까지 이를 대기 영역으로 이동합니다. 이는 서버가 I/O 를 기다리는 데 리소스를 낭비하지 않도록 합니다.
3. I/O 가 완료될 때까지 다른 작업이 실행될 수 있습니다. 이를 통해 서버는 여러 작업을 동시에 처리할 수 있습니다.
4. I/O 가 준비되면 작업은 중단된 지점부터 계속됩니다. 이는 비동기 프로그래밍의 핵심 기능입니다.

이 패턴은 Python 3.4 에서 Python 표준 라이브러리에 추가된 `asyncio`와 같은 최신 비동기 Python 프레임워크의 기반을 형성합니다.
