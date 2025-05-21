# 제너레이터로 소켓 래핑하기

이 단계에서는 제너레이터를 사용하여 소켓 작업을 래핑하는 방법을 배우겠습니다. 이는 특히 비동기 프로그래밍과 관련하여 매우 중요한 개념입니다. 비동기 프로그래밍을 사용하면 프로그램이 다른 작업이 완료될 때까지 기다리지 않고 여러 작업을 동시에 처리할 수 있습니다. 제너레이터를 사용하여 소켓 작업을 래핑하면 코드를 더 효율적으로 만들고 관리하기 쉽게 만들 수 있습니다.

## 문제 이해하기

`server.py` 파일에는 제너레이터를 사용하는 간단한 네트워크 서버 구현이 포함되어 있습니다. 현재 코드를 살펴보겠습니다. 이 코드는 서버의 기반이며, 변경하기 전에 이를 이해하는 것이 중요합니다.

```python
def tcp_server(address, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield 'recv', sock
        client, addr = sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        yield 'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield 'send', client
        client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()
```

이 코드에서는 `yield` 키워드를 사용합니다. `yield` 키워드는 Python 에서 제너레이터를 만드는 데 사용됩니다. 제너레이터는 함수의 실행을 일시 중지하고 재개할 수 있는 특수한 유형의 반복자입니다. 여기에서 `yield`는 서버가 연결을 받을 준비가 되었거나 클라이언트 핸들러가 데이터를 받거나 보낼 준비가 되었음을 나타내는 데 사용됩니다. 그러나 수동 `yield` 문은 이벤트 루프의 내부 작동 방식을 사용자에게 노출합니다. 즉, 사용자는 이벤트 루프가 작동하는 방식을 알아야 하므로 코드를 이해하고 유지 관리하기 어려울 수 있습니다.

## GenSocket 클래스 만들기

제너레이터로 소켓 작업을 래핑하기 위해 `GenSocket` 클래스를 만들어 보겠습니다. 이렇게 하면 코드가 더 깔끔하고 읽기 쉬워집니다. 소켓 작업을 클래스에 캡슐화함으로써 사용자로부터 이벤트 루프의 세부 정보를 숨기고 서버의 상위 수준 논리에 집중할 수 있습니다.

1. 편집기에서 `server.py` 파일을 엽니다.

```bash
cd /home/labex/project
```

이 명령은 현재 디렉토리를 `server.py` 파일이 있는 프로젝트 디렉토리로 변경합니다. 올바른 디렉토리에 있으면 원하는 텍스트 편집기에서 파일을 열 수 있습니다.

2. 파일의 끝, 기존 함수 앞에 다음 `GenSocket` 클래스를 추가합니다.

```python
class GenSocket:
    """
    A generator-based wrapper for socket operations.
    """
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        """Accept a connection and return a new GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    def recv(self, maxsize):
        """Receive data from the socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        """Send data to the socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Forward any other attributes to the underlying socket"""
        return getattr(self.sock, name)
```

이 `GenSocket` 클래스는 소켓 작업의 래퍼 역할을 합니다. `__init__` 메서드는 소켓 객체로 클래스를 초기화합니다. `accept`, `recv`, `send` 메서드는 해당 소켓 작업을 수행하고 `yield`를 사용하여 작업이 준비되었음을 나타냅니다. `__getattr__` 메서드를 사용하면 클래스가 다른 모든 속성을 기본 소켓 객체로 전달할 수 있습니다.

3. 이제 `tcp_server` 및 `echo_handler` 함수를 수정하여 `GenSocket` 클래스를 사용합니다.

```python
def tcp_server(address, handler):
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = yield from sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        data = yield from client.recv(1000)
        if not data:
            break
        yield from client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()
```

명시적 `yield 'recv', sock` 및 `yield 'send', client` 문이 더 깔끔한 `yield from` 표현식으로 대체된 방식을 확인하십시오. `yield from` 키워드는 실행을 다른 제너레이터로 위임하는 데 사용됩니다. 이렇게 하면 코드를 더 읽기 쉽게 만들고 사용자로부터 이벤트 루프의 세부 정보를 숨길 수 있습니다. 이제 코드는 일반 함수 호출과 더 유사하게 보이며 사용자는 이벤트 루프의 내부 작동 방식에 대해 걱정할 필요가 없습니다.

4. 서버가 어떻게 사용되는지 보여주기 위해 간단한 테스트 함수를 추가해 보겠습니다.

```python
def run_server():
    """Start the server on port 25000"""
    tasks.append(tcp_server(('localhost', 25000), echo_handler))
    try:
        event_loop()
    except KeyboardInterrupt:
        print("Server stopped")

if __name__ == '__main__':
    print("Starting echo server on port 25000...")
    print("Press Ctrl+C to stop")
    run_server()
```

이 코드는 더 읽기 쉽고 유지 관리하기 쉽습니다. `GenSocket` 클래스는 yielding 로직을 캡슐화하여 서버 코드가 이벤트 루프의 세부 사항이 아닌 상위 수준 흐름에 집중할 수 있도록 합니다. `run_server` 함수는 포트 25000 에서 서버를 시작하고 `KeyboardInterrupt` 예외를 처리하여 사용자가 `Ctrl+C`를 눌러 서버를 중지할 수 있도록 합니다.

## 이점 이해하기

`yield from` 접근 방식은 다음과 같은 몇 가지 이점을 제공합니다.

1. **더 깔끔한 코드**: 소켓 작업이 일반 함수 호출과 더 유사하게 보입니다. 이렇게 하면 특히 초보자의 경우 코드를 더 쉽게 읽고 이해할 수 있습니다.
2. **추상화**: 이벤트 루프의 세부 정보가 사용자로부터 숨겨집니다. 사용자는 서버 코드를 사용하기 위해 이벤트 루프가 작동하는 방식을 알 필요가 없습니다.
3. **가독성**: 코드는 수행하는 방식이 아닌 수행하는 작업을 더 잘 표현합니다. 이렇게 하면 코드가 더 자체 설명적이고 유지 관리하기 쉬워집니다.
4. **유지 관리성**: 이벤트 루프에 대한 변경 사항은 서버 코드에 대한 변경 사항을 필요로 하지 않습니다. 즉, 나중에 이벤트 루프를 수정해야 하는 경우 서버 코드에 영향을 주지 않고 그렇게 할 수 있습니다.

이 패턴은 다음 단계에서 살펴볼 최신 async/await 구문에 대한 디딤돌입니다. async/await 구문은 Python 에서 비동기 코드를 작성하는 더 발전되고 깔끔한 방법이며, `yield from` 패턴을 이해하면 더 쉽게 전환할 수 있습니다.
