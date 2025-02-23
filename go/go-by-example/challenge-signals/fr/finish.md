# Sommaire

Le défi Signals montre comment gérer les signaux Unix dans des programmes Go à l'aide de canaux. En créant un canal tamponné pour recevoir des notifications de `os.Signal` et en enregistrant le canal pour recevoir des notifications de signaux spécifiés à l'aide de `signal.Notify`, nous pouvons gérer les signaux de manière gracieuse et sortir du programme lorsque le signal attendu est reçu.
