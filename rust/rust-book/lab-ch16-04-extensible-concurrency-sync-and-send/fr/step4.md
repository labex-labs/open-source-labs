# Implementing Send and Sync Manually Is Unsafe

Étant donné que les types composés des traits `Send` et `Sync` sont automatiquement également `Send` et `Sync`, nous n'avons pas besoin d'implémenter manuellement ces traits. En tant que traits marqueurs, ils n'ont même pas de méthodes à implémenter. Ils sont simplement utiles pour imposer des invariants liés à la concurrence.

L'implémentation manuelle de ces traits implique l'écriture de code Rust non sécurisé. Nous parlerons de l'utilisation de code Rust non sécurisé au chapitre 19 ; pour l'instant, l'information importante est que la construction de nouveaux types concurrents ne composés pas de parties `Send` et `Sync` nécessite une réflexion approfondie pour maintenir les garanties de sécurité. *https://doc.rust-lang.org/stable/nomicon* contient plus d'informations sur ces garanties et sur la manière de les maintenir.
