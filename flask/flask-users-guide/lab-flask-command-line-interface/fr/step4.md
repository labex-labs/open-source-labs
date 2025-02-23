# Créer une commande personnalisée

L'interface de ligne de commande (CLI) de Flask vous permet de créer des commandes personnalisées qui peuvent être exécutées à partir de la ligne de commande. Créons une commande personnalisée nommée `greet` qui prend un nom en argument et affiche un message de salutation.

Créez un nouveau fichier Python nommé `commands.py` et ajoutez le code suivant :

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

Enregistrez le fichier et exécutez-le à l'aide de la commande suivante :

```
python commands.py John
```

Vous devriez voir le message "Hello, John!" affiché dans le terminal.
