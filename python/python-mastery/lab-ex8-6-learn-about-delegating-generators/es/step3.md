# Envolver sockets con generadores

En este paso, aprenderemos cómo usar generadores para envolver operaciones de sockets. Este es un concepto realmente importante, especialmente cuando se trata de programación asíncrona. La programación asíncrona permite que tu programa maneje múltiples tareas al mismo tiempo sin esperar a que una tarea termine antes de comenzar otra. Usar generadores para envolver operaciones de sockets puede hacer que tu código sea más eficiente y fácil de manejar.

## Comprender el problema

El archivo `server.py` contiene una implementación simple de un servidor de red utilizando generadores. Echemos un vistazo al código actual. Este código es la base de nuestro servidor, y entenderlo es crucial antes de realizar cualquier cambio.

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

En este código, usamos la palabra clave `yield`. La palabra clave `yield` se utiliza en Python para crear generadores. Un generador es un tipo especial de iterador que te permite pausar y reanudar la ejecución de una función. Aquí, `yield` se utiliza para indicar cuándo el servidor está listo para recibir una conexión o cuándo un manejador de cliente está listo para recibir o enviar datos. Sin embargo, las declaraciones `yield` manuales exponen el funcionamiento interno del bucle de eventos al usuario. Esto significa que el usuario tiene que saber cómo funciona el bucle de eventos, lo que puede hacer que el código sea más difícil de entender y mantener.

## Crear una clase GenSocket

Vamos a crear una clase `GenSocket` para envolver las operaciones de sockets con generadores. Esto hará que nuestro código sea más limpio y legible. Al encapsular las operaciones de sockets en una clase, podemos ocultar los detalles del bucle de eventos al usuario y centrarnos en la lógica de alto nivel del servidor.

1. Abre el archivo `server.py` en el editor:

```bash
cd /home/labex/project
```

Este comando cambia el directorio actual al directorio del proyecto donde se encuentra el archivo `server.py`. Una vez que estés en el directorio correcto, puedes abrir el archivo en tu editor de texto preferido.

2. Agrega la siguiente clase `GenSocket` al final del archivo, antes de cualquier función existente:

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

Esta clase `GenSocket` actúa como un envoltorio para las operaciones de sockets. El método `__init__` inicializa la clase con un objeto de socket. Los métodos `accept`, `recv` y `send` realizan las operaciones de socket correspondientes y usan `yield` para indicar cuándo la operación está lista. El método `__getattr__` permite que la clase reenvíe cualquier otro atributo al objeto de socket subyacente.

3. Ahora, modifica las funciones `tcp_server` y `echo_handler` para usar la clase `GenSocket`:

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

Observa cómo las declaraciones explícitas `yield 'recv', sock` y `yield 'send', client` se han reemplazado con expresiones `yield from` más limpias. La palabra clave `yield from` se utiliza para delegar la ejecución a otro generador. Esto hace que el código sea más legible y oculta los detalles del bucle de eventos al usuario. Ahora, el código se parece más a llamadas de función normales, y el usuario no tiene que preocuparse por el funcionamiento interno del bucle de eventos.

4. Vamos a agregar una función de prueba simple para demostrar cómo se usaría nuestro servidor:

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

Este código es más legible y mantenible. La clase `GenSocket` encapsula la lógica de `yield`, lo que permite que el código del servidor se centre en el flujo de alto nivel en lugar de los detalles del bucle de eventos. La función `run_server` inicia el servidor en el puerto 25000 y maneja la excepción `KeyboardInterrupt`, lo que permite al usuario detener el servidor presionando `Ctrl+C`.

## Comprender los beneficios

El enfoque `yield from` ofrece varios beneficios:

1. **Código más limpio**: Las operaciones de socket se parecen más a llamadas de función normales. Esto hace que el código sea más fácil de leer y entender, especialmente para los principiantes.
2. **Abstracción**: Los detalles del bucle de eventos se ocultan al usuario. El usuario no tiene que saber cómo funciona el bucle de eventos para usar el código del servidor.
3. **Legibilidad**: El código expresa mejor lo que está haciendo en lugar de cómo lo está haciendo. Esto hace que el código sea más autoexplicativo y fácil de mantener.
4. **Mantenibilidad**: Los cambios en el bucle de eventos no requerirán cambios en el código del servidor. Esto significa que si necesitas modificar el bucle de eventos en el futuro, puedes hacerlo sin afectar el código del servidor.

Este patrón es un paso hacia la sintaxis moderna de `async/await`, que exploraremos en el siguiente paso. La sintaxis `async/await` es una forma más avanzada y limpia de escribir código asíncrono en Python, y entender el patrón `yield from` te ayudará a pasar a ella más fácilmente.
