# Utiliser Box`<T>`{=html} pour obtenir un type récursif avec une taille connue

Puisque Rust ne peut pas déterminer combien d'espace allouer pour les types définis de manière récursive, le compilateur renvoie une erreur avec cette suggestion utile :

    help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
    representable
      |
    2 |     Cons(i32, Box<List>),
      |               ++++    +

Dans cette suggestion, _indirection_ signifie que plutôt que de stocker directement une valeur, nous devrions modifier la structure de données pour stocker la valeur indirectement en stockant un pointeur vers la valeur.

Parce qu'un `Box<T>` est un pointeur, Rust sait toujours combien d'espace un `Box<T>` nécessite : la taille d'un pointeur ne change pas en fonction de la quantité de données vers lesquelles il pointe. Cela signifie que nous pouvons placer un `Box<T>` dans la variante `Cons` au lieu d'une autre valeur de type `List` directement. Le `Box<T>` pointera vers la prochaine valeur de type `List` qui se trouvera sur le tas plutôt que dans la variante `Cons`. Conceptuellement, nous avons toujours une liste, créée avec des listes contenant d'autres listes, mais cette implémentation est maintenant plus similaire à placer les éléments les uns à côté des autres plutôt que les uns à l'intérieur des autres.

Nous pouvons modifier la définition de l'énumération `List` dans le Listing 15-2 et l'utilisation de `List` dans le Listing 15-3 pour le code du Listing 15-5, qui compilera.

Nom de fichier : `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(
        1,
        Box::new(Cons(
            2,
            Box::new(Cons(
                3,
                Box::new(Nil)
            ))
        ))
    );
}
```

Listing 15-5 : Définition de `List` qui utilise `Box<T>` pour avoir une taille connue

La variante `Cons` nécessite la taille d'un `i32` plus l'espace pour stocker les données de pointeur de la boîte. La variante `Nil` ne stocke pas de valeurs, donc elle nécessite moins d'espace que la variante `Cons`. Nous savons maintenant qu'une valeur de type `List` prendra la taille d'un `i32` plus la taille des données de pointeur d'une boîte. En utilisant une boîte, nous avons rompu la chaîne infinie et récursive, de sorte que le compilateur peut déterminer la taille qu'il doit allouer pour stocker une valeur de type `List`. La Figure 15-2 montre à quoi ressemble maintenant la variante `Cons`.

Figure 15-2 : Une `List` dont la taille n'est pas infinie, car `Cons` contient un `Box`

Les boîtes ne fournissent que l'indirection et l'allocation sur le tas ; elles n'ont pas d'autres capacités spéciales, comme celles que nous verrons avec les autres types de pointeurs intelligents. Elles n'ont également pas la surcharge de performance que ces capacités spéciales entraînent, de sorte qu'elles peuvent être utiles dans des cas comme la liste cons où l'indirection est la seule caractéristique dont nous avons besoin. Nous examinerons d'autres cas d'utilisation des boîtes au Chapitre 17.

Le type `Box<T>` est un pointeur intelligent car il implémente le trait `Deref`, qui permet de traiter les valeurs de type `Box<T>` comme des références. Lorsqu'une valeur de type `Box<T>` sort de portée, les données stockées sur le tas vers lesquelles la boîte pointe sont également nettoyées en raison de l'implémentation du trait `Drop`. Ces deux traits seront encore plus importants pour la fonctionnalité fournie par les autres types de pointeurs intelligents que nous discuterons dans le reste de ce chapitre. Explorerons ces deux traits en détail.
