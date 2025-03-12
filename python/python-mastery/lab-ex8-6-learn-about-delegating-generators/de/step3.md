# Einwickeln von Sockets mit Generatoren

In diesem Schritt werden wir lernen, wie man Generatoren verwendet, um Socket-Operationen zu kapseln. Dies ist ein sehr wichtiges Konzept, insbesondere im Bereich der asynchronen Programmierung. Asynchrone Programmierung ermöglicht es Ihrem Programm, mehrere Aufgaben gleichzeitig zu bearbeiten, ohne auf das Ende einer Aufgabe zu warten, bevor eine andere gestartet wird. Die Verwendung von Generatoren zur Kapselung von Socket-Operationen kann Ihren Code effizienter und leichter zu verwalten machen.

## Das Problem verstehen

Die Datei `server.py` enthält eine einfache Implementierung eines Netzwerkservers unter Verwendung von Generatoren. Schauen wir uns den aktuellen Code an. Dieser Code ist die Grundlage unseres Servers, und es ist wichtig, ihn zu verstehen, bevor wir irgendwelche Änderungen vornehmen.

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

In diesem Code verwenden wir das Schlüsselwort `yield`. Das Schlüsselwort `yield` wird in Python verwendet, um Generatoren zu erstellen. Ein Generator ist ein spezieller Typ von Iterator, der es Ihnen ermöglicht, die Ausführung einer Funktion anzuhalten und fortzusetzen. Hier wird `yield` verwendet, um anzuzeigen, wann der Server bereit ist, eine Verbindung zu akzeptieren oder wann ein Client-Handler bereit ist, Daten zu empfangen oder zu senden. Allerdings machen die manuellen `yield`-Anweisungen die internen Funktionsweisen der Ereignisschleife (event loop) dem Benutzer zugänglich. Das bedeutet, dass der Benutzer wissen muss, wie die Ereignisschleife funktioniert, was den Code schwieriger zu verstehen und zu warten macht.

## Erstellen einer GenSocket-Klasse

Lassen Sie uns eine `GenSocket`-Klasse erstellen, um Socket-Operationen mit Generatoren zu kapseln. Dies wird unseren Code sauberer und lesbarer machen. Indem wir die Socket-Operationen in einer Klasse kapseln, können wir die Details der Ereignisschleife vor dem Benutzer verbergen und uns auf die Hochschul-logik des Servers konzentrieren.

1. Öffnen Sie die Datei `server.py` im Editor:

```bash
cd /home/labex/project
```

Dieser Befehl wechselt das aktuelle Verzeichnis in das Projektverzeichnis, in dem sich die Datei `server.py` befindet. Sobald Sie sich im richtigen Verzeichnis befinden, können Sie die Datei in Ihrem bevorzugten Texteditor öffnen.

2. Fügen Sie die folgende `GenSocket`-Klasse am Ende der Datei, vor allen bestehenden Funktionen, hinzu:

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

Diese `GenSocket`-Klasse fungiert als Wrapper für Socket-Operationen. Die `__init__`-Methode initialisiert die Klasse mit einem Socket-Objekt. Die Methoden `accept`, `recv` und `send` führen die entsprechenden Socket-Operationen aus und verwenden `yield`, um anzuzeigen, wann die Operation bereit ist. Die `__getattr__`-Methode ermöglicht es der Klasse, alle anderen Attribute an das zugrunde liegende Socket-Objekt weiterzuleiten.

3. Modifizieren Sie nun die Funktionen `tcp_server` und `echo_handler`, um die `GenSocket`-Klasse zu verwenden:

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

Beachten Sie, wie die expliziten `yield 'recv', sock`- und `yield 'send', client`-Anweisungen durch sauberere `yield from`-Ausdrücke ersetzt wurden. Das Schlüsselwort `yield from` wird verwendet, um die Ausführung an einen anderen Generator zu delegieren. Dies macht den Code lesbarer und verbirgt die Details der Ereignisschleife vor dem Benutzer. Jetzt sieht der Code eher wie normale Funktionsaufrufe aus, und der Benutzer muss sich nicht um die internen Funktionsweisen der Ereignisschleife kümmern.

4. Fügen wir eine einfache Testfunktion hinzu, um zu demonstrieren, wie unser Server verwendet wird:

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

Dieser Code ist lesbarer und leichter zu warten. Die `GenSocket`-Klasse kapselt die Yield-Logik, sodass der Servercode sich auf den Hochschulfluss statt auf die Details der Ereignisschleife konzentrieren kann. Die `run_server`-Funktion startet den Server auf Port 25000 und behandelt die `KeyboardInterrupt`-Ausnahme, die es dem Benutzer ermöglicht, den Server durch Drücken von `Ctrl+C` zu stoppen.

## Die Vorteile verstehen

Der `yield from`-Ansatz bietet mehrere Vorteile:

1. **Sauberer Code**: Die Socket-Operationen sehen eher wie normale Funktionsaufrufe aus. Dies macht den Code leichter zu lesen und zu verstehen, insbesondere für Anfänger.
2. **Abstraktion**: Die Details der Ereignisschleife sind vor dem Benutzer verborgen. Der Benutzer muss nicht wissen, wie die Ereignisschleife funktioniert, um den Servercode zu verwenden.
3. **Lesbarkeit**: Der Code drückt eher aus, was er tut, als wie er es tut. Dies macht den Code selbstverständlicher und leichter zu warten.
4. **Wartbarkeit**: Änderungen an der Ereignisschleife erfordern keine Änderungen am Servercode. Das bedeutet, dass Sie die Ereignisschleife in Zukunft ändern können, ohne den Servercode zu beeinflussen.

Dieses Muster ist ein Sprungbrett zu der modernen async/await-Syntax, die wir im nächsten Schritt untersuchen werden. Die async/await-Syntax ist eine fortschrittlichere und sauberere Art, asynchronen Code in Python zu schreiben, und das Verständnis des `yield from`-Musters wird Ihnen helfen, sich leichter auf sie umzustellen.
