# Simulating a Slow Request

Nous allons examiner comment une requête à traitement lent peut affecter les autres requêtes envoyées à notre implémentation de serveur actuelle. Le Listing 20-10 implémente la gestion d'une requête à _/sleep_ avec une réponse simulée lente qui forcera le serveur à dormir pendant cinq secondes avant de répondre.

Nom de fichier : `src/main.rs`

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) = 1 match &request_line[..] {
      2 "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
      3 "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
      4 _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    --snip--
}
```

Listing 20-10 : Simulation d'une requête lente en dormant pendant cinq secondes

Nous avons changé d'`if` à `match` maintenant que nous avons trois cas \[1\]. Nous devons explicitement matcher sur une tranche de `request_line` pour effectuer une correspondance de motifs avec les valeurs littérales de chaîne ; `match` ne fait pas de référencement et de déréférencement automatique, comme la méthode d'égalité le fait.

Le premier bras \[2\] est le même que le bloc `if` du Listing 20-9. Le second bras \[3\] correspond à une requête à _/sleep_. Lorsque cette requête est reçue, le serveur dormira pendant cinq secondes avant de générer la page HTML réussie. Le troisième bras \[4\] est le même que le bloc `else` du Listing 20-9.

Vous pouvez voir à quel point notre serveur est primitif : des bibliothèques réelles géreraient la reconnaissance de multiples requêtes de manière beaucoup moins verbeuse!

Démarrez le serveur avec `cargo run`. Ensuite, ouvrez deux fenêtres de navigateur : l'une pour *http://127.0.0.1:7878* et l'autre pour *http://127.0.0.1:7878/sleep*. Si vous entrez l'URI _/_ plusieurs fois, comme auparavant, vous verrez qu'elle répondra rapidement. Mais si vous entrez _/sleep_ puis chargez _/_, vous verrez que _/_ attendra jusqu'à ce que `sleep` ait dormi pendant ses cinq secondes complètes avant de se charger.

Il existe plusieurs techniques que nous pourrions utiliser pour éviter que les requêtes ne se bloquent derrière une requête lente ; celle que nous allons implémenter est un pool de threads.
