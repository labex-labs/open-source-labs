# Exécuter l'image Docker

Maintenant que vous avez construit l'image, vous pouvez l'exécuter pour voir si elle fonctionne.

Exécutez l'image Docker

```bash
docker run -p 5001:5000 -d python-hello-world
```

Le drapeau `-p` mappe un port exécutant à l'intérieur du conteneur vers votre hôte. Dans ce cas, nous sommes en train de mapper l'application Python exécutant sur le port 5000 à l'intérieur du conteneur, vers le port 5001 sur votre hôte. Notez que si le port 5001 est déjà utilisé par une autre application sur votre hôte, vous devrez peut-être remplacer 5001 par une autre valeur, telle que 5002.

Accédez à l'onglet **PORTS** dans la fenêtre du terminal et cliquez sur le lien pour ouvrir l'application dans un nouvel onglet de navigateur.

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

Dans un terminal, exécutez `curl localhost:5001`, qui renvoie `hello world!`.

Vérifiez la sortie des journaux du conteneur.

Si vous voulez voir les journaux de votre application, vous pouvez utiliser la commande `docker container logs`. Par défaut, `docker container logs` imprime ce qui est envoyé à la sortie standard par votre application. Utilisez `docker container ls` pour trouver l'ID de votre conteneur en cours d'exécution.

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

Le Dockerfile est le moyen de créer des builds reproductibles pour votre application. Un workflow courant consiste à faire exécuter `docker image build` par votre automatisation CI/CD en tant que partie de son processus de build. Une fois les images construites, elles seront envoyées vers un registre central, où elles peuvent être accessibles par tous les environnements (tels qu'un environnement de test) qui ont besoin d'exécuter des instances de cette application. Dans l'étape suivante, nous pousserons notre image personnalisée vers le registre Docker public : le Docker Hub, où elle peut être consommée par d'autres développeurs et opérateurs.
