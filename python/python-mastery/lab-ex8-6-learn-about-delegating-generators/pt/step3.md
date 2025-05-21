# Empacotando Sockets com Geradores

Nesta etapa, vamos aprender como usar geradores para empacotar operações de socket. Este é um conceito muito importante, especialmente quando se trata de programação assíncrona. A programação assíncrona permite que seu programa lide com múltiplas tarefas de uma vez sem esperar que uma tarefa termine antes de iniciar outra. Usar geradores para empacotar operações de socket pode tornar seu código mais eficiente e mais fácil de gerenciar.

## Compreendendo o Problema

O arquivo `server.py` contém uma implementação simples de servidor de rede usando geradores. Vamos dar uma olhada no código atual. Este código é a base do nosso servidor, e entendê-lo é crucial antes de fazermos quaisquer alterações.

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

Neste código, usamos a palavra-chave `yield`. A palavra-chave `yield` é usada em Python para criar geradores. Um gerador é um tipo especial de iterador que permite pausar e retomar a execução de uma função. Aqui, `yield` é usado para indicar quando o servidor está pronto para receber uma conexão ou quando um manipulador de cliente está pronto para receber ou enviar dados. No entanto, as instruções `yield` manuais expõem o funcionamento interno do loop de eventos ao usuário. Isso significa que o usuário precisa saber como o loop de eventos funciona, o que pode tornar o código mais difícil de entender e manter.

## Criando uma Classe GenSocket

Vamos criar uma classe `GenSocket` para empacotar operações de socket com geradores. Isso tornará nosso código mais limpo e legível. Ao encapsular as operações de socket em uma classe, podemos ocultar os detalhes do loop de eventos do usuário e focar na lógica de alto nível do servidor.

1. Abra o arquivo `server.py` no editor:

```bash
cd /home/labex/project
```

Este comando altera o diretório atual para o diretório do projeto onde o arquivo `server.py` está localizado. Depois de estar no diretório correto, você pode abrir o arquivo em seu editor de texto preferido.

2. Adicione a seguinte classe `GenSocket` ao final do arquivo, antes de quaisquer funções existentes:

```python
class GenSocket:
    """
    Um wrapper baseado em gerador para operações de socket.
    """
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        """Aceita uma conexão e retorna um novo GenSocket"""
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    def recv(self, maxsize):
        """Recebe dados do socket"""
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        """Envia dados para o socket"""
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        """Encaminha quaisquer outros atributos para o socket subjacente"""
        return getattr(self.sock, name)
```

Esta classe `GenSocket` atua como um wrapper para operações de socket. O método `__init__` inicializa a classe com um objeto socket. Os métodos `accept`, `recv` e `send` executam as operações de socket correspondentes e usam `yield` para indicar quando a operação está pronta. O método `__getattr__` permite que a classe encaminhe quaisquer outros atributos para o objeto socket subjacente.

3. Agora, modifique as funções `tcp_server` e `echo_handler` para usar a classe `GenSocket`:

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

Observe como as instruções explícitas `yield 'recv', sock` e `yield 'send', client` foram substituídas por expressões `yield from` mais limpas. A palavra-chave `yield from` é usada para delegar a execução a outro gerador. Isso torna o código mais legível e oculta os detalhes do loop de eventos do usuário. Agora, o código se parece mais com chamadas de função normais, e o usuário não precisa se preocupar com o funcionamento interno do loop de eventos.

4. Vamos adicionar uma função de teste simples para demonstrar como nosso servidor seria usado:

```python
def run_server():
    """Inicia o servidor na porta 25000"""
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

Este código é mais legível e fácil de manter. A classe `GenSocket` encapsula a lógica de produção, permitindo que o código do servidor se concentre no fluxo de alto nível, em vez dos detalhes do loop de eventos. A função `run_server` inicia o servidor na porta 25000 e lida com a exceção `KeyboardInterrupt`, que permite ao usuário parar o servidor pressionando `Ctrl+C`.

## Compreendendo os Benefícios

A abordagem `yield from` oferece vários benefícios:

1. **Código mais limpo**: As operações de socket se parecem mais com chamadas de função normais. Isso torna o código mais fácil de ler e entender, especialmente para iniciantes.
2. **Abstração**: Os detalhes do loop de eventos são ocultos do usuário. O usuário não precisa saber como o loop de eventos funciona para usar o código do servidor.
3. **Legibilidade**: O código expressa melhor o que está fazendo, em vez de como está fazendo. Isso torna o código mais autoexplicativo e mais fácil de manter.
4. **Manutenibilidade**: Mudanças no loop de eventos não exigirão mudanças no código do servidor. Isso significa que, se você precisar modificar o loop de eventos no futuro, poderá fazê-lo sem afetar o código do servidor.

Este padrão é um trampolim para a sintaxe moderna async/await, que exploraremos na próxima etapa. A sintaxe async/await é uma maneira mais avançada e limpa de escrever código assíncrono em Python, e entender o padrão `yield from` o ajudará a fazer a transição para ele com mais facilidade.
