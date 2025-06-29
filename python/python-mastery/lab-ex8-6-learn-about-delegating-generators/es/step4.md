# De generadores a async/await

En este último paso, exploraremos cómo el patrón `yield from` en Python evolucionó hacia la sintaxis moderna de `async`/`await`. Comprender esta evolución es crucial, ya que te ayuda a ver la conexión entre los generadores y la programación asíncrona. La programación asíncrona permite que tu programa maneje múltiples tareas sin esperar a que cada una termine, lo cual es especialmente útil en la programación de redes y otras operaciones limitadas por E/S (I/O).

## La conexión entre generadores y async/await

La sintaxis `async`/`await`, introducida en Python 3.5, se basa en la funcionalidad de generadores y `yield from`. Bajo el capó, las funciones `async` se implementan utilizando generadores. Esto significa que los conceptos que has aprendido sobre generadores están directamente relacionados con cómo funciona `async`/`await`.

Para pasar del uso de generadores a la sintaxis `async`/`await`, necesitamos seguir estos pasos:

1. Utilizar el decorador `@coroutine` del módulo `types`. Este decorador ayuda a convertir funciones basadas en generadores en una forma que se pueda usar con `async`/`await`.
2. Convertir las funciones que usan `yield from` para que usen `async` y `await` en su lugar. Esto hace que el código sea más legible y exprese mejor la naturaleza asíncrona de las operaciones.
3. Actualizar el bucle de eventos para manejar corrutinas nativas. El bucle de eventos es responsable de programar y ejecutar tareas asíncronas.

## Actualizar la clase GenSocket

Ahora, modifiquemos nuestra clase `GenSocket` para que funcione con el decorador `@coroutine`. Esto permitirá que nuestra clase se use en un contexto `async`/`await`.

1. Abre el archivo `server.py` en el editor. Puedes hacer esto ejecutando el siguiente comando en la terminal:

```bash
cd /home/labex/project
```

2. En la parte superior del archivo `server.py`, agrega la importación de `coroutine`. Esta importación es necesaria para usar el decorador `@coroutine`.

```python
from types import coroutine
```

3. Actualiza la clase `GenSocket` para usar el decorador `@coroutine`. Este decorador transforma nuestros métodos basados en generadores en corrutinas esperables (awaitable), lo que significa que se pueden usar con la palabra clave `await`.

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

## Convertir a la sintaxis async/await

A continuación, convertamos nuestro código del servidor para usar la sintaxis `async`/`await`. Esto hará que el código sea más legible y exprese claramente la naturaleza asíncrona de las operaciones.

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

Observa que `yield from` se ha reemplazado con `await`, y las funciones ahora se definen con `async def` en lugar de `def`. Este cambio hace que el código sea más intuitivo y fácil de entender.

## Comprender la transformación

La transición de generadores con `yield from` a la sintaxis `async`/`await` no es solo un simple cambio sintáctico. Representa un cambio en cómo pensamos sobre la programación asíncrona.

1. **Generadores con yield from**:
   - Cuando se usan generadores con `yield from`, se cede explícitamente el control para señalar que una tarea está lista. Esto significa que tienes que gestionar manualmente cuándo una tarea puede continuar.
   - También necesitas gestionar manualmente la programación de las tareas. Esto puede ser complejo, especialmente en programas más grandes.
   - El enfoque se centra en la mecánica del flujo de control, lo que puede hacer que el código sea más difícil de leer y mantener.

2. **Sintaxis async/await**:
   - Con la sintaxis `async`/`await`, el control se cede implícitamente en los puntos `await`. Esto hace que el código sea más sencillo, ya que no tienes que preocuparte por ceder explícitamente el control.
   - El bucle de eventos se encarga de programar las tareas, por lo que no tienes que gestionarlo manualmente.
   - El enfoque se centra en el flujo lógico del programa, lo que hace que el código sea más legible y mantenible.

Esta transformación permite escribir código asíncrono más legible y mantenible, lo cual es especialmente importante para aplicaciones complejas como servidores de red.

## Programación asíncrona moderna

En Python moderno, generalmente se utiliza el módulo `asyncio` para la programación asíncrona en lugar de un bucle de eventos personalizado. El módulo `asyncio` proporciona soporte integrado para muchas características útiles:

- Ejecutar múltiples corrutinas de forma concurrente. Esto permite que tu programa maneje múltiples tareas al mismo tiempo.
- Gestionar la E/S de red. Simplifica el proceso de enviar y recibir datos a través de la red.
- Primitivas de sincronización. Estas te ayudan a gestionar el acceso a recursos compartidos en un entorno concurrente.
- Programación y cancelación de tareas. Puedes programar fácilmente tareas para que se ejecuten en momentos específicos y cancelarlas si es necesario.

Así es como podría verse nuestro servidor utilizando `asyncio`:

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

Este código logra la misma funcionalidad que nuestro servidor basado en generadores, pero utiliza la biblioteca estándar `asyncio`, que es más robusta y rica en características.

## Conclusión

En este laboratorio, has aprendido varios conceptos importantes:

1. La declaración `yield from` y cómo delega a otro generador. Este es un concepto fundamental para entender cómo funcionan los generadores.
2. Cómo usar `yield from` con corrutinas para el paso de mensajes. Esto te permite comunicarte entre diferentes partes de tu programa asíncrono.
3. Envolver operaciones de sockets con generadores para un código más limpio. Esto hace que tu código relacionado con la red esté más organizado y sea más fácil de entender.
4. La transición de generadores a la sintaxis moderna de `async`/`await`. Comprender esta transición te ayudará a escribir código asíncrono más legible y mantenible en Python, ya sea que uses generadores directamente o la sintaxis moderna de `async`/`await`.
