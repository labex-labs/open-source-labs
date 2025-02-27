# Capturer l'environnement avec les closures

Nous allons tout d'abord examiner comment utiliser les closures pour capturer des valeurs de l'environnement dans lequel elles sont définies pour une utilisation ultérieure. Voici le scénario : de temps en temps, notre société de T-shirts distribue une chemise exclusive et limitée à quelqu'un de notre liste de diffusion en tant que promotion. Les personnes inscrites sur la liste de diffusion peuvent optionnellement ajouter leur couleur préférée à leur profil. Si la personne choisie pour une chemise gratuite a défini sa couleur préférée, elle reçoit une chemise de cette couleur. Si la personne n'a pas spécifié de couleur préférée, elle reçoit la couleur que la société a le plus en stock actuellement.

Il existe de nombreuses façons de mettre en œuvre cela. Pour cet exemple, nous allons utiliser une énumération appelée `ShirtColor` qui a les variantes `Red` et `Blue` (limitant le nombre de couleurs disponibles pour la simplicité). Nous représentons le stock de la société avec une structure `Inventory` qui a un champ nommé `shirts` qui contient un `Vec<ShirtColor>` représentant les couleurs de chemises actuellement en stock. La méthode `giveaway` définie sur `Inventory` obtient la préférence de couleur de chemise optionnelle du gagnant de la chemise gratuite et renvoie la couleur de chemise que la personne recevra. Ce montage est montré dans la Liste 13-1.

Nom du fichier : `src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

Liste 13-1 : Situation de distribution de chemises par la société de T-shirts

Le `store` défini dans `main` a deux chemises bleues et une chemise rouge restantes à distribuer pour cette promotion limitée \[2\]. Nous appelons la méthode `giveaway` pour un utilisateur ayant une préférence pour une chemise rouge \[3\] et un utilisateur sans aucune préférence \[4\].

Encore une fois, ce code pourrait être implémenté de nombreuses façons, et ici, pour nous concentrer sur les closures, nous sommes restés aux concepts que vous avez déjà appris, excepté le corps de la méthode `giveaway` qui utilise une closure. Dans la méthode `giveaway`, nous obtenons la préférence de l'utilisateur en tant que paramètre de type `Option<ShirtColor>` et appelons la méthode `unwrap_or_else` sur `user_preference` \[1\]. La méthode `unwrap_or_else` sur `Option<T>` est définie par la bibliothèque standard. Elle prend un argument : une closure sans aucun argument qui renvoie une valeur `T` (le même type stocké dans la variante `Some` de `Option<T>`, dans ce cas `ShirtColor`). Si `Option<T>` est la variante `Some`, `unwrap_or_else` renvoie la valeur à l'intérieur de `Some`. Si `Option<T>` est la variante `None`, `unwrap_or_else` appelle la closure et renvoie la valeur renvoyée par la closure.

Nous spécifions l'expression de closure `|| self.most_stocked()` comme argument pour `unwrap_or_else`. Il s'agit d'une closure qui ne prend pas de paramètres elle-même (si la closure avait des paramètres, ils apparaîtraient entre les deux tuyaux verticaux). Le corps de la closure appelle `self.most_stocked()`. Nous définissons la closure ici, et l'implémentation de `unwrap_or_else` évaluera la closure plus tard si le résultat est nécessaire.

Exécuter ce code affiche ce qui suit :

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

Un aspect intéressant ici est que nous avons passé une closure qui appelle `self.most_stocked()` sur l'instance `Inventory` actuelle. La bibliothèque standard n'a pas besoin de savoir quoi que ce soit sur les types `Inventory` ou `ShirtColor` que nous avons définis, ou sur la logique que nous voulons utiliser dans ce scénario. La closure capture une référence immuable à l'instance `Inventory` `self` et la passe avec le code que nous spécifions à la méthode `unwrap_or_else`. Les fonctions, en revanche, ne sont pas capables de capturer leur environnement de cette manière.
