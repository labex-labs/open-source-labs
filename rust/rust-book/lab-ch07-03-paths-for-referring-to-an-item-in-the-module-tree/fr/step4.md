# Making Structs and Enums Public

Nous pouvons également utiliser `pub` pour désigner des structs et des enums comme publics, mais il y a quelques détails supplémentaires concernant l'utilisation de `pub` avec des structs et des enums. Si nous utilisons `pub` avant la définition d'un struct, nous rendons le struct public, mais les champs du struct resteront privés. Nous pouvons rendre chacun des champs publics ou non au cas par cas. Dans la Liste 7-9, nous avons défini un struct public `back_of_house::Breakfast` avec un champ public `toast` mais un champ privé `seasonal_fruit`. Cela modélise le cas dans un restaurant où le client peut choisir le type de pain qui accompagne un repas, mais le chef décide de quel fruit accompagner le repas en fonction de ce qui est de saison et en stock. Les fruits disponibles changent rapidement, donc les clients ne peuvent pas choisir le fruit ou même voir lequel fruit ils vont recevoir.

Nom de fichier : `src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // The next line won't compile if we uncomment it; we're not
    // allowed to see or modify the seasonal fruit that comes
    // with the meal
    // meal.seasonal_fruit = String::from("blueberries");
}
```

Liste 7-9 : Un struct avec certains champs publics et certains champs privés

Parce que le champ `toast` dans le struct `back_of_house::Breakfast` est public, dans `eat_at_restaurant` nous pouvons lire et écrire dans le champ `toast` en utilisant la notation pointée. Remarquez que nous ne pouvons pas utiliser le champ `seasonal_fruit` dans `eat_at_restaurant`, car `seasonal_fruit` est privé. Essayez de décommenter la ligne modifiant la valeur du champ `seasonal_fruit` pour voir quel message d'erreur vous obtenez!

De plus, notez que parce que `back_of_house::Breakfast` a un champ privé, le struct doit fournir une fonction associée publique qui construit une instance de `Breakfast` (nous l'avons nommée `summer` ici). Si `Breakfast` n'avait pas une telle fonction, nous ne pourrions pas créer une instance de `Breakfast` dans `eat_at_restaurant` car nous ne pourrions pas définir la valeur du champ privé `seasonal_fruit` dans `eat_at_restaurant`.

En revanche, si nous rendons un enum public, toutes ses variantes sont alors publiques. Nous n'avons besoin que du mot clé `pub` avant le mot clé `enum`, comme montré dans la Liste 7-10.

Nom de fichier : `src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

Liste 7-10 : Désigner un enum comme public rend toutes ses variantes publiques.

Parce que nous avons rendu l'enum `Appetizer` public, nous pouvons utiliser les variantes `Soup` et `Salad` dans `eat_at_restaurant`.

Les enums ne sont pas très utiles à moins que leurs variantes ne soient publiques ; il serait ennuyeux d'avoir à annoter toutes les variantes d'enum avec `pub` dans chaque cas, donc la valeur par défaut pour les variantes d'enum est d'être publiques. Les structs sont souvent utiles sans que leurs champs soient publics, donc les champs de struct suivent la règle générale selon laquelle tout est privé par défaut, sauf s'il est annoté avec `pub`.

Il y a encore une situation impliquant `pub` que nous n'avons pas couverte, et c'est notre dernière fonctionnalité de système de modules : le mot clé `use`. Nous aborderons `use` tout seul d'abord, puis nous montrerons comment combiner `pub` et `use`.
