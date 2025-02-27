# Un examen plus approfondi d'une requête HTTP

HTTP est un protocole basé sur le texte, et une requête suit ce format :

    Méthode URI-Version HTTP CRLF
    en-têtes CRLF
    corps du message

La première ligne est la _ligne de requête_ qui contient des informations sur ce que le client demande. La première partie de la ligne de requête indique la _méthode_ utilisée, telle que `GET` ou `POST`, qui décrit comment le client effectue cette requête. Notre client a utilisé une requête `GET`, ce qui signifie qu'il demande des informations.

La partie suivante de la ligne de requête est _/_ qui indique l'_identifiant de ressource uniforme_ _(URI)_ que le client demande : une URI est presque, mais pas tout à fait, la même chose qu'un _localisateur de ressource uniforme_ _(URL)_. La différence entre les URIs et les URLs n'est pas importante pour nos besoins dans ce chapitre, mais la spécification HTTP utilise le terme _URI_, donc nous pouvons simplement substituer mentalement _URL_ à _URI_ ici.

La dernière partie est la version HTTP utilisée par le client, puis la ligne de requête se termine par une séquence CRLF. (CRLF signifie _retour chariot_ et _saut de ligne_, qui sont des termes issus des temps de la machine à écrire!) La séquence CRLF peut également être écrite comme `\r\n`, où `\r` est un retour chariot et `\n` est un saut de ligne. La _séquence CRLF_ sépare la ligne de requête du reste des données de la requête. Notez que lorsqu'on imprime la séquence CRLF, on voit un nouveau ligne commencer plutôt que `\r\n`.

En examinant les données de la ligne de requête que nous avons reçues en exécutant notre programme jusqu'à présent, on voit que `GET` est la méthode, _/_ est l'URI de la requête et `HTTP/1.1` est la version.

Après la ligne de requête, les lignes suivantes à partir de `Host:` sont des en-têtes. Les requêtes `GET` n'ont pas de corps.

Essayez d'effectuer une requête à partir d'un autre navigateur ou de demander une autre adresse, telle que _127.0.0.1:7878/test_, pour voir comment les données de la requête changent.

Maintenant que nous savons ce que le navigateur demande, envoyons quelques données en retour!
