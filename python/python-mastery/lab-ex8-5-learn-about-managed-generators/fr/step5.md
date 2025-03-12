# Implémentation d'un serveur d'écho (echo server)

Maintenant, nous allons ajouter l'implémentation d'un serveur d'écho à notre fichier `server.py`. Un serveur d'écho est un type de serveur qui renvoie simplement les données qu'il reçoit d'un client. C'est un excellent moyen de comprendre comment les serveurs gèrent les données entrantes et communiquent avec les clients.

Ajoutez le code suivant à la fin du fichier `server.py`. Ce code configurera notre serveur d'écho et gérera les connexions clientes.

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

Comprenons ce code étape par étape :

1. La fonction `tcp_server` :

   - Tout d'abord, elle configure un socket pour écouter les connexions entrantes. Un socket est un point final de communication entre deux machines.
   - Ensuite, elle utilise `yield 'recv', sock` pour mettre en pause la fonction jusqu'à ce qu'un client se connecte. C'est une partie essentielle de notre approche asynchrone.
   - Enfin, elle crée une nouvelle tâche de gestion pour chaque connexion client. Cela permet au serveur de gérer plusieurs clients de manière concurrente.

2. La fonction `echo_handler` :

   - Elle cède (yield) `'recv', client` pour attendre que le client envoie des données. Cela met en pause la fonction jusqu'à ce que des données soient disponibles.
   - Elle cède `'send', client` pour attendre qu'elle puisse renvoyer des données au client. Cela garantit que le client est prêt à recevoir les données.
   - Elle traite les données du client jusqu'à ce que la connexion soit fermée par le client.

3. Lorsque nous exécutons le serveur, nous ajoutons la tâche `tcp_server` à la file d'attente et nous démarrons le planificateur. Le planificateur est responsable de la gestion de toutes les tâches et s'assure qu'elles s'exécutent de manière asynchrone.

Pour tester le serveur, exécutez - le dans un terminal :

```bash
python3 /home/labex/project/server.py
```

Vous devriez voir un message indiquant que le serveur est en cours d'exécution. Cela signifie que le serveur écoute maintenant les connexions entrantes.

Ouvrez un autre terminal et connectez - vous au serveur en utilisant `nc` (netcat). Netcat est un utilitaire simple qui vous permet de vous connecter à un serveur et d'envoyer des données.

```bash
nc localhost 25000
```

Maintenant, vous pouvez taper des messages et les voir renvoyés avec le préfixe "GOT:" :

```
Hello
GOT:Hello
World
GOT:World
```

Si vous n'avez pas `nc` installé, vous pouvez utiliser la bibliothèque intégrée `telnetlib` de Python. Telnetlib est une bibliothèque qui vous permet de vous connecter à un serveur en utilisant le protocole Telnet.

```bash
python3 -c "import telnetlib; t = telnetlib.Telnet('localhost', 25000); t.interact()"
```

Vous pouvez ouvrir plusieurs fenêtres de terminal et connecter plusieurs clients simultanément. Le serveur gérera toutes les connexions de manière concurrente, même s'il est mono - thread. Cela est dû à notre planificateur de tâches basé sur les générateurs, qui permet au serveur de mettre en pause et de reprendre les tâches selon les besoins.

## Comment cela fonctionne

Cet exemple démontre une application puissante des générateurs pour les E/S asynchrones :

1. Le serveur cède (yield) lorsqu'il devrait normalement bloquer en attendant des E/S. Cela signifie que, au lieu d'attendre indéfiniment des données, le serveur peut se mettre en pause et laisser d'autres tâches s'exécuter.
2. Le planificateur le déplace dans une zone d'attente jusqu'à ce que les E/S soient prêtes. Cela garantit que le serveur ne gaspille pas de ressources en attendant des E/S.
3. D'autres tâches peuvent s'exécuter pendant que l'on attend que les E/S se terminent. Cela permet au serveur de gérer plusieurs tâches de manière concurrente.
4. Lorsque les E/S sont prêtes, la tâche reprend là où elle s'était arrêtée. C'est une caractéristique clé de la programmation asynchrone.

Ce modèle forme la base des frameworks Python asynchrones modernes comme `asyncio`, qui a été ajouté à la bibliothèque standard de Python en Python 3.4.
