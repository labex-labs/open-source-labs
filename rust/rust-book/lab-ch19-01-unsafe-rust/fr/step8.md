# Implémenter un trait non sécurisé

Nous pouvons utiliser `unsafe` pour implémenter un trait non sécurisé. Un trait est non sécurisé lorsqu'au moins une de ses méthodes a une certaine propriété que le compilateur ne peut pas vérifier. Nous déclarons qu'un trait est `non sécurisé` en ajoutant le mot clé `unsafe` avant `trait` et en marquant l'implémentation du trait comme `unsafe` également, comme montré dans le Listing 19-11.

    unsafe trait Foo {
        // méthodes ici
    }

    unsafe impl Foo for i32 {
        // implémentations de méthodes ici
    }

Listing 19-11 : Définition et implémentation d'un trait non sécurisé

En utilisant `unsafe impl`, nous promettons que nous respecterons les propriétés que le compilateur ne peut pas vérifier.

Par exemple, rappelez-vous les traits marqueurs `Send` et `Sync` que nous avons discutés dans "Concurrency extensible avec les traits Send et Sync" : le compilateur implémente automatiquement ces traits si nos types sont composés entièrement de types `Send` et `Sync`. Si nous implémentons un type qui contient un type qui n'est pas `Send` ou `Sync`, tel que des pointeurs bruts, et que nous voulons marquer ce type comme `Send` ou `Sync`, nous devons utiliser `unsafe`. Rust ne peut pas vérifier que notre type respecte les garanties qu'il peut être envoyé en toute sécurité entre les threads ou accès à partir de plusieurs threads ; par conséquent, nous devons effectuer ces vérifications manuellement et indiquer cela avec `unsafe`.
