# HashMap

Alors que les vecteurs stockent des valeurs par un index entier, les `HashMap` stockent des valeurs par clé. Les clés de `HashMap` peuvent être des booléens, des entiers, des chaînes de caractères ou tout autre type qui implémente les traits `Eq` et `Hash`. On en parlera plus longuement dans la section suivante.

Comme les vecteurs, les `HashMap` sont redimensionnables, mais les `HashMap` peuvent également se rétrécir lorsqu'elles ont de l'espace inutilisé. Vous pouvez créer une `HashMap` avec une capacité initiale donnée en utilisant `HashMap::with_capacity(uint)`, ou utiliser `HashMap::new()` pour obtenir une `HashMap` avec une capacité initiale par défaut (recommandé).

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "We're sorry, the call cannot be completed as dialed.
            Please hang up and try again.",
        "645-7689" => "Hello, this is Mr. Awesome's Pizza. My name is Fred.
            What can I get for you today?",
        _ => "Hi! Who is this again?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // Prend une référence et renvoie Option<&V>
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Appel à Daniel: {}", call(number)),
        _ => println!("Je n'ai pas le numéro de Daniel."),
    }

    // `HashMap::insert()` renvoie `None`
    // si la valeur insérée est nouvelle, `Some(value)` sinon
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Appel à Ashley: {}", call(number)),
        _ => println!("Je n'ai pas le numéro d'Ashley."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` renvoie un itérateur qui produit
    // des paires (&'a clé, &'a valeur) dans un ordre arbitraire.
    for (contact, &number) in contacts.iter() {
        println!("Appel à {}: {}", contact, call(number));
    }
}
```

Pour en savoir plus sur le fonctionnement du hachage et des tableaux de hachage (quelquefois appelés tables de hachage), consultez la page Wikipédia sur les tables de hachage.
