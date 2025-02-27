# Exporter une API publique pratique avec `pub use`

La structure de votre API publique est une considération importante lors de la publication d'une boîte à outils (crate). Les personnes qui utilisent votre boîte à outils sont moins familières avec la structure que vous et peuvent avoir du mal à trouver les éléments qu'elles souhaitent utiliser si votre boîte à outils a une hiérarchie de modules importante.

Au chapitre 7, nous avons vu comment rendre des éléments publics en utilisant le mot-clé `pub` et comment amener des éléments dans une portée avec le mot-clé `use`. Cependant, la structure qui a du sens pour vous pendant le développement d'une boîte à outils peut ne pas être très pratique pour vos utilisateurs. Vous pouvez vouloir organiser vos structs dans une hiérarchie comportant plusieurs niveaux, mais alors, les personnes qui souhaitent utiliser un type que vous avez défini profondément dans la hiérarchie peuvent avoir du mal à découvrir l'existence de ce type. Ils peuvent également être gênés de devoir taper `use` `my_crate::`un_module`::`un_autre_module`::`TypeUtile`;` plutôt que `use` `my_crate::`TypeUtile`;`.

La bonne nouvelle est que si la structure _n'est pas_ pratique pour les autres à utiliser à partir d'une autre bibliothèque, vous n'avez pas besoin de réorganiser votre organisation interne : au lieu de cela, vous pouvez ré-exporter des éléments pour créer une structure publique différente de votre structure privée en utilisant `pub use`. La _ré-exportation_ prend un élément public dans un emplacement et le rend public dans un autre emplacement, comme s'il était défini dans l'autre emplacement à la place.

Par exemple, disons que nous avons créé une bibliothèque appelée `art` pour modéliser des concepts artistiques. Dans cette bibliothèque, il y a deux modules : un module `kinds` contenant deux énumérations nommées `PrimaryColor` et `SecondaryColor` et un module `utils` contenant une fonction nommée `mix`, comme montré dans la liste 14-3.

Nom du fichier : `src/lib.rs`

```rust
//! # Art
//!
//! Une bibliothèque pour modéliser des concepts artistiques.

pub mod kinds {
    /// Les couleurs primaires selon le modèle de couleur RYB.
    pub enum PrimaryColor {
        Red,
        Yellow,
        Blue,
    }

    /// Les couleurs secondaires selon le modèle de couleur RYB.
    pub enum SecondaryColor {
        Orange,
        Green,
        Purple,
    }
}

pub mod utils {
    use crate::kinds::*;

    /// Combine deux couleurs primaires en quantités égales pour créer
    /// une couleur secondaire.
    pub fn mix(
        c1: PrimaryColor,
        c2: PrimaryColor,
    ) -> SecondaryColor {
        --snip--
    }
}
```

Liste 14-3 : Une bibliothèque `art` avec des éléments organisés dans les modules `kinds` et `utils`

La figure 14-3 montre à quoi ressemblerait la page d'accueil de la documentation de cette boîte à outils générée par `cargo doc`.

Figure 14-3 : Page d'accueil de la documentation de `art` qui liste les modules `kinds` et `utils`

Notez que les types `PrimaryColor` et `SecondaryColor` ne sont pas listés sur la page d'accueil, ni la fonction `mix`. Nous devons cliquer sur `kinds` et `utils` pour les voir.

Une autre boîte à outils qui dépend de cette bibliothèque aurait besoin d'énoncés `use` qui amènent les éléments de `art` dans la portée, en spécifiant la structure de module actuellement définie. La liste 14-4 montre un exemple d'une boîte à outils qui utilise les éléments `PrimaryColor` et `mix` de la boîte à outils `art`.

Nom du fichier : `src/main.rs`

```rust
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}
```

Liste 14-4 : Une boîte à outils utilisant les éléments de la boîte à outils `art` avec sa structure interne exportée

L'auteur du code de la liste 14-4, qui utilise la boîte à outils `art`, a dû découvrir que `PrimaryColor` se trouve dans le module `kinds` et `mix` se trouve dans le module `utils`. La structure de module de la boîte à outils `art` est plus pertinente pour les développeurs travaillant sur la boîte à outils `art` que pour ceux qui l'utilisent. La structure interne ne contient aucune information utile pour quelqu'un qui essaie de comprendre comment utiliser la boîte à outils `art`, mais plutôt cause de la confusion car les développeurs qui l'utilisent doivent trouver où chercher et doivent spécifier les noms de module dans les énoncés `use`.

Pour supprimer l'organisation interne de l'API publique, nous pouvons modifier le code de la boîte à outils `art` de la liste 14-3 pour ajouter des énoncés `pub use` pour ré-exporter les éléments au niveau supérieur, comme montré dans la liste 14-5.

Nom du fichier : `src/lib.rs`

```rust
//! # Art
//!
//! Une bibliothèque pour modéliser des concepts artistiques.

pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    --snip--
}

pub mod utils {
    --snip--
}
```

Liste 14-5 : Ajout d'énoncés `pub use` pour ré-exporter des éléments

La documentation API que `cargo doc` génère pour cette boîte à outils listera désormais et lira les ré-exportations sur la page d'accueil, comme montré dans la figure 14-4, rendant les types `PrimaryColor` et `SecondaryColor` et la fonction `mix` plus faciles à trouver.

Figure 14-4 : Page d'accueil de la documentation de `art` qui liste les ré-exportations

Les utilisateurs de la boîte à outils `art` peuvent toujours voir et utiliser la structure interne de la liste 14-3 comme démontré dans la liste 14-4, ou ils peuvent utiliser la structure plus pratique de la liste 14-5, comme montré dans la liste 14-6.

Nom du fichier : `src/main.rs`

```rust
use art::mix;
use art::PrimaryColor;

fn main() {
    --snip--
}
```

Liste 14-6 : Un programme utilisant les éléments ré-exportés de la boîte à outils `art`

Dans les cas où il y a de nombreux modules imbriqués, la ré-exportation des types au niveau supérieur avec `pub use` peut faire une différence significative dans l'expérience des personnes qui utilisent la boîte à outils. Un autre usage courant de `pub use` est de ré-exporter des définitions d'une dépendance dans la boîte à outils actuelle pour que les définitions de cette boîte à outils fassent partie de l'API publique de votre boîte à outils.

Créer une structure d'API publique utile est plus une question d'art que de science, et vous pouvez itérer pour trouver l'API qui fonctionne le mieux pour vos utilisateurs. Le choix de `pub use` vous donne de la flexibilité quant à la manière dont vous structurez votre boîte à outils internement et découple cette structure interne de ce que vous présentez à vos utilisateurs. Considérez le code de certaines des boîtes à outils que vous avez installées pour voir si leur structure interne diffère de leur API publique.
