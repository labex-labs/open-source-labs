# Mémoire et allocation

Dans le cas d'un littéral de chaîne, nous connaissons le contenu à la compilation, donc le texte est directement codé en dur dans l'exécutable final. C'est pourquoi les littéraux de chaîne sont rapides et efficaces. Mais ces propriétés ne viennent que de l'immutabilité des littéraux de chaîne. Malheureusement, nous ne pouvons pas insérer un bloc de mémoire dans le binaire pour chaque morceau de texte dont la taille est inconnue à la compilation et qui peut changer pendant l'exécution du programme.

Avec le type `String`, pour prendre en charge un texte mutable et pouvant grandir, nous devons allouer une quantité de mémoire sur le tas, inconnue à la compilation, pour stocker le contenu. Cela signifie :

- La mémoire doit être demandée à l'allocateur de mémoire à l'exécution.
- Nous avons besoin d'un moyen de renvoyer cette mémoire à l'allocateur lorsque nous avons fini avec notre `String`.

La première partie est faite par nous : lorsque nous appelons `String::from`, son implémentation demande la mémoire dont elle a besoin. Cela est assez universel dans les langages de programmation.

Cependant, la deuxième partie est différente. Dans les langages avec un _ramasse-miettes (GC)_, le GC surveille et nettoie la mémoire qui n'est plus utilisée, et nous n'avons pas besoin de nous en préoccuper. Dans la plupart des langages sans GC, il est de notre responsabilité de déterminer quand la mémoire n'est plus utilisée et d'appeler du code pour la libérer explicitement, tout comme nous l'avons fait pour la demander. Faire cela correctement a historiquement été un problème de programmation difficile. Si nous oublions, nous gaspillons de la mémoire. Si nous le faisons trop tôt, nous aurons une variable invalide. Si nous le faisons deux fois, c'est également un bogue. Nous devons associer exactement un `allocate` avec exactement un `free`.

Rust prend une voie différente : la mémoire est automatiquement renvoyée une fois que la variable qui la possède sort de portée. Voici une version de notre exemple de portée de la liste 4-1 utilisant une `String` au lieu d'un littéral de chaîne :

    {
        let s = String::from("hello"); // s est valide à partir de ce point
        // faire des choses avec s
    }                                  // cette portée est maintenant terminée, et s n'est plus valide

Il y a un point naturel où nous pouvons renvoyer la mémoire dont notre `String` a besoin à l'allocateur : lorsque `s` sort de portée. Lorsqu'une variable sort de portée, Rust appelle une fonction spéciale pour nous. Cette fonction s'appelle `drop`, et c'est là que l'auteur de `String` peut mettre le code pour renvoyer la mémoire. Rust appelle `drop` automatiquement à la parenthèse fermante.

> Note : En C++, ce modèle de libération de ressources à la fin de la durée de vie d'un élément est parfois appelé _Resource Acquisition Is Initialization_ _(RAII)_. La fonction `drop` en Rust vous sera familière si vous avez utilisé des modèles RAII.

Ce modèle a un impact profond sur la manière d'écrire du code Rust. Cela peut sembler simple pour le moment, mais le comportement du code peut être inattendu dans des situations plus complexes lorsque nous voulons avoir plusieurs variables utiliser les données que nous avons allouées sur le tas. Explorons maintenant certaines de ces situations.
