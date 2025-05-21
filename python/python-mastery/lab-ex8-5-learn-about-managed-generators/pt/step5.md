# Implementando um Servidor Echo

Agora, vamos adicionar a implementação de um servidor echo ao nosso arquivo `server.py`. Um servidor echo é um tipo de servidor que simplesmente envia de volta quaisquer dados que recebe de um cliente. Esta é uma ótima maneira de entender como os servidores lidam com dados recebidos e se comunicam com os clientes.

Adicione o seguinte código ao final do arquivo `server.py`. Este código configurará nosso servidor echo e lidará com as conexões dos clientes.

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

Vamos entender este código passo a passo:

1. A função `tcp_server`:

   - Primeiro, ela configura um socket para ouvir as conexões recebidas. Um socket é um ponto final para comunicação entre duas máquinas.
   - Em seguida, ela usa `yield 'recv', sock` para pausar a função até que um cliente se conecte. Esta é uma parte fundamental de nossa abordagem assíncrona.
   - Finalmente, ela cria uma nova tarefa de manipulador para cada conexão de cliente. Isso permite que o servidor lide com múltiplos clientes simultaneamente.

2. A função `echo_handler`:

   - Ela produz `'recv', client` para esperar que o cliente envie dados. Isso pausa a função até que os dados estejam disponíveis.
   - Ela produz `'send', client` para esperar até que possa enviar dados de volta ao cliente. Isso garante que o cliente esteja pronto para receber os dados.
   - Ela processa os dados do cliente até que a conexão seja fechada pelo cliente.

3. Quando executamos o servidor, ele adiciona a tarefa `tcp_server` à fila e inicia o agendador. O agendador é responsável por gerenciar todas as tarefas e garantir que elas sejam executadas de forma assíncrona.

Para testar o servidor, execute-o em um terminal:

```bash
python3 /home/labex/project/server.py
```

Você deve ver uma mensagem indicando que o servidor está em execução. Isso significa que o servidor agora está ouvindo as conexões recebidas.

Abra outro terminal e conecte-se ao servidor usando `nc` (netcat). Netcat é um utilitário simples que permite que você se conecte a um servidor e envie dados.

```bash
nc localhost 25000
```

Agora você pode digitar mensagens e vê-las sendo ecoadas de volta com o prefixo "GOT:":

```
Hello
GOT:Hello
World
GOT:World
```

Se você não tiver `nc` instalado, pode usar o `telnetlib` embutido do Python. Telnetlib é uma biblioteca que permite que você se conecte a um servidor usando o protocolo Telnet.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

Você pode abrir várias janelas de terminal e conectar vários clientes simultaneamente. O servidor lidará com todas as conexões simultaneamente, apesar de ser de thread único. Isso é graças ao nosso agendador de tarefas baseado em geradores, que permite que o servidor pause e retome as tarefas conforme necessário.

## Como Funciona

Este exemplo demonstra uma aplicação poderosa de geradores para I/O assíncrono:

1. O servidor produz (yield) quando, de outra forma, bloquearia esperando por I/O. Isso significa que, em vez de esperar indefinidamente por dados, o servidor pode pausar e deixar outras tarefas serem executadas.
2. O agendador o move para uma área de espera até que o I/O esteja pronto. Isso garante que o servidor não desperdice recursos esperando por I/O.
3. Outras tarefas podem ser executadas enquanto esperam a conclusão do I/O. Isso permite que o servidor lide com múltiplas tarefas simultaneamente.
4. Quando o I/O está pronto, a tarefa continua de onde parou. Este é um recurso fundamental da programação assíncrona.

Este padrão forma a base de frameworks Python assíncronos modernos como `asyncio`, que foi adicionado à biblioteca padrão do Python na versão 3.4.
