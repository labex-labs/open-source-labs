# Introduction

Dans ce laboratoire, nous allons découvrir l'énumération `Option` de la bibliothèque `std` de Rust, qui est utilisée pour gérer les cas où l'absence est possible. Elle propose deux options : `Some(T)` lorsqu'un élément de type `T` est trouvé, et `None` lorsqu'aucun élément n'est trouvé. Ces cas peuvent être traités explicitement à l'aide de `match` ou implicitement à l'aide de `unwrap`. Le traitement explicite permet un contrôle plus fin et des résultats plus significatifs, tandis que `unwrap` peut soit renvoyer l'élément interne soit entraîner une panique.

> **Note** : Si le nom de fichier n'est pas spécifié dans le laboratoire, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
