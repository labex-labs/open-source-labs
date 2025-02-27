# Unsafe Superpowers

Pour passer au Rust non sécurisé, utilisez le mot clé `unsafe` puis commencez un nouveau bloc qui contient le code non sécurisé. Vous pouvez effectuer cinq actions en Rust non sécurisé que vous ne pouvez pas en Rust sécurisé, que nous appelons _super-pouvoirs non sécurisés_. Ces super-pouvoirs incluent la capacité de :

1.  Déréférencer un pointeur brut
2.  Appeler une fonction ou une méthode non sécurisée
3.  Accéder ou modifier une variable statique mutable
4.  Implémenter un trait non sécurisé
5.  Accéder aux champs des `union`

Il est important de comprendre que `unsafe` ne désactive pas le vérificateur d'emprunt ni aucune des autres vérifications de sécurité de Rust : si vous utilisez une référence dans du code non sécurisé, elle sera toujours vérifiée. Le mot clé `unsafe` ne vous donne accès que à ces cinq fonctionnalités qui ne sont ensuite pas vérifiées par le compilateur pour la sécurité mémoire. Vous obtiendrez toujours un certain degré de sécurité à l'intérieur d'un bloc `unsafe`.

De plus, `unsafe` ne signifie pas que le code à l'intérieur du bloc est nécessairement dangereux ou qu'il présentera certainement des problèmes de sécurité mémoire : l'idée est que, en tant que programmeur, vous vous assurerez que le code à l'intérieur d'un bloc `unsafe` accédera à la mémoire de manière valide.

Les gens sont fallibles et des erreurs se produiront, mais en exigeant que ces cinq opérations non sécurisées soient à l'intérieur de blocs annotés avec `unsafe`, vous saurez que tout problème lié à la sécurité mémoire doit être dans un bloc `unsafe`. Gardez les blocs `unsafe` petits ; vous serez reconnaissant plus tard lorsque vous investiguerez les bogues de mémoire.

Pour isoler le code non sécurisé le plus possible, il est préférable d'enfermer ce code dans une abstraction sécurisée et de fournir une API sécurisée, que nous aborderons plus tard dans le chapitre lorsque nous examinerons les fonctions et les méthodes non sécurisées. Des parties de la bibliothèque standard sont implémentées comme des abstractions sécurisées sur du code non sécurisé qui a été audité. Enveloppant le code non sécurisé dans une abstraction sécurisée empêche les utilisations de `unsafe` de se propager dans tous les endroits où vous ou vos utilisateurs voudriez utiliser la fonctionnalité implémentée avec du code non sécurisé, car utiliser une abstraction sécurisée est sécurisé.

Examillons chacun des cinq super-pouvoirs non sécurisés tour à tour. Nous examinerons également certaines abstractions qui offrent une interface sécurisée au code non sécurisé.
