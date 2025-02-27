# Déplacements partiels

Dans la [décomposition] d'une seule variable, les liaisons de modèle `by-move` et `by-reference` peuvent être utilisées en même temps. Cela entraînera un _déplacement partiel_ de la variable, ce qui signifie que certaines parties de la variable seront déplacées tandis que d'autres resteront. Dans un tel cas, la variable parent ne peut plus être utilisée ensuite dans son ensemble, cependant les parties qui ne sont que référencées (et non déplacées) peuvent toujours être utilisées.

```rust
fn main() {
    #[derive(Debug)]
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let person = Person {
        name: String::from("Alice"),
        age: Box::new(20),
    };

    // `name` est déplacé de `person`, mais `age` est référencé
    let Person { name, ref age } = person;

    println!("L'âge de la personne est {}", age);

    println!("Le nom de la personne est {}", name);

    // Erreur! emprunt d'une valeur partiellement déplacée : `person` le déplacement partiel se produit
    //println!("La structure personne est {:?}", person);

    // `person` ne peut pas être utilisée mais `person.age` peut l'être car il n'est pas déplacé
    println!("L'âge de la personne à partir de la structure personne est {}", person.age);
}
```

(Dans cet exemple, nous stockons la variable `age` sur le tas pour illustrer le déplacement partiel : supprimer `ref` dans le code ci-dessus entraînerait une erreur car la propriété de `person.age` serait déplacée vers la variable `age`. Si `Person.age` était stocké sur la pile, `ref` ne serait pas nécessaire car la définition de `age` copierait les données de `person.age` sans les déplacer.)
