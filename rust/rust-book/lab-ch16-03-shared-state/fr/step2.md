# Utilisation de Mutex pour autoriser l'accès aux données par un seul thread à la fois

_Mutex_ est une abréviation de _mutual exclusion_, car un mutex ne permet qu'un seul thread d'accéder à certaines données à un moment donné. Pour accéder aux données d'un mutex, un thread doit tout d'abord signaler qu'il souhaite accéder en demandant à acquérir le _verrou_ du mutex. Le verrou est une structure de données qui fait partie du mutex et qui suit qui a actuellement un accès exclusif aux données. Par conséquent, le mutex est décrit comme _gardant_ les données qu'il détient via le système de verrouillage.

Les mutex ont une réputation de difficulté d'utilisation car vous devez vous souvenir de deux règles :

1. Vous devez tenter d'acquérir le verrou avant d'utiliser les données.
2. Lorsque vous avez fini avec les données protégées par le mutex, vous devez déverrouiller les données pour que d'autres threads puissent acquérir le verrou.

Pour une métaphore du monde réel d'un mutex, imaginez une discussion de panel lors d'une conférence avec un seul micro. Avant qu'un intervenant puisse parler, il doit demander ou signaler qu'il souhaite utiliser le micro. Lorsqu'il obtient le micro, il peut parler aussi longtemps qu'il le souhaite puis remettre le micro au prochain intervenant qui demande à parler. Si un intervenant oublie de remettre le micro lorsqu'il a fini, personne d'autre ne peut parler. Si la gestion du micro partagé se passe mal, le panel ne fonctionnera pas comme prévu!

La gestion des mutex peut être incroyablement difficile à faire correctement, c'est pourquoi tant de gens sont enthousiastes pour les canaux. Cependant, grâce au système de types et aux règles d'appartenance de Rust, vous ne pouvez pas faire de fautes dans le verrouillage et le déverrouillage.
