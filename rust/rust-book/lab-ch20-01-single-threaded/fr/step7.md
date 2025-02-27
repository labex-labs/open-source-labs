# Validation de la requête et réponse sélective

En ce moment, notre serveur web renvoie le HTML contenu dans le fichier quoi que le client ait demandé. Ajoutons une fonctionnalité pour vérifier que le navigateur demande _/_ avant de renvoyer le fichier HTML, et renvoyer une erreur si le navigateur demande autre chose. Pour cela, nous devons modifier `handle_connection`, comme indiqué dans la Liste 20-6. Ce nouveau code vérifie le contenu de la requête reçue par rapport à ce que nous savons qu'une requête à _/_ ressemble et ajoute des blocs `if` et `else` pour traiter les requêtes différemment.

Nom du fichier : `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
      .lines()
      .next()
      .unwrap()
      .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // some other request
    }
}
```

Liste 20-6 : Traitement des requêtes à _/_ différemment des autres requêtes

Nous allons seulement examiner la première ligne de la requête HTTP, donc au lieu de lire toute la requête dans un vecteur, nous appelons `next` pour obtenir le premier élément de l'itérateur \[1\]. Le premier `unwrap` gère l'`Option` et arrête le programme si l'itérateur n'a aucun élément. Le second `unwrap` gère le `Result` et a le même effet que l'`unwrap` qui était dans la fonction `map` ajoutée dans la Liste 20-2.

Ensuite, nous vérifions la `request_line` pour voir si elle est égale à la ligne de requête d'une requête GET vers le chemin _/_ \[2\]. Si c'est le cas, le bloc `if` renvoie le contenu de notre fichier HTML.

Si la `request_line` n'est _pas_ égale à la requête GET vers le chemin _/_, cela signifie que nous avons reçu une autre requête. Nous ajouterons du code au bloc `else` \[3\] dans un instant pour répondre à toutes les autres requêtes.

Exécutez maintenant ce code et demandez _127.0.0.1:7878_ ; vous devriez obtenir le HTML contenu dans _hello.html_. Si vous effectuez n'importe quelle autre requête, telle que _127.0.0.1:7878/something-else_, vous obtiendrez une erreur de connexion comme celles que vous avez vues en exécutant le code dans la Liste 20-1 et la Liste 20-2.

Maintenant, ajoutons le code de la Liste 20-7 au bloc `else` pour renvoyer une réponse avec le code d'état 404, qui indique que le contenu de la requête n'a pas été trouvé. Nous renverrons également un peu de HTML pour une page à afficher dans le navigateur indiquant la réponse à l'utilisateur final.

Nom du fichier : `src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Liste 20-7 : Renvoyer un code d'état 404 et une page d'erreur si une autre chose que _/_ est demandée

Ici, notre réponse a une ligne d'état avec le code d'état 404 et la phrase de raison `NOT FOUND` \[1\]. Le corps de la réponse sera le HTML contenu dans le fichier _404.html_ \[1\]. Vous devrez créer un fichier _404.html_ à côté de _hello.html_ pour la page d'erreur ; n'hésitez pas à utiliser tout le HTML que vous voulez, ou utilisez l'HTML exemple dans la Liste 20-8.

Nom du fichier : `404.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Oops!</h1>
    <p>Sorry, I don't know what you're asking for.</p>
  </body>
</html>
```

Liste 20-8 : Contenu d'échantillonnage pour la page à renvoyer avec toute réponse 404

Avec ces modifications, exécutez à nouveau votre serveur. Demander _127.0.0.1:7878_ devrait renvoyer le contenu de _hello.html_, et n'importe quelle autre requête, comme _127.0.0.1:7878/foo_, devrait renvoyer le HTML d'erreur contenu dans _404.html_.
