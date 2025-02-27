# Extensible Concurrency with the Send and Sync Traits

Intéressamment, le langage Rust a _très_ peu de fonctionnalités de concurrence. Presque toutes les fonctionnalités de concurrence dont nous avons parlé jusqu'à présent dans ce chapitre font partie de la bibliothèque standard, et non du langage. Vos options pour gérer la concurrence ne sont pas limitées au langage ou à la bibliothèque standard ; vous pouvez écrire vos propres fonctionnalités de concurrence ou utiliser celles écrites par d'autres.

Cependant, deux concepts de concurrence sont intégrés au langage : les traits `std::marker` `Send` et `Sync`.
