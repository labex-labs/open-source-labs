# Un peu de refactoring

En ce moment, les blocs `if` et `else` ont beaucoup de répétitions : ils lisent tous les deux des fichiers et écrivent le contenu des fichiers dans le flux. Les seules différences sont la ligne d'état et le nom du fichier. Rendre le code plus concise en extraisant ces différences dans des lignes `if` et `else` séparées qui assigneront les valeurs de la ligne d'état et du nom du fichier à des variables ; nous pourrons ensuite utiliser ces variables de manière inconditionnelle dans le code pour lire le fichier et écrire la réponse. La Liste 20-9 montre le code résultant après avoir remplacé les grands blocs `if` et `else`.

Nom du fichier : `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) =
        if request_line == "GET / HTTP/1.1" {
            ("HTTP/1.1 200 OK", "hello.html")
        } else {
            ("HTTP/1.1 404 NOT FOUND", "404.html")
        };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Liste 20-9 : Refactoring des blocs `if` et `else` pour ne contenir que le code différent entre les deux cas

Maintenant, les blocs `if` et `else` ne renvoient que les valeurs appropriées pour la ligne d'état et le nom du fichier dans un tuple ; nous utilisons ensuite la déstructuration pour assigner ces deux valeurs à `status_line` et `filename` à l'aide d'un motif dans l'instruction `let`, comme discuté au chapitre 18.

Le code précédemment dupliqué est maintenant en dehors des blocs `if` et `else` et utilise les variables `status_line` et `filename`. Cela facilite la compréhension des différences entre les deux cas, et cela signifie que nous n'avons qu'un seul endroit où mettre à jour le code si nous voulons changer la manière dont la lecture du fichier et l'écriture de la réponse fonctionnent. Le comportement du code dans la Liste 20-9 sera le même que celui dans la Liste 20-8.

Génial! Nous avons maintenant un serveur web simple en environ 40 lignes de code Rust qui répond à une demande avec une page de contenu et répond à toutes les autres demandes avec une réponse 404.

En ce moment, notre serveur s'exécute dans un seul fil, ce qui signifie qu'il ne peut servir qu'une demande à la fois. Examinons comment cela peut être un problème en simulant quelques demandes lentes. Ensuite, nous le corrigerons pour que notre serveur puisse gérer plusieurs demandes simultanément.
