# Retourner du HTML réel

Implémentons la fonctionnalité pour retourner plus qu'une page blanche. Créez le nouveau fichier _hello.html_ dans le répertoire racine de votre projet, pas dans le répertoire `src`. Vous pouvez entrer tout le HTML que vous voulez ; la Liste 20-4 montre une possibilité.

Nom du fichier : `hello.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Hello!</h1>
    <p>Hi from Rust</p>
  </body>
</html>
```

Liste 20-4 : Un fichier HTML exemple à retourner dans une réponse

Il s'agit d'un document HTML5 minimal avec un titre et quelques textes. Pour le retourner depuis le serveur lorsqu'une requête est reçue, nous modifierons `handle_connection` comme indiqué dans la Liste 20-5 pour lire le fichier HTML, l'ajouter au corps de la réponse et l'envoyer.

Nom du fichier : `src/main.rs`

```rust
use std::{
  1 fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
     .lines()
     .map(|result| result.unwrap())
     .take_while(|line|!line.is_empty())
     .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

  2 let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Liste 20-5 : Envoi du contenu de _hello.html_ comme corps de la réponse

Nous avons ajouté `fs` à l'instruction `use` pour inclure le module de système de fichiers de la bibliothèque standard dans la portée \[1\]. Le code pour lire le contenu d'un fichier en tant que chaîne devrait vous paraître familier ; nous l'avons utilisé lorsque nous avons lu le contenu d'un fichier pour notre projet d'E/S dans la Liste 12-4.

Ensuite, nous utilisons `format!` pour ajouter le contenu du fichier comme corps de la réponse de succès \[2\]. Pour assurer une réponse HTTP valide, nous ajoutons l'en-tête `Content-Length` qui est défini sur la taille de notre corps de réponse, dans ce cas la taille de `hello.html`.

Exécutez ce code avec `cargo run` et chargez _127.0.0.1:7878_ dans votre navigateur ; vous devriez voir votre HTML affiché!

Actuellement, nous ignorons les données de la requête dans `http_request` et envoyons simplement le contenu du fichier HTML sans condition. Cela signifie que si vous essayez de demander _127.0.0.1:7878/something-else_ dans votre navigateur, vous recevrez toujours cette même réponse HTML. Pour l'instant, notre serveur est très limité et ne fait pas ce que la plupart des serveurs web font. Nous voulons personnaliser nos réponses en fonction de la requête et n'envoyer le fichier HTML que pour une requête correctement formée à _/_.
