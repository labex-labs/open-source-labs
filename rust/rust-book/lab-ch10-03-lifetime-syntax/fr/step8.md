# Lifetime Annotations in Struct Definitions

Jusqu'à présent, les structs que nous avons définis contiennent tous des types propriétaires. Nous pouvons définir des structs pour contenir des références, mais dans ce cas, nous devons ajouter une annotation de durée de vie à chaque référence dans la définition du struct. La Liste 10-24 présente un struct nommé `ImportantExcerpt` qui contient une slice de chaîne de caractères.

Nom de fichier : `src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
       .split('.')
       .next()
       .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

Liste 10-24: Un struct qui contient une référence, nécessitant une annotation de durée de vie

Ce struct a le seul champ `part` qui contient une slice de chaîne de caractères, qui est une référence \[2\]. Comme pour les types de données génériques, nous déclarons le nom du paramètre de durée de vie générique entre crochets angulaires après le nom du struct afin que nous puissions utiliser le paramètre de durée de vie dans le corps de la définition du struct \[1\]. Cette annotation signifie qu'une instance de `ImportantExcerpt` ne peut pas avoir une durée de vie supérieure à celle de la référence qu'elle contient dans son champ `part`.

La fonction `main` ici crée une instance du struct `ImportantExcerpt` \[5\] qui contient une référence à la première phrase de la `String` \[4\] propriété de la variable `novel` \[3\]. Les données dans `novel` existent avant la création de l'instance `ImportantExcerpt`. De plus, `novel` ne sort pas de portée avant que l'instance `ImportantExcerpt` ne sorte de portée, donc la référence dans l'instance `ImportantExcerpt` est valide.
