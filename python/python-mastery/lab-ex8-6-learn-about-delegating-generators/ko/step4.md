# 제너레이터에서 Async/Await로

이 마지막 단계에서는 Python 의 `yield from` 패턴이 어떻게 현대적인 `async`/`await` 구문으로 발전했는지 살펴보겠습니다. 이러한 진화를 이해하는 것은 제너레이터와 비동기 프로그래밍 간의 연결을 파악하는 데 도움이 되므로 매우 중요합니다. 비동기 프로그래밍을 사용하면 프로그램이 각 작업이 완료될 때까지 기다리지 않고 여러 작업을 처리할 수 있으므로 네트워크 프로그래밍 및 기타 I/O 기반 작업에 특히 유용합니다.

## 제너레이터와 Async/Await 간의 연결

Python 3.5 에 도입된 `async`/`await` 구문은 제너레이터 및 `yield from` 기능을 기반으로 구축되었습니다. 내부적으로 `async` 함수는 제너레이터를 사용하여 구현됩니다. 즉, 제너레이터에 대해 배운 개념은 `async`/`await`가 작동하는 방식과 직접적으로 관련이 있습니다.

제너레이터 사용에서 `async`/`await` 구문으로 전환하려면 다음 단계를 따라야 합니다.

1. `types` 모듈에서 `@coroutine` 데코레이터를 사용합니다. 이 데코레이터는 제너레이터 기반 함수를 `async`/`await`와 함께 사용할 수 있는 형태로 변환하는 데 도움이 됩니다.
2. `yield from`을 사용하는 함수를 `async` 및 `await`를 사용하도록 변환합니다. 이렇게 하면 코드를 더 읽기 쉽게 만들고 작업의 비동기적 특성을 더 잘 표현할 수 있습니다.
3. 기본 코루틴을 처리하도록 이벤트 루프를 업데이트합니다. 이벤트 루프는 비동기 작업을 예약하고 실행하는 역할을 합니다.

## GenSocket 클래스 업데이트

이제 `GenSocket` 클래스를 수정하여 `@coroutine` 데코레이터와 함께 작동하도록 하겠습니다. 이렇게 하면 클래스를 `async`/`await` 컨텍스트에서 사용할 수 있습니다.

1. 편집기에서 `server.py` 파일을 엽니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
cd /home/labex/project
```

2. `server.py` 파일의 맨 위에 `coroutine`에 대한 import 를 추가합니다. 이 import 는 `@coroutine` 데코레이터를 사용하기 위해 필요합니다.

```python
from types import coroutine
```

3. `@coroutine` 데코레이터를 사용하도록 `GenSocket` 클래스를 업데이트합니다. 이 데코레이터는 제너레이터 기반 메서드를 awaitable 코루틴으로 변환합니다. 즉, `await` 키워드와 함께 사용할 수 있습니다.

```python
class GenSocket:
    """
    A generator-based wrapper for socket operations
    that works with async/await.
    """
    def __init__(self, sock):
        self.sock = sock

    @coroutine
    def accept(self):
        """Accept a connection and return a new GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    @coroutine
    def recv(self, maxsize):
        """Receive data from the socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    @coroutine
    def send(self, data):
        """Send data to the socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Forward any other attributes to the underlying socket"""
        return getattr(self.sock, name)
```

## Async/Await 구문으로 변환

다음으로, 서버 코드를 변환하여 `async`/`await` 구문을 사용해 보겠습니다. 이렇게 하면 코드를 더 읽기 쉽게 만들고 작업의 비동기적 특성을 명확하게 표현할 수 있습니다.

```python
async def tcp_server(address, handler):
    """
    An asynchronous TCP server using async/await.
    """
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await sock.accept()
        tasks.append(handler(client, addr))

async def echo_handler(client, address):
    """
    An asynchronous handler for echo clients.
    """
    print('Connection from', address)
    while True:
        data = await client.recv(1000)
        if not data:
            break
        await client.send(b'GOT:' + data)
    print('Connection closed')
    client.close()
```

`yield from`이 `await`로 대체되었고 함수가 이제 `def` 대신 `async def`로 정의되었음을 확인하십시오. 이 변경으로 코드가 더 직관적이고 이해하기 쉬워졌습니다.

## 변환 이해하기

`yield from`을 사용하는 제너레이터에서 `async`/`await` 구문으로의 전환은 단순한 구문 변경만은 아닙니다. 이는 비동기 프로그래밍에 대한 사고 방식의 변화를 나타냅니다.

1. **yield from 을 사용하는 제너레이터**:

   - `yield from`을 사용하는 제너레이터를 사용할 때 작업이 준비되었음을 알리기 위해 명시적으로 제어를 양보합니다. 즉, 작업이 언제 계속될 수 있는지 수동으로 관리해야 합니다.
   - 또한 작업의 스케줄링을 수동으로 관리해야 합니다. 이는 특히 더 큰 프로그램에서 복잡할 수 있습니다.
   - 제어 흐름의 메커니즘에 초점을 맞추면 코드를 읽고 유지 관리하기 어려울 수 있습니다.

2. **Async/await 구문**:
   - `async`/`await` 구문을 사용하면 `await` 지점에서 제어가 암시적으로 양보됩니다. 이렇게 하면 제어를 명시적으로 양보하는 것에 대해 걱정할 필요가 없으므로 코드가 더 간단해집니다.
   - 이벤트 루프가 작업의 스케줄링을 처리하므로 수동으로 관리할 필요가 없습니다.
   - 프로그램의 논리적 흐름에 초점을 맞추면 코드를 더 읽기 쉽고 유지 관리할 수 있습니다.

이 변환을 통해 더 읽기 쉽고 유지 관리 가능한 비동기 코드를 사용할 수 있으며, 이는 네트워크 서버와 같은 복잡한 응용 프로그램에 특히 중요합니다.

## 최신 비동기 프로그래밍

최신 Python 에서는 사용자 지정 이벤트 루프 대신 일반적으로 `asyncio` 모듈을 비동기 프로그래밍에 사용합니다. `asyncio` 모듈은 다음과 같은 많은 유용한 기능에 대한 기본 제공 지원을 제공합니다.

- 여러 코루틴을 동시에 실행합니다. 이렇게 하면 프로그램이 여러 작업을 동시에 처리할 수 있습니다.
- 네트워크 I/O 를 관리합니다. 네트워크를 통해 데이터를 보내고 받는 프로세스를 단순화합니다.
- 동기화 기본 요소. 이는 동시 환경에서 공유 리소스에 대한 액세스를 관리하는 데 도움이 됩니다.
- 작업 예약 및 취소. 특정 시간에 실행되도록 작업을 쉽게 예약하고 필요한 경우 취소할 수 있습니다.

다음은 `asyncio`를 사용하는 서버의 모습입니다.

```python
import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Connection from {addr}')

    while True:
        data = await reader.read(1000)
        if not data:
            break

        writer.write(b'GOT:' + data)
        await writer.drain()

    print('Connection closed')
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, 'localhost', 25000
    )

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
```

이 코드는 제너레이터 기반 서버와 동일한 기능을 수행하지만 더 강력하고 기능이 풍부한 표준 `asyncio` 라이브러리를 사용합니다.

## 결론

이 랩에서는 몇 가지 중요한 개념에 대해 배웠습니다.

1. `yield from` 문과 다른 제너레이터로 위임하는 방법. 이는 제너레이터가 작동하는 방식을 이해하는 데 기본적인 개념입니다.
2. 메시지 전달을 위해 코루틴과 함께 `yield from`을 사용하는 방법. 이를 통해 비동기 프로그램의 서로 다른 부분 간에 통신할 수 있습니다.
3. 더 깔끔한 코드를 위해 제너레이터로 소켓 작업을 래핑하는 방법. 이렇게 하면 네트워크 관련 코드가 더 체계적이고 이해하기 쉬워집니다.
4. 제너레이터에서 현대적인 `async`/`await` 구문으로의 전환. 이 전환을 이해하면 제너레이터를 직접 사용하든 현대적인 `async`/`await` 구문을 사용하든 Python 에서 더 읽기 쉽고 유지 관리 가능한 비동기 코드를 작성하는 데 도움이 됩니다.
