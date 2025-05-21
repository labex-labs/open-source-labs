# De Geradores para Async/Await

Nesta etapa final, exploraremos como o padrão `yield from` em Python evoluiu para a sintaxe moderna `async`/`await`. Entender essa evolução é crucial, pois ajuda você a ver a conexão entre geradores e programação assíncrona. A programação assíncrona permite que seu programa lide com múltiplas tarefas sem esperar que cada uma termine, o que é especialmente útil em programação de rede e outras operações de I/O.

## A Conexão entre Geradores e Async/Await

A sintaxe `async`/`await`, introduzida no Python 3.5, é construída sobre a funcionalidade de geradores e `yield from`. Por baixo dos panos, as funções `async` são implementadas usando geradores. Isso significa que os conceitos que você aprendeu sobre geradores estão diretamente relacionados a como `async`/`await` funciona.

Para fazer a transição do uso de geradores para a sintaxe `async`/`await`, precisamos seguir estas etapas:

1. Use o decorador `@coroutine` do módulo `types`. Este decorador ajuda a converter funções baseadas em geradores em uma forma que pode ser usada com `async`/`await`.
2. Converta funções que usam `yield from` para usar `async` e `await` em vez disso. Isso torna o código mais legível e expressa melhor a natureza assíncrona das operações.
3. Atualize o loop de eventos para lidar com corrotinas nativas. O loop de eventos é responsável por agendar e executar tarefas assíncronas.

## Atualizando a Classe GenSocket

Agora, vamos modificar nossa classe `GenSocket` para trabalhar com o decorador `@coroutine`. Isso permitirá que nossa classe seja usada em um contexto `async`/`await`.

1. Abra o arquivo `server.py` no editor. Você pode fazer isso executando o seguinte comando no terminal:

```bash
cd /home/labex/project
```

2. No topo do arquivo `server.py`, adicione a importação para `coroutine`. Esta importação é necessária para usar o decorador `@coroutine`.

```python
from types import coroutine
```

3. Atualize a classe `GenSocket` para usar o decorador `@coroutine`. Este decorador transforma nossos métodos baseados em geradores em corrotinas awaitable, o que significa que eles podem ser usados com a palavra-chave `await`.

```python
class GenSocket:
    """
    Um wrapper baseado em gerador para operações de socket
    que funciona com async/await.
    """
    def __init__(self, sock):
        self.sock = sock

    @coroutine
    def accept(self):
        """Aceita uma conexão e retorna um novo GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    @coroutine
    def recv(self, maxsize):
        """Recebe dados do socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    @coroutine
    def send(self, data):
        """Envia dados para o socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Encaminha quaisquer outros atributos para o socket subjacente"""
        return getattr(self.sock, name)
```

## Convertendo para a Sintaxe Async/Await

Em seguida, vamos converter nosso código do servidor para usar a sintaxe `async`/`await`. Isso tornará o código mais legível e expressará claramente a natureza assíncrona das operações.

```python
async def tcp_server(address, handler):
    """
    Um servidor TCP assíncrono usando async/await.
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
    Um manipulador assíncrono para clientes echo.
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

Observe que `yield from` foi substituído por `await`, e as funções agora são definidas com `async def` em vez de `def`. Essa mudança torna o código mais intuitivo e fácil de entender.

## Compreendendo a Transformação

A transição de geradores com `yield from` para a sintaxe `async`/`await` não é apenas uma simples mudança sintática. Ela representa uma mudança em como pensamos sobre programação assíncrona.

1. **Geradores com yield from**:

   - Ao usar geradores com `yield from`, você explicitamente cede o controle para sinalizar que uma tarefa está pronta. Isso significa que você precisa gerenciar manualmente quando uma tarefa pode continuar.
   - Você também precisa gerenciar manualmente o agendamento de tarefas. Isso pode ser complexo, especialmente em programas maiores.
   - O foco está na mecânica do fluxo de controle, o que pode tornar o código mais difícil de ler e manter.

2. **Sintaxe Async/await**:
   - Com a sintaxe `async`/`await`, o controle é implicitamente cedido nos pontos `await`. Isso torna o código mais direto, pois você não precisa se preocupar em ceder explicitamente o controle.
   - O loop de eventos cuida do agendamento de tarefas, então você não precisa gerenciá-lo manualmente.
   - O foco está no fluxo lógico do programa, o que torna o código mais legível e fácil de manter.

Essa transformação permite um código assíncrono mais legível e fácil de manter, o que é especialmente importante para aplicações complexas como servidores de rede.

## Programação Assíncrona Moderna

No Python moderno, geralmente usamos o módulo `asyncio` para programação assíncrona em vez de um loop de eventos personalizado. O módulo `asyncio` fornece suporte integrado para muitos recursos úteis:

- Executar múltiplas corrotinas simultaneamente. Isso permite que seu programa lide com múltiplas tarefas ao mesmo tempo.
- Gerenciar I/O de rede. Ele simplifica o processo de envio e recebimento de dados pela rede.
- Primitivas de sincronização. Elas ajudam você a gerenciar o acesso a recursos compartilhados em um ambiente concorrente.
- Agendamento e cancelamento de tarefas. Você pode facilmente agendar tarefas para serem executadas em horários específicos e cancelá-las, se necessário.

Veja como nosso servidor pode parecer usando `asyncio`:

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

Este código atinge a mesma funcionalidade que nosso servidor baseado em geradores, mas usa a biblioteca `asyncio` padrão, que é mais robusta e rica em recursos.

## Conclusão

Neste laboratório, você aprendeu sobre vários conceitos importantes:

1. A instrução `yield from` e como ela delega para outro gerador. Este é um conceito fundamental para entender como os geradores funcionam.
2. Como usar `yield from` com corrotinas para passagem de mensagens. Isso permite que você se comunique entre diferentes partes do seu programa assíncrono.
3. Empacotar operações de socket com geradores para um código mais limpo. Isso torna seu código relacionado à rede mais organizado e fácil de entender.
4. A transição de geradores para a sintaxe moderna `async`/`await`. Entender essa transição o ajudará a escrever um código assíncrono mais legível e fácil de manter em Python, seja usando geradores diretamente ou a sintaxe moderna `async`/`await`.
