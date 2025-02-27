# Handling Errors Returned from run in main

Nous vérifierons les erreurs et les gérerons en utilisant une technique similaire à celle que nous avons utilisée avec `Config::build` dans le Listing 12-10, mais avec une légère différence :

Nom du fichier : `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

Nous utilisons `if let` plutôt que `unwrap_or_else` pour vérifier si `run` renvoie une valeur `Err` et pour appeler `process::exit(1)` si c'est le cas. La fonction `run` ne renvoie pas une valeur que nous voulons `unwrap` de la même manière que `Config::build` renvoie l'instance `Config`. Comme `run` renvoie `()` dans le cas de réussite, nous n'avons besoin que de détecter une erreur, donc nous n'avons pas besoin que `unwrap_or_else` renvoie la valeur déballée, qui ne serait que `()`.

Le corps des fonctions `if let` et `unwrap_or_else` est le même dans les deux cas : nous affichons l'erreur et sortons.
