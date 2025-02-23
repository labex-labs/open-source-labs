# Adresse déjà utilisée

Si vous voyez une erreur `OSError` avec le message "Adresse déjà utilisée" lors de l'essai de démarrer le serveur, cela signifie qu'un autre programme utilise déjà le port 5000, qui est le port par défaut pour le serveur de développement. Vous pouvez soit identifier et arrêter l'autre programme, soit choisir un autre port.

Pour identifier le processus utilisant le port 5000, vous pouvez utiliser la commande `netstat` ou `lsof`. Voici des exemples pour Linux, macOS et Windows :

- Linux :

```bash
netstat -nlp | grep 5000
```

- macOS / Linux :

```bash
lsof -P -i :5000
```

- Windows :

```bash
-ano > netstat | findstr 5000
```

Une fois que vous avez identifié le processus, vous pouvez utiliser d'autres outils du système d'exploitation pour l'arrêter. Après avoir arrêté le processus, vous devriez être en mesure d'exécuter le serveur de développement sans problème.
