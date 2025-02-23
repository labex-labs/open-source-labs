# Résumé

Le laboratoire Signaux montre comment gérer les signaux Unix dans des programmes Go à l'aide de canaux. En créant un canal tamponné pour recevoir des notifications `os.Signal` et en enregistrant le canal pour recevoir des notifications de signaux spécifiés à l'aide de `signal.Notify`, nous pouvons gérer les signaux de manière appropriée et quitter le programme lorsque le signal attendu est reçu.
