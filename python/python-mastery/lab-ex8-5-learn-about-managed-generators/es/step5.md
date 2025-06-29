# Implementando un servidor de eco (echo server)

Ahora, vamos a agregar la implementación de un servidor de eco a nuestro archivo `server.py`. Un servidor de eco es un tipo de servidor que simplemente devuelve cualquier dato que reciba de un cliente. Esta es una excelente manera de entender cómo los servidores manejan los datos entrantes y se comunican con los clientes.

Agrega el siguiente código al final del archivo `server.py`. Este código configurará nuestro servidor de eco y manejará las conexiones de los clientes.

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

Vamos a entender este código paso a paso:

1. La función `tcp_server`:
   - Primero, configura un socket para escuchar las conexiones entrantes. Un socket es un punto final para la comunicación entre dos máquinas.
   - Luego, utiliza `yield 'recv', sock` para pausar la función hasta que se conecte un cliente. Esta es una parte clave de nuestro enfoque asíncrono.
   - Finalmente, crea una nueva tarea de manejo para cada conexión de cliente. Esto permite que el servidor maneje múltiples clientes de forma concurrente.

2. La función `echo_handler`:
   - Devuelve `'recv', client` para esperar a que el cliente envíe datos. Esto pausa la función hasta que haya datos disponibles.
   - Devuelve `'send', client` para esperar hasta que pueda enviar datos de vuelta al cliente. Esto asegura que el cliente esté listo para recibir los datos.
   - Procesa los datos del cliente hasta que la conexión sea cerrada por el cliente.

3. Cuando ejecutamos el servidor, agrega la tarea `tcp_server` a la cola y inicia el programador de tareas (scheduler). El programador de tareas es responsable de administrar todas las tareas y asegurarse de que se ejecuten de forma asíncrona.

Para probar el servidor, ejecútalo en una terminal:

```bash
python3 /home/labex/project/server.py
```

Deberías ver un mensaje que indica que el servidor está en funcionamiento. Esto significa que el servidor ahora está escuchando las conexiones entrantes.

Abre otra terminal y conéctate al servidor utilizando `nc` (netcat). Netcat es una utilidad simple que te permite conectarte a un servidor y enviar datos.

```bash
nc localhost 25000
```

Ahora puedes escribir mensajes y verlos devueltos con el prefijo "GOT:":

```
Hello
GOT:Hello
World
GOT:World
```

Si no tienes `nc` instalado, puedes usar la biblioteca incorporada `telnetlib` de Python. Telnetlib es una biblioteca que te permite conectarte a un servidor utilizando el protocolo Telnet.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

Puedes abrir múltiples ventanas de terminal y conectar múltiples clientes simultáneamente. El servidor manejará todas las conexiones de forma concurrente, a pesar de ser de un solo hilo (single - threaded). Esto se debe a nuestro programador de tareas basado en generadores, que permite al servidor pausar y reanudar tareas según sea necesario.

## Cómo funciona

Este ejemplo demuestra una poderosa aplicación de los generadores para la E/S asíncrona (async I/O):

1. El servidor devuelve un valor cuando de lo contrario se bloquearía esperando la E/S. Esto significa que en lugar de esperar indefinidamente por datos, el servidor puede pausar y dejar que otras tareas se ejecuten.
2. El programador de tareas lo mueve a un área de espera hasta que la E/S esté lista. Esto asegura que el servidor no gaste recursos esperando la E/S.
3. Otras tareas pueden ejecutarse mientras se espera a que se complete la E/S. Esto permite que el servidor maneje múltiples tareas de forma concurrente.
4. Cuando la E/S está lista, la tarea continúa desde donde se detuvo. Esta es una característica clave de la programación asíncrona.

Este patrón forma la base de los modernos marcos de trabajo asíncronos de Python como `asyncio`, que se agregó a la biblioteca estándar de Python en Python 3.4.
