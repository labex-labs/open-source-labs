# Itérer sur les lignes avec la méthode lines

Rust possède une méthode pratique pour gérer l'itération ligne par ligne de chaînes de caractères, nommé `lines` de manière commode, qui fonctionne comme indiqué dans le listing 12-17. Notez que cela ne compilera pas encore.

Nom de fichier : `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // faire quelque chose avec line
    }
}
```

Listing 12-17 : Itération sur chaque ligne de `contents`

La méthode `lines` renvoie un itérateur. Nous parlerons en détail des itérateurs au chapitre 13, mais rappelez-vous que vous avez vu cette manière d'utiliser un itérateur dans le listing 3-5, où nous avons utilisé une boucle `for` avec un itérateur pour exécuter du code sur chaque élément d'une collection.
