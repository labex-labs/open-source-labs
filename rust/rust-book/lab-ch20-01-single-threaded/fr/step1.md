# Building a Single-Threaded Web Server

Nous allons commencer par faire fonctionner un serveur web mono-fil. Avant de commencer, jetons un coup d'œil rapide sur les protocoles impliqués dans la construction de serveurs web. Les détails de ces protocoles sont en dehors du champ d'étude de ce livre, mais une vue d'ensemble rapide vous donnera les informations dont vous avez besoin.

Les deux principaux protocoles impliqués dans les serveurs web sont le _Hypertext Transfer Protocol_ _(HTTP)_ et le _Transmission Control Protocol_ _(TCP)_. Les deux protocoles sont des protocoles _demande-réponse_, ce qui signifie qu'un _client_ initie des requêtes et qu'un _serveur_ écoute les requêtes et fournit une réponse au client. Le contenu de ces requêtes et réponses est défini par les protocoles.

TCP est le protocole de niveau inférieur qui décrit les détails de la manière dont l'information passe d'un serveur à l'autre, mais ne spécifie pas ce que cette information est. HTTP s'appuie sur TCP en définissant le contenu des requêtes et des réponses. Technologiquement, il est possible d'utiliser HTTP avec d'autres protocoles, mais dans la grande majorité des cas, HTTP envoie ses données via TCP. Nous travaillerons avec les octets bruts des requêtes et réponses TCP et HTTP.
