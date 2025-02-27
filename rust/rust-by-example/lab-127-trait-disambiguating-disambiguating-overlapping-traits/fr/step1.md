# Disambiguïsation des traits imbriqués

Un type peut implémenter de nombreux traits différents. Et si deux traits ont le même nom? Par exemple, de nombreux traits pourraient avoir une méthode nommée `get()`. Ils pourraient même avoir des types de retour différents!

Bonne nouvelle : puisque chaque implémentation de trait a son propre bloc `impl`, il est clair lequel des `get` de trait vous implémentez.

Et quand il est temps d'_appeler_ ces méthodes? Pour les distinguer, nous devons utiliser la syntaxe Qualifiée en Toutes Longueurs.

```rust
trait UsernameWidget {
    // Récupérer le nom d'utilisateur sélectionné dans ce widget
    fn get(&self) -> String;
}

trait AgeWidget {
    // Récupérer l'âge sélectionné dans ce widget
    fn get(&self) -> u8;
}

// Un formulaire avec à la fois un UsernameWidget et un AgeWidget
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // Si vous décommentez cette ligne, vous obtiendrez une erreur disant
    // "multiple `get` found". Parce que, après tout, il y a plusieurs méthodes
    // nommées `get`.
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
