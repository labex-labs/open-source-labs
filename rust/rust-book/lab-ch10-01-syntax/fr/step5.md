# Dans les définitions d'enums

Comme nous l'avons fait avec les structs, nous pouvons définir des enums pour stocker des types de données génériques dans leurs variantes. Revoyons l'enum `Option<T>` que fournit la bibliothèque standard, que nous avons utilisé au Chapitre 6 :

```rust
enum Option<T> {
    Some(T),
    None,
}
```

Cette définition devrait désormais avoir plus de sens pour vous. Comme vous pouvez le voir, l'enum `Option<T>` est générique sur le type `T` et a deux variantes : `Some`, qui stocke une valeur du type `T`, et une variante `None` qui ne stocke aucune valeur. En utilisant l'enum `Option<T>`, nous pouvons exprimer le concept abstrait d'une valeur optionnelle, et parce que `Option<T>` est générique, nous pouvons utiliser cette abstraction peu importe le type de la valeur optionnelle.

Les enums peuvent également utiliser plusieurs types génériques. La définition de l'enum `Result` que nous avons utilisée au Chapitre 9 en est un exemple :

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

L'enum `Result` est générique sur deux types, `T` et `E`, et a deux variantes : `Ok`, qui stocke une valeur du type `T`, et `Err`, qui stocke une valeur du type `E`. Cette définition facilite l'utilisation de l'enum `Result` partout où nous avons une opération qui peut réussir (retourner une valeur d'un certain type `T`) ou échouer (retourner une erreur d'un certain type `E`). En fait, c'est ce que nous avons utilisé pour ouvrir un fichier dans la Liste 9-3, où `T` a été remplacé par le type `std::fs::File` lorsque le fichier a été ouvert avec succès et `E` a été remplacé par le type `std::io::Error` lorsqu'il y a eu des problèmes à l'ouverture du fichier.

Lorsque vous reconnaissez des situations dans votre code avec plusieurs définitions de struct ou d'enum qui ne diffèrent que par les types des valeurs qu'elles stockent, vous pouvez éviter la duplication en utilisant des types génériques à la place.
