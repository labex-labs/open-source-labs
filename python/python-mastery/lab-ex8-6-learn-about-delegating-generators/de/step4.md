# Von Generatoren zu Async/Await

In diesem letzten Schritt werden wir untersuchen, wie sich das `yield from`-Muster in Python zur modernen `async`/`await`-Syntax entwickelt hat. Das Verständnis dieser Entwicklung ist von entscheidender Bedeutung, da es Ihnen hilft, die Verbindung zwischen Generatoren und asynchroner Programmierung zu erkennen. Asynchrone Programmierung ermöglicht es Ihrem Programm, mehrere Aufgaben zu bearbeiten, ohne auf das Ende jeder einzelnen Aufgabe zu warten. Dies ist besonders nützlich in der Netzwerkprogrammierung und anderen I/O - gebundenen Operationen.

## Die Verbindung zwischen Generatoren und Async/Await

Die `async`/`await`-Syntax, die in Python 3.5 eingeführt wurde, baut auf der Generator- und `yield from`-Funktionalität auf. Im Hintergrund werden `async`-Funktionen mithilfe von Generatoren implementiert. Das bedeutet, dass die Konzepte, die Sie über Generatoren gelernt haben, direkt mit der Funktionsweise von `async`/`await` zusammenhängen.

Um von der Verwendung von Generatoren zur `async`/`await`-Syntax zu wechseln, müssen wir die folgenden Schritte befolgen:

1. Verwenden Sie den `@coroutine`-Decorator aus dem `types`-Modul. Dieser Decorator hilft dabei, generatorbasierte Funktionen in eine Form zu bringen, die mit `async`/`await` verwendet werden kann.
2. Konvertieren Sie Funktionen, die `yield from` verwenden, so dass sie stattdessen `async` und `await` nutzen. Dies macht den Code lesbarer und bringt die asynchrone Natur der Operationen besser zum Ausdruck.
3. Aktualisieren Sie die Ereignisschleife (event loop), um native Koroutinen zu verarbeiten. Die Ereignisschleife ist für die Planung und Ausführung asynchroner Aufgaben verantwortlich.

## Aktualisieren der GenSocket-Klasse

Jetzt modifizieren wir unsere `GenSocket`-Klasse, damit sie mit dem `@coroutine`-Decorator funktioniert. Dies ermöglicht es uns, unsere Klasse in einem `async`/`await`-Kontext zu verwenden.

1. Öffnen Sie die Datei `server.py` im Editor. Sie können dies tun, indem Sie den folgenden Befehl im Terminal ausführen:

```bash
cd /home/labex/project
```

2. Fügen Sie am Anfang der Datei `server.py` den Import für `coroutine` hinzu. Dieser Import ist erforderlich, um den `@coroutine`-Decorator zu verwenden.

```python
from types import coroutine
```

3. Aktualisieren Sie die `GenSocket`-Klasse, um den `@coroutine`-Decorator zu verwenden. Dieser Decorator wandelt unsere generatorbasierten Methoden in ausführbare Koroutinen um, was bedeutet, dass sie mit dem `await`-Schlüsselwort verwendet werden können.

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

## Umwandlung in die Async/Await-Syntax

Als Nächstes wandeln wir unseren Servercode um, um die `async`/`await`-Syntax zu verwenden. Dies macht den Code lesbarer und bringt die asynchrone Natur der Operationen klar zum Ausdruck.

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

Beachten Sie, dass `yield from` durch `await` ersetzt wurde und die Funktionen jetzt mit `async def` anstelle von `def` definiert werden. Diese Änderung macht den Code intuitiver und leichter zu verstehen.

## Das Verständnis der Transformation

Der Übergang von Generatoren mit `yield from` zur `async`/`await`-Syntax ist nicht nur eine einfache syntaktische Änderung. Er repräsentiert eine Verschiebung in der Art und Weise, wie wir über asynchrone Programmierung denken.

1. **Generatoren mit yield from**:

   - Wenn Sie Generatoren mit `yield from` verwenden, geben Sie explizit die Kontrolle ab, um anzuzeigen, dass eine Aufgabe bereit ist. Das bedeutet, dass Sie manuell verwalten müssen, wann eine Aufgabe fortgesetzt werden kann.
   - Sie müssen auch die Planung der Aufgaben manuell verwalten. Dies kann komplex sein, insbesondere in größeren Programmen.
   - Der Schwerpunkt liegt auf der Mechanik des Kontrollflusses, was den Code schwieriger zu lesen und zu warten machen kann.

2. **Async/await-Syntax**:
   - Mit der `async`/`await`-Syntax wird die Kontrolle implizit an `await`-Punkten abgegeben. Dies macht den Code einfacher, da Sie sich nicht um das explizite Abgeben der Kontrolle kümmern müssen.
   - Die Ereignisschleife kümmert sich um die Planung der Aufgaben, sodass Sie dies nicht manuell verwalten müssen.
   - Der Schwerpunkt liegt auf dem logischen Fluss des Programms, was den Code lesbarer und wartbarer macht.

Diese Transformation ermöglicht einen lesbareren und wartbareren asynchronen Code, was besonders wichtig für komplexe Anwendungen wie Netzwerkserver ist.

## Moderne asynchrone Programmierung

In modernem Python verwenden wir normalerweise das `asyncio`-Modul für asynchrone Programmierung anstelle einer benutzerdefinierten Ereignisschleife. Das `asyncio`-Modul bietet integrierte Unterstützung für viele nützliche Funktionen:

- Gleichzeitiges Ausführen mehrerer Koroutinen. Dies ermöglicht es Ihrem Programm, mehrere Aufgaben gleichzeitig zu bearbeiten.
- Verwaltung von Netzwerk-I/O. Es vereinfacht den Prozess des Senden und Empfangens von Daten über das Netzwerk.
- Synchronisierungsprimitive. Diese helfen Ihnen, den Zugang zu gemeinsamen Ressourcen in einer parallelen Umgebung zu verwalten.
- Aufgabenplanung und -abbruch. Sie können Aufgaben einfach zu bestimmten Zeiten planen und bei Bedarf abbrechen.

So könnte unser Server unter Verwendung von `asyncio` aussehen:

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

Dieser Code erreicht die gleiche Funktionalität wie unser generatorbasierter Server, verwendet jedoch die Standardbibliothek `asyncio`, die robuster und featurereicher ist.

## Fazit

In diesem Lab haben Sie mehrere wichtige Konzepte gelernt:

1. Die `yield from`-Anweisung und wie sie die Ausführung an einen anderen Generator delegiert. Dies ist ein grundlegendes Konzept für das Verständnis der Funktionsweise von Generatoren.
2. Wie man `yield from` mit Koroutinen für die Nachrichtenübertragung verwendet. Dies ermöglicht es Ihnen, zwischen verschiedenen Teilen Ihres asynchronen Programms zu kommunizieren.
3. Das Einwickeln von Socket-Operationen mit Generatoren für einen saubereren Code. Dies macht Ihren netzwerkbezogenen Code besser organisiert und leichter zu verstehen.
4. Der Übergang von Generatoren zur modernen `async`/`await`-Syntax. Das Verständnis dieses Übergangs wird Ihnen helfen, lesbareren und wartbareren asynchronen Code in Python zu schreiben, unabhängig davon, ob Sie direkt Generatoren oder die moderne `async`/`await`-Syntax verwenden.
