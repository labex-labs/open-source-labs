# Introduction

Dans ce laboratoire, nous allons explorer le concept d'RAII (Resource Acquisition Is Initialization) en Rust, qui impose que l'acquisition de ressources soit initialisée. Cela signifie que lorsque les objets sortent de portée, leurs destructeurs sont appelés et leurs ressources possédées sont libérées, éliminant ainsi la nécessité de la gestion manuelle de la mémoire et assurant la protection contre les bugs de fuite de ressources. Nous allons également découvrir le trait `Drop` en Rust, qui permet d'implementer une logique de destructeur personnalisée pour les types qui en ont besoin.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
