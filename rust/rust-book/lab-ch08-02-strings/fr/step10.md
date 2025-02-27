# Slicing Strings

Indexer une chaîne de caractères est souvent une mauvaise idée car il n'est pas clair quel devrait être le type de retour de l'opération d'indexation de chaîne : une valeur d'octet, un caractère, une grappe de caractères ou une tranche de chaîne. Si vous avez vraiment besoin d'utiliser des indices pour créer des tranches de chaîne, donc, Rust vous demande d'être plus précis.

Plutôt qu'indexer en utilisant `[]` avec un seul nombre, vous pouvez utiliser `[]` avec une plage pour créer une tranche de chaîne contenant des octets particuliers :

```rust
let hello = "Здравствуйте";

let s = &hello[0..4];
```

Ici, `s` sera un `&str` qui contient les quatre premiers octets de la chaîne. Plus tôt, nous avons mentionné que chacun de ces caractères était de deux octets, ce qui signifie que `s` sera `Зд`.

Si nous essayions de découper seulement une partie des octets d'un caractère avec quelque chose comme `&hello[0..1]`, Rust planterait à l'exécution de la même manière qu'il le ferait si un indice invalide était consulté dans un vecteur :

```rust
thread 'main' panicked at 'byte index 1 is not a char boundary;
it is inside 'З' (bytes 0..2) of `Здравствуйте`', src/main.rs:4:14
```

Vous devriez faire preuve de prudence lorsqu'il s'agit de créer des tranches de chaîne avec des plages, car cela peut faire planter votre programme.
