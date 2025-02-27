# Introduction

Dans ce laboratoire, on explore le concept de boxing, d'allocation sur la pile et d'allocation sur le tas en Rust. Toutes les valeurs en Rust sont par défaut allouées sur la pile, mais elles peuvent être emballées (allouées sur le tas) à l'aide du type `Box<T>`. Un emballage est un pointeur intelligent vers une valeur allouée sur le tas, et lorsqu'il sort de portée, son destructeur est appelé et la mémoire sur le tas est libérée. Le boxing permet de créer une double indirection et peut être déréférencé à l'aide de l'opérateur `*`. Le laboratoire fournit des exemples de code et des explications sur la manière dont le boxing fonctionne et sur la façon dont il affecte l'allocation de mémoire sur la pile.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
