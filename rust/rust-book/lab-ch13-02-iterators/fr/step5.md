# Using Closures That Capture Their Environment

Plusieurs adapteurs d'itérateur prennent des closures en arguments, et généralement les closures que nous spécifierons en tant qu'arguments pour les adapteurs d'itérateur seront des closures qui capturent leur environnement.

Pour cet exemple, nous utiliserons la méthode `filter` qui prend une closure. La closure reçoit un élément de l'itérateur et renvoie un `bool`. Si la closure renvoie `true`, la valeur sera incluse dans l'itération produite par `filter`. Si la closure renvoie `false`, la valeur ne sera pas incluse.

Dans la Liste 13-16, nous utilisons `filter` avec une closure qui capture la variable `shoe_size` de son environnement pour itérer sur une collection d'instances de la structure `Shoe`. Elle ne renverra que les chaussures de la taille spécifiée.

Nom du fichier : `src/lib.rs`

```rust
#[derive(PartialEq, Debug)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];

        let in_my_size = shoes_in_size(shoes, 10);

        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
    }
}
```

Liste 13-16: Utilisation de la méthode `filter` avec une closure qui capture `shoe_size`

La fonction `shoes_in_size` prend la propriété d'un vecteur de chaussures et une taille de chaussure en paramètres. Elle renvoie un vecteur ne contenant que les chaussures de la taille spécifiée.

Dans le corps de `shoes_in_size`, nous appelons `into_iter` pour créer un itérateur qui prend la propriété du vecteur. Ensuite, nous appelons `filter` pour adapter cet itérateur en un nouvel itérateur ne contenant que les éléments pour lesquels la closure renvoie `true`.

La closure capture le paramètre `shoe_size` de l'environnement et compare la valeur avec la taille de chaque chaussure, ne conservant que les chaussures de la taille spécifiée. Enfin, l'appel à `collect` rassemble les valeurs renvoyées par l'itérateur adapté dans un vecteur qui est renvoyé par la fonction.

Le test montre que lorsqu'on appelle `shoes_in_size`, on obtient seulement les chaussures qui ont la même taille que la valeur que nous avons spécifiée.
