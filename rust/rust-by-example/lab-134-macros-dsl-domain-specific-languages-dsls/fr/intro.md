# Introduction

Dans ce laboratoire, nous explorons le concept de Domain Specific Languages (DSLs) en Rust, qui sont de mini "langages" intégrés dans les macros Rust. Ces macros se développent en constructions Rust normales, mais offrent une syntaxe concise et intuitive pour une fonctionnalité spécifique. Un exemple pratique est démontré en utilisant une API de calculatrice, où une expression est fournie à la macro et la sortie est imprimée dans la console. Cela permet de créer des interfaces plus complexes comme celles trouvées dans des bibliothèques telles que `lazy_static` ou `clap`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
