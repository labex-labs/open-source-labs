# Create a Custom Command

The Flask CLI allows you to create custom commands that can be executed from the command line. Let's create a custom command named `greet` that takes a name as an argument and prints a greeting message.

Create a new Python file named `commands.py` and add the following code:

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

Save the file and execute it using the following command:

```
python commands.py John
```

You should see the message "Hello, John!" printed in the terminal.


