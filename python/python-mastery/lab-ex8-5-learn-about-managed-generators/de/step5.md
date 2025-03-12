# Implementierung eines Echo-Servers

Jetzt werden wir die Implementierung eines Echo-Servers zu unserer `server.py`-Datei hinzufügen. Ein Echo-Server ist eine Art Server, der einfach alle Daten, die er von einem Client erhält, zurücksendet. Dies ist eine großartige Möglichkeit, zu verstehen, wie Server eingehende Daten verarbeiten und mit Clients kommunizieren.

Fügen Sie den folgenden Code am Ende der `server.py`-Datei hinzu. Dieser Code wird unseren Echo-Server einrichten und Client-Verbindungen verwalten.

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

Lassen Sie uns diesen Code Schritt für Schritt verstehen:

1. Die `tcp_server`-Funktion:

   - Zunächst richtet sie einen Socket ein, um auf eingehende Verbindungen zu warten. Ein Socket ist ein Endpunkt für die Kommunikation zwischen zwei Maschinen.
   - Dann verwendet sie `yield 'recv', sock`, um die Funktion anzuhalten, bis ein Client eine Verbindung herstellt. Dies ist ein Schlüsselteil unseres asynchronen Ansatzes.
   - Schließlich erstellt sie für jede Client-Verbindung eine neue Handler-Aufgabe. Dies ermöglicht es dem Server, mehrere Clients gleichzeitig zu verwalten.

2. Die `echo_handler`-Funktion:

   - Sie gibt `'recv', client` zurück, um auf die Daten des Clients zu warten. Dies hält die Funktion an, bis Daten verfügbar sind.
   - Sie gibt `'send', client` zurück, um zu warten, bis sie Daten an den Client senden kann. Dies stellt sicher, dass der Client bereit ist, die Daten zu empfangen.
   - Sie verarbeitet die Client-Daten, bis die Verbindung vom Client geschlossen wird.

3. Wenn wir den Server ausführen, fügen wir die `tcp_server`-Aufgabe zur Warteschlange hinzu und starten den Scheduler. Der Scheduler ist für die Verwaltung aller Aufgaben verantwortlich und stellt sicher, dass sie asynchron ausgeführt werden.

Um den Server zu testen, führen Sie ihn in einem Terminal aus:

```bash
python3 /home/labex/project/server.py
```

Sie sollten eine Nachricht sehen, die darauf hinweist, dass der Server läuft. Dies bedeutet, dass der Server jetzt auf eingehende Verbindungen wartet.

Öffnen Sie ein anderes Terminal und verbinden Sie sich mit dem Server mithilfe von `nc` (Netcat). Netcat ist ein einfaches Werkzeug, das es Ihnen ermöglicht, sich mit einem Server zu verbinden und Daten zu senden.

```bash
nc localhost 25000
```

Jetzt können Sie Nachrichten eingeben und sehen, wie sie mit "GOT:" vorangestellt zurückgesendet werden:

```
Hello
GOT:Hello
World
GOT:World
```

Wenn Sie `nc` nicht installiert haben, können Sie die integrierte `telnetlib` von Python verwenden. Telnetlib ist eine Bibliothek, die es Ihnen ermöglicht, sich mit einem Server über das Telnet-Protokoll zu verbinden.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

Sie können mehrere Terminalfenster öffnen und mehrere Clients gleichzeitig verbinden. Der Server wird alle Verbindungen gleichzeitig verwalten, obwohl er single-threaded (eingleitig) ist. Dies ist dank unseres auf Generatoren basierenden Task-Schedulers möglich, der es dem Server ermöglicht, Aufgaben bei Bedarf anzuhalten und fortzusetzen.

## Wie es funktioniert

Dieses Beispiel zeigt eine leistungsstarke Anwendung von Generatoren für asynchrone E/A:

1. Der Server gibt die Kontrolle ab, wenn er normalerweise blockieren würde, während er auf E/A wartet. Dies bedeutet, dass der Server anstatt unendlich lange auf Daten zu warten, anhalten und andere Aufgaben ausführen lassen kann.
2. Der Scheduler verschiebt ihn in einen Wartebereich, bis die E/A bereit ist. Dies stellt sicher, dass der Server keine Ressourcen verschwendet, indem er auf E/A wartet.
3. Andere Aufgaben können ausgeführt werden, während auf die E/A-Vervollständigung gewartet wird. Dies ermöglicht es dem Server, mehrere Aufgaben gleichzeitig zu verwalten.
4. Wenn die E/A bereit ist, wird die Aufgabe dort fortgesetzt, wo sie aufgehört hat. Dies ist ein Schlüsselmerkmal der asynchronen Programmierung.

Dieses Muster bildet die Grundlage moderner asynchroner Python-Frameworks wie `asyncio`, das in Python 3.4 zur Python-Standardbibliothek hinzugefügt wurde.
