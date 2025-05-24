# Criar um Comando Personalizado

A CLI (Command Line Interface) do Flask permite que você crie comandos personalizados que podem ser executados a partir da linha de comando. Vamos criar um comando personalizado chamado `greet` que recebe um nome como argumento e imprime uma mensagem de saudação.

Crie um novo arquivo Python chamado `commands.py` e adicione o seguinte código:

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

Salve o arquivo e execute-o usando o seguinte comando:

```
python commands.py John
```

Você deverá ver a mensagem "Hello, John!" impressa no terminal.
