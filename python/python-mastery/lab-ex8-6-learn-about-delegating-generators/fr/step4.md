# De générateurs à async/await

Dans cette étape finale, nous allons explorer comment le modèle `yield from` en Python a évolué vers la syntaxe moderne `async`/`await`. Comprendre cette évolution est crucial car elle vous aide à voir le lien entre les générateurs et la programmation asynchrone. La programmation asynchrone permet à votre programme de gérer plusieurs tâches sans attendre que chacune d'elles se termine, ce qui est particulièrement utile en programmation réseau et dans d'autres opérations liées à l'E/S (I/O).

## Le lien entre les générateurs et async/await

La syntaxe `async`/`await`, introduite en Python 3.5, est construite sur la base des fonctionnalités des générateurs et de `yield from`. En réalité, les fonctions `async` sont implémentées à l'aide de générateurs. Cela signifie que les concepts que vous avez appris sur les générateurs sont directement liés au fonctionnement de `async`/`await`.

Pour passer de l'utilisation des générateurs à la syntaxe `async`/`await`, nous devons suivre ces étapes :

1. Utiliser le décorateur `@coroutine` du module `types`. Ce décorateur aide à convertir les fonctions basées sur les générateurs en une forme utilisable avec `async`/`await`.
2. Convertir les fonctions utilisant `yield from` pour utiliser `async` et `await` à la place. Cela rend le code plus lisible et exprime mieux la nature asynchrone des opérations.
3. Mettre à jour la boucle d'événements pour gérer les coroutines natives. La boucle d'événements est responsable de la planification et de l'exécution des tâches asynchrones.

## Mise à jour de la classe GenSocket

Maintenant, modifions notre classe `GenSocket` pour qu'elle fonctionne avec le décorateur `@coroutine`. Cela permettra à notre classe d'être utilisée dans un contexte `async`/`await`.

1. Ouvrez le fichier `server.py` dans l'éditeur. Vous pouvez le faire en exécutant la commande suivante dans le terminal :

```bash
cd /home/labex/project
```

2. En haut du fichier `server.py`, ajoutez l'import pour `coroutine`. Cet import est nécessaire pour utiliser le décorateur `@coroutine`.

```python
from types import coroutine
```

3. Mettez à jour la classe `GenSocket` pour utiliser le décorateur `@coroutine`. Ce décorateur transforme nos méthodes basées sur les générateurs en coroutines attendables, ce qui signifie qu'elles peuvent être utilisées avec le mot - clé `await`.

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

## Conversion vers la syntaxe async/await

Ensuite, convertissons notre code de serveur pour utiliser la syntaxe `async`/`await`. Cela rendra le code plus lisible et exprimera clairement la nature asynchrone des opérations.

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

Remarquez que `yield from` a été remplacé par `await`, et les fonctions sont maintenant définies avec `async def` au lieu de `def`. Ce changement rend le code plus intuitif et plus facile à comprendre.

## Comprendre la transformation

Le passage des générateurs avec `yield from` à la syntaxe `async`/`await` n'est pas seulement un simple changement syntaxique. Il représente un changement dans la façon dont nous pensons la programmation asynchrone.

1. **Générateurs avec yield from** :

   - Lorsque vous utilisez des générateurs avec `yield from`, vous cédez explicitement le contrôle pour signaler qu'une tâche est prête. Cela signifie que vous devez gérer manuellement le moment où une tâche peut continuer.
   - Vous devez également gérer manuellement la planification des tâches. Cela peut être complexe, surtout dans les programmes plus grands.
   - L'accent est mis sur la mécanique du flux de contrôle, ce qui peut rendre le code plus difficile à lire et à maintenir.

2. **Syntaxe async/await** :
   - Avec la syntaxe `async`/`await`, le contrôle est cédé implicitement aux points `await`. Cela rend le code plus simple car vous n'avez pas à vous soucier de céder explicitement le contrôle.
   - La boucle d'événements s'occupe de la planification des tâches, vous n'avez donc pas à la gérer manuellement.
   - L'accent est mis sur le flux logique du programme, ce qui rend le code plus lisible et plus maintenable.

Cette transformation permet d'obtenir un code asynchrone plus lisible et plus maintenable, ce qui est particulièrement important pour les applications complexes comme les serveurs réseau.

## Programmation asynchrone moderne

En Python moderne, nous utilisons généralement le module `asyncio` pour la programmation asynchrone au lieu d'une boucle d'événements personnalisée. Le module `asyncio` offre une prise en charge intégrée de nombreuses fonctionnalités utiles :

- Exécution de plusieurs coroutines de manière concurrente. Cela permet à votre programme de gérer plusieurs tâches en même temps.
- Gestion de l'E/S réseau. Il simplifie le processus d'envoi et de réception de données sur le réseau.
- Primitives de synchronisation. Elles vous aident à gérer l'accès aux ressources partagées dans un environnement concurrent.
- Planification et annulation de tâches. Vous pouvez facilement planifier des tâches pour qu'elles s'exécutent à des moments spécifiques et les annuler si nécessaire.

Voici à quoi pourrait ressembler notre serveur en utilisant `asyncio` :

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

Ce code atteint la même fonctionnalité que notre serveur basé sur les générateurs, mais utilise la bibliothèque standard `asyncio`, qui est plus robuste et riche en fonctionnalités.

## Conclusion

Dans ce laboratoire, vous avez appris plusieurs concepts importants :

1. L'instruction `yield from` et comment elle délègue à un autre générateur. C'est un concept fondamental pour comprendre le fonctionnement des générateurs.
2. Comment utiliser `yield from` avec les coroutines pour le passage de messages. Cela vous permet de communiquer entre différentes parties de votre programme asynchrone.
3. Encapsuler les opérations de socket avec des générateurs pour un code plus propre. Cela rend votre code lié au réseau plus organisé et plus facile à comprendre.
4. La transition des générateurs vers la syntaxe moderne `async`/`await`. Comprendre cette transition vous aidera à écrire un code asynchrone plus lisible et plus maintenable en Python, que vous utilisiez directement les générateurs ou la syntaxe moderne `async`/`await`.
