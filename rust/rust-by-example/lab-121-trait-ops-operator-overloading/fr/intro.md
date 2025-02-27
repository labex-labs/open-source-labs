# Introduction

Dans ce laboratoire, nous explorons le surchargement d'opérateurs en Rust et comment il peut être réalisé grâce à des traits. Les opérateurs en Rust peuvent être surchargés à l'aide de traits, ce qui leur permet d'effectuer différentes tâches en fonction de leurs arguments d'entrée. L'opérateur `+`, par exemple, est un sucre syntaxique pour la méthode `add` et peut être utilisé par tout implémentateur du trait `Add`. Les traits qui surchargent les opérateurs, y compris `Add`, se trouvent dans `core::ops`. Le code Rust fourni montre comment surcharger l'opérateur `+` pour les types personnalisés `Foo` et `Bar`, donnant respectivement des types de sortie différents `FooBar` et `BarFoo`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
