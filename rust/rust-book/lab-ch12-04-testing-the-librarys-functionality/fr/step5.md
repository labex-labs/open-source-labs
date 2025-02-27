# Rechercher la requête dans chaque ligne

Ensuite, nous allons vérifier si la ligne actuelle contient notre chaîne de requête. Heureusement, les chaînes ont une méthode pratique appelée `contains` qui le fait pour nous! Ajoutez un appel à la méthode `contains` dans la fonction `search`, comme indiqué dans le listing 12-18. Notez que cela ne compilera toujours pas.

Nom de fichier : `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // faire quelque chose avec line
        }
    }
}
```

Listing 12-18 : Ajout de la fonctionnalité pour voir si la ligne contient la chaîne dans `query`

En ce moment, nous construisons la fonctionnalité. Pour que le code compile, nous devons retourner une valeur dans le corps comme nous l'avons indiqué dans la signature de la fonction.
