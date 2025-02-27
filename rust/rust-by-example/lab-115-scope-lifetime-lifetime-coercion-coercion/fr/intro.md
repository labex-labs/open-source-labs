# Introduction

Dans ce laboratoire, le concept de coercition en Rust est exploré, où une durée de vie plus longue peut être coercée en une durée de vie plus courte pour permettre une fonctionnalité dans une portée spécifique. Cela peut se produire par coercition inférée par le compilateur Rust ou en déclarant une différence de durée de vie en utilisant une syntaxe telle que `<'a: 'b, 'b>`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
