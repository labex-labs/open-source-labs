# Erstellen eines benutzerdefinierten Befehls

Die Flask CLI ermöglicht es Ihnen, benutzerdefinierte Befehle zu erstellen, die von der Befehlszeile ausgeführt werden können. Erstellen wir einen benutzerdefinierten Befehl namens `greet`, der einen Namen als Argument nimmt und eine Begrüßungsnachricht ausgibt.

Erstellen Sie eine neue Python-Datei mit dem Namen `commands.py` und fügen Sie den folgenden Code hinzu:

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

Speichern Sie die Datei und führen Sie sie mit dem folgenden Befehl aus:

```
python commands.py John
```

Sie sollten die Nachricht "Hello, John!" in der Konsole sehen.
