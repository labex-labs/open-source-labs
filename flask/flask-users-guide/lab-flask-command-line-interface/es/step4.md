# Crear un comando personalizado

La CLI de Flask le permite crear comandos personalizados que se pueden ejecutar desde la línea de comandos. Vamos a crear un comando personalizado llamado `greet` que tome un nombre como argumento y imprima un mensaje de saludo.

Cree un nuevo archivo de Python llamado `commands.py` y agregue el siguiente código:

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

Guarde el archivo y ejecútelo usando el siguiente comando:

```
python commands.py John
```

Debería ver el mensaje "Hello, John!" impreso en la terminal.
