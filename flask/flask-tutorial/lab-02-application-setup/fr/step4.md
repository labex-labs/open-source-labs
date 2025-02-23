# Exécution de l'application

Avec votre application configurée, vous pouvez maintenant l'exécuter en utilisant la commande `flask`. Assurez-vous d'exécuter cette commande à partir du répertoire racine, et non du package `flaskr`.

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

Vous devriez voir une sortie similaire à celle-ci :

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

Ensuite, ouvrez l'onglet **Web 5000**, et vous devriez voir ceci :

![Flask app hello world page](../assets/hello-world.png)
