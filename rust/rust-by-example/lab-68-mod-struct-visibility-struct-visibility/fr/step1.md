# Visibilité des structs

Les structs ont un niveau supplémentaire de visibilité pour leurs champs. La visibilité est par défaut privée et peut être modifiée avec le modificateur `pub`. Cette visibilité n'a d'importance que lorsqu'un struct est accédé depuis l'extérieur du module dans lequel il est défini, et a pour but de cacher des informations (encapsulation).

```rust
mod my {
    // Un struct public avec un champ public de type générique `T`
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // Un struct public avec un champ privé de type générique `T`
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // Une méthode de construction publique
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // Les structs publics avec des champs publics peuvent être construits comme d'habitude
    let open_box = my::OpenBox { contents: "public information" };

    // et leurs champs peuvent être normalement accédés.
    println!("The open box contains: {}", open_box.contents);

    // Les structs publics avec des champs privés ne peuvent pas être construits en utilisant les noms de champs.
    // Erreur! `ClosedBox` a des champs privés
    //let closed_box = my::ClosedBox { contents: "classified information" };
    // TODO ^ Essayez de décommenter cette ligne

    // Cependant, les structs avec des champs privés peuvent être créés en utilisant
    // des constructeurs publics
    let _closed_box = my::ClosedBox::new("classified information");

    // et les champs privés d'un struct public ne peuvent pas être accédés.
    // Erreur! Le champ `contents` est privé
    //println!("The closed box contains: {}", _closed_box.contents);
    // TODO ^ Essayez de décommenter cette ligne
}
```
