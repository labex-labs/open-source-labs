# Packages and Crates

Les premières parties du système de modules que nous aborderons sont les packages et les crates.

Une _crate_ est la plus petite quantité de code que le compilateur Rust considère à la fois. Même si vous exécutez `rustc` plutôt que `cargo` et que vous passez un seul fichier de code source (comme nous l'avons fait tout au début de "Écrire et exécuter un programme Rust"), le compilateur considère ce fichier comme une crate. Les crates peuvent contenir des modules, et les modules peuvent être définis dans d'autres fichiers qui sont compilés avec la crate, comme nous le verrons dans les sections suivantes.

Une crate peut être de deux types : une crate binaire ou une crate bibliothèque. Les _crates binaires_ sont des programmes que vous pouvez compiler en un exécutable que vous pouvez exécuter, comme un programme de ligne de commande ou un serveur. Chacune doit avoir une fonction appelée `main` qui définit ce qui se passe lorsque l'exécutable est exécuté. Toutes les crates que nous avons créées jusqu'à présent ont été des crates binaires.

Les _crates bibliothèques_ n'ont pas de fonction `main`, et elles ne se compilent pas en un exécutable. Au lieu de cela, elles définissent des fonctionnalités destinées à être partagées avec plusieurs projets. Par exemple, la crate `rand` que nous avons utilisée au Chapitre 2 fournit des fonctionnalités pour générer des nombres aléatoires. La plupart du temps, lorsque les Rustaceans disent "crate", ils veulent dire une crate bibliothèque, et ils utilisent "crate" de manière interchangeable avec le concept de programmation général d'une "bibliothèque".

La _racine de la crate_ est un fichier source à partir duquel le compilateur Rust commence et qui constitue le module racine de votre crate (nous expliquerons les modules en profondeur dans "Définir des modules pour contrôler la portée et la confidentialité").

Un _package_ est un paquet d'une ou plusieurs crates qui fournit un ensemble de fonctionnalités. Un package contient un fichier `Cargo.toml` qui décrit comment construire ces crates. Cargo est en fait un package qui contient la crate binaire pour l'outil de ligne de commande que vous avez utilisé pour construire votre code. Le package Cargo contient également une crate bibliothèque dont dépend la crate binaire. D'autres projets peuvent dépendre de la crate bibliothèque Cargo pour utiliser la même logique que l'outil de ligne de commande Cargo.

Une crate peut être de deux types : une crate binaire ou une crate bibliothèque. Un package peut contenir autant de crates binaires que vous le souhaitez, mais au plus qu'une seule crate bibliothèque. Un package doit contenir au moins une crate, que ce soit une crate bibliothèque ou une crate binaire.

Parcourons ce qui se passe lorsque nous créons un package. Tout d'abord, nous entrons la commande `cargo new my-project` :

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

Après avoir exécuté `cargo new my-project`, nous utilisons `ls` pour voir ce que Cargo a créé. Dans le répertoire du projet, il y a un fichier `Cargo.toml`, qui nous donne un package. Il y a également un répertoire `src` qui contient `main.rs`. Ouvrez `Cargo.toml` dans votre éditeur de texte, et notez qu'il n'y est pas fait mention de `src/main.rs`. Cargo suit une convention selon laquelle `src/main.rs` est la racine de la crate d'un crate binaire ayant le même nom que le package. De même, Cargo sait que si le répertoire du package contient `src/lib.rs`, le package contient une crate bibliothèque ayant le même nom que le package, et `src/lib.rs` est sa racine de crate. Cargo passe les fichiers de racine de la crate à `rustc` pour construire la bibliothèque ou le binaire.

Ici, nous avons un package qui ne contient que `src/main.rs`, ce qui signifie qu'il ne contient qu'une crate binaire nommée `my-project`. Si un package contient `src/main.rs` et `src/lib.rs`, il a deux crates : une binaire et une bibliothèque, les deux ayant le même nom que le package. Un package peut avoir plusieurs crates binaires en plaçant des fichiers dans le répertoire `src/bin` : chaque fichier sera une crate binaire distincte.

> **Feuille de synthèse sur les modules**
>
> Avant d'approfondir les détails des modules et des chemins, voici une référence rapide sur la manière dont les modules, les chemins, le mot clé `use` et le mot clé `pub` fonctionnent dans le compilateur, et sur la manière dont la plupart des développeurs organisent leur code. Nous verrons des exemples de chacune de ces règles tout au long de ce chapitre, mais c'est un bon endroit pour se référer comme rappel sur la manière dont les modules fonctionnent.
>
> - **Commencer par la racine de la crate** : Lors de la compilation d'une crate, le compilateur regarde d'abord dans le fichier de racine de la crate (généralement `src/lib.rs` pour une crate bibliothèque ou `src/main.rs` pour une crate binaire) pour le code à compiler.
> - **Déclarer des modules** : Dans le fichier de racine de la crate, vous pouvez déclarer de nouveaux modules ; disons que vous déclarez un module "jardin" avec `mod garden;`. Le compilateur cherchera le code du module dans ces emplacements :
> - En ligne, à l'intérieur des accolades qui remplacent le point-virgule suivant `mod garden`
> - Dans le fichier `src/garden.rs`
> - Dans le fichier `src/garden/mod.rs`
> - **Déclarer des sous-modules** : Dans tout fichier autre que la racine de la crate, vous pouvez déclarer des sous-modules. Par exemple, vous pourriez déclarer `mod vegetables;` dans `src/garden.rs`. Le compilateur cherchera le code du sous-module dans le répertoire nommé pour le module parent dans ces emplacements :
> - En ligne, directement après `mod vegetables`, à l'intérieur des accolades au lieu du point-virgule
> - Dans le fichier `src/garden/vegetables.rs`
> - Dans le fichier `src/garden/vegetables/mod.rs`
> - **Chemins vers le code dans les modules** : Une fois qu'un module fait partie de votre crate, vous pouvez vous référer au code de ce module depuis n'importe où ailleurs dans la même crate, à condition que les règles de confidentialité le permettent, en utilisant le chemin vers le code. Par exemple, un type `Asparagus` dans le module de légumes du jardin serait trouvé à `crate::garden::vegetables::Asparagus`.
> - **Privé vs. public** : Le code à l'intérieur d'un module est privé pour ses modules parents par défaut. Pour rendre un module public, déclarez-le avec `pub mod` au lieu de `mod`. Pour rendre également les éléments à l'intérieur d'un module public, utilisez `pub` avant leurs déclarations.
> - **Le mot clé use** : Dans une portée, le mot clé `use` crée des raccourcis pour les éléments pour réduire la répétition des chemins longs. Dans toute portée qui peut se référer à `crate::garden::vegetables::Asparagus`, vous pouvez créer un raccourci avec `use crate::garden::vegetables::Asparagus;` et à partir de là, vous n'aurez plus qu'à écrire `Asparagus` pour utiliser ce type dans la portée.
>
> Ici, nous créons une crate binaire nommée `backyard` qui illustre ces règles. Le répertoire de la crate, également nommé `backyard`, contient ces fichiers et répertoires :
>
> ```bash
> backyard
> ├── Cargo.lock
> ├── Cargo.toml
> └── src
> ├── garden
> │ └── vegetables.rs
> ├── garden.rs
> └── main.rs
> ```
>
> Le fichier de racine de la crate dans ce cas est `src/main.rs`, et il contient :
>
> ```rust
> use crate::garden::vegetables::Asparagus;
>
> pub mod garden;
>
> fn main() {
>     let plant = Asparagus {};
>     println!("I'm growing {:?}!", plant);
> }
> ```
>
> La ligne `pub mod garden;` indique au compilateur d'inclure le code qu'il trouve dans `src/garden.rs`, qui est :
>
> ```rust
> pub mod vegetables;
> ```
>
> Ici, `pub mod vegetables;` signifie que le code dans `src/garden/vegetables.rs` est également inclus. Ce code est :
>
> ```rust
> #[derive(Debug)]
> pub struct Asparagus {}
> ```
>
> Maintenant, approfondissons les détails de ces règles et démontrons-les en action!
