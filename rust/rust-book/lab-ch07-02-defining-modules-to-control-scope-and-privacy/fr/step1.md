# Définir des modules pour contrôler la portée et la confidentialité

Dans cette section, nous parlerons de modules et d'autres parties du système de modules, notamment des _chemins_, qui vous permettent de nommer des éléments ; le mot-clé `use` qui permet d'ajouter un chemin à la portée ; et le mot-clé `pub` pour rendre des éléments publics. Nous aborderons également le mot-clé `as`, les packages externes et l'opérateur glob.

Les _modules_ nous permettent d'organiser le code dans une boîte à outils pour qu'il soit lisible et facilement réutilisable. Les modules nous permettent également de contrôler la _confidentialité_ des éléments car le code à l'intérieur d'un module est privé par défaut. Les éléments privés sont des détails d'implémentation internes qui ne sont pas disponibles pour une utilisation externe. Nous pouvons choisir de rendre publics les modules et les éléments qu'ils contiennent, ce qui les expose et permet à du code externe de les utiliser et de dépendre d'eux.

Par exemple, écrivons une boîte à outils de bibliothèque qui fournit les fonctionnalités d'un restaurant. Nous définirons les signatures des fonctions mais laisserons leurs corps vides pour nous concentrer sur l'organisation du code plutôt que sur l'implémentation d'un restaurant.

Dans l'industrie du restaurant, certaines parties d'un restaurant sont appelées _l'avant-scène_ et d'autres _l'arrière-scène_. L'avant-scène est où se trouvent les clients ; cela englobe l'endroit où les hôtes assiettent les clients, les serveurs prennent les commandes et le paiement, et les barman prennent les commandes de boissons. L'arrière-scène est où les chefs et les cuisiniers travaillent dans la cuisine, les lave-vaisselle nettoient, et les managers font du travail administratif.

Pour structurer notre boîte à outils de cette manière, nous pouvons organiser ses fonctions en modules imbriqués. Créez une nouvelle bibliothèque nommée `restaurant` en exécutant `cargo new restaurant --lib`. Ensuite, entrez le code de la Liste 7-1 dans `src/lib.rs` pour définir certains modules et les signatures des fonctions ; ce code est la partie de l'avant-scène.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}

        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}

        fn serve_order() {}

        fn take_payment() {}
    }
}
```

Liste 7-1 : Un module `front_of_house` contenant d'autres modules qui contiennent ensuite des fonctions

Nous définissons un module avec le mot-clé `mod` suivi du nom du module (dans ce cas, `front_of_house`). Le corps du module se trouve ensuite entre accolades. À l'intérieur des modules, nous pouvons placer d'autres modules, comme dans ce cas avec les modules `hosting` et `serving`. Les modules peuvent également contenir des définitions pour d'autres éléments, tels que des structs, des énumérations, des constantes, des traits et - comme dans la Liste 7-1 - des fonctions.

En utilisant des modules, nous pouvons regrouper des définitions connexes et nommer pourquoi elles sont connexes. Les programmeurs utilisant ce code peuvent naviguer dans le code en fonction des groupes plutôt que d'avoir à lire toutes les définitions, ce qui facilite la recherche des définitions qui leur sont pertinentes. Les programmeurs ajoutant de nouvelles fonctionnalités à ce code sauraient où placer le code pour maintenir l'organisation du programme.

Plus tôt, nous avons mentionné que `src/main.rs` et `src/lib.rs` sont appelés racines de boîte à outils. La raison de leur nom est que le contenu de l'un ou l'autre de ces deux fichiers forme un module nommé `crate` à la racine de la structure de module de la boîte à outils, connue sous le nom d'_arbre de modules_.

La Liste 7-2 montre l'arbre de modules pour la structure de la Liste 7-1.

```bash
crate
└── front_of_house
├── hosting
│ ├── add_to_waitlist
│ └── seat_at_table
└── serving
├── take_order
├── serve_order
└── take_payment
```

Liste 7-2 : L'arbre de modules pour le code de la Liste 7-1

Cet arbre montre comment certains modules se trouvent imbriqués dans d'autres modules ; par exemple, `hosting` est imbriqué dans `front_of_house`. L'arbre montre également que certains modules sont des _frères_, ce qui signifie qu'ils sont définis dans le même module ; `hosting` et `serving` sont des frères définis dans `front_of_house`. Si le module A est contenu dans le module B, nous disons que le module A est le _fils_ du module B et que le module B est le _parent_ du module A. Remarquez que l'arbre de modules complet est enraciné sous le module implicite nommé `crate`.

L'arbre de modules vous peut rappeler l'arbre de répertoires du système de fichiers de votre ordinateur ; c'est une comparaison très appropriée ! Tout comme les répertoires dans un système de fichiers, vous utilisez des modules pour organiser votre code. Et tout comme les fichiers dans un répertoire, nous avons besoin d'un moyen de trouver nos modules.
