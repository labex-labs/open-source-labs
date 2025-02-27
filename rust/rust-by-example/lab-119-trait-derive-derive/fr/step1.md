# Derive

Le compilateur est capable de fournir des implémentations de base pour certains traits via l'attribut `#[derive]`. Ces traits peuvent toujours être implémentés manuellement si un comportement plus complexe est requis.

Voici une liste des traits pouvant être dérivés :

- Traits de comparaison : `Eq`, `PartialEq`, `Ord`, `PartialOrd`.
- `Clone`, pour créer `T` à partir de `&T` via une copie.
- `Copy`, pour donner à un type une « sémantique de copie » au lieu d'une « sémantique de déplacement ».
- `Hash`, pour calculer un hachage à partir de `&T`.
- `Default`, pour créer une instance vide d'un type de données.
- `Debug`, pour formater une valeur à l'aide du formateur `{:?}`.

```rust
// `Centimeters`, un struct tuple qui peut être comparé
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, un struct tuple qui peut être imprimé
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, un struct tuple sans attribut supplémentaire
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Erreur : `Seconds` ne peut pas être imprimé ; il n'implémente pas le trait `Debug`
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Essayez de décommenter cette ligne

    // Erreur : `Seconds` ne peut pas être comparé ; il n'implémente pas le trait `PartialEq`
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Essayez de décommenter cette ligne

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "plus petit"
        } else {
            "plus grand"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
