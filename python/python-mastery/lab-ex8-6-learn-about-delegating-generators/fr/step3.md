# Encapsulation des sockets avec des générateurs

Dans cette étape, nous allons apprendre à utiliser des générateurs pour encapsuler les opérations de socket. C'est un concept très important, surtout en ce qui concerne la programmation asynchrone. La programmation asynchrone permet à votre programme de gérer plusieurs tâches simultanément sans attendre qu'une tâche se termine avant de commencer une autre. L'utilisation de générateurs pour encapsuler les opérations de socket peut rendre votre code plus efficace et plus facile à gérer.

## Comprendre le problème

Le fichier `server.py` contient une implémentation simple d'un serveur réseau utilisant des générateurs. Jetons un coup d'œil au code actuel. Ce code est la base de notre serveur, et il est crucial de le comprendre avant d'apporter des modifications.

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

Dans ce code, nous utilisons le mot-clé `yield`. Le mot-clé `yield` est utilisé en Python pour créer des générateurs. Un générateur est un type spécial d'itérateur qui vous permet de mettre en pause et de reprendre l'exécution d'une fonction. Ici, `yield` est utilisé pour indiquer quand le serveur est prêt à recevoir une connexion ou quand un gestionnaire de client est prêt à recevoir ou à envoyer des données. Cependant, les instructions `yield` manuelles exposent le fonctionnement interne de la boucle d'événements à l'utilisateur. Cela signifie que l'utilisateur doit savoir comment fonctionne la boucle d'événements, ce qui peut rendre le code plus difficile à comprendre et à maintenir.

## Création d'une classe GenSocket

Créons une classe `GenSocket` pour encapsuler les opérations de socket avec des générateurs. Cela rendra notre code plus propre et plus lisible. En encapsulant les opérations de socket dans une classe, nous pouvons cacher les détails de la boucle d'événements à l'utilisateur et nous concentrer sur la logique de haut niveau du serveur.

1. Ouvrez le fichier `server.py` dans l'éditeur :

```bash
cd /home/labex/project
```

Cette commande change le répertoire courant pour le répertoire du projet où se trouve le fichier `server.py`. Une fois que vous êtes dans le bon répertoire, vous pouvez ouvrir le fichier dans votre éditeur de texte préféré.

2. Ajoutez la classe `GenSocket` suivante à la fin du fichier, avant toute fonction existante :

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

Cette classe `GenSocket` agit comme un wrapper pour les opérations de socket. La méthode `__init__` initialise la classe avec un objet socket. Les méthodes `accept`, `recv` et `send` effectuent les opérations de socket correspondantes et utilisent `yield` pour indiquer quand l'opération est prête. La méthode `__getattr__` permet à la classe de transférer tous les autres attributs à l'objet socket sous-jacent.

3. Maintenant, modifiez les fonctions `tcp_server` et `echo_handler` pour utiliser la classe `GenSocket` :

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

Remarquez comment les instructions explicites `yield 'recv', sock` et `yield 'send', client` ont été remplacées par des expressions `yield from` plus propres. Le mot-clé `yield from` est utilisé pour déléguer l'exécution à un autre générateur. Cela rend le code plus lisible et cache les détails de la boucle d'événements à l'utilisateur. Maintenant, le code ressemble plus à des appels de fonction normaux, et l'utilisateur n'a pas à se soucier du fonctionnement interne de la boucle d'événements.

4. Ajoutons une fonction de test simple pour démontrer comment notre serveur serait utilisé :

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

Ce code est plus lisible et plus maintenable. La classe `GenSocket` encapsule la logique de rendu, permettant au code du serveur de se concentrer sur le flux de haut niveau plutôt que sur les détails de la boucle d'événements. La fonction `run_server` démarre le serveur sur le port 25000 et gère l'exception `KeyboardInterrupt`, ce qui permet à l'utilisateur d'arrêter le serveur en appuyant sur `Ctrl+C`.

## Comprendre les avantages

L'approche `yield from` offre plusieurs avantages :

1. **Code plus propre** : Les opérations de socket ressemblent plus à des appels de fonction normaux. Cela rend le code plus facile à lire et à comprendre, surtout pour les débutants.
2. **Abstraction** : Les détails de la boucle d'événements sont cachés à l'utilisateur. L'utilisateur n'a pas besoin de savoir comment fonctionne la boucle d'événements pour utiliser le code du serveur.
3. **Lisibilité** : Le code exprime mieux ce qu'il fait plutôt que comment il le fait. Cela rend le code plus explicite et plus facile à maintenir.
4. **Maintenabilité** : Les modifications apportées à la boucle d'événements n'auront pas besoin de modifier le code du serveur. Cela signifie que si vous avez besoin de modifier la boucle d'événements à l'avenir, vous pouvez le faire sans affecter le code du serveur.

Ce modèle est un tremplin vers la syntaxe async/await moderne, que nous explorerons dans l'étape suivante. La syntaxe async/await est un moyen plus avancé et plus propre d'écrire du code asynchrone en Python, et la compréhension du modèle `yield from` vous aidera à passer à elle plus facilement.
