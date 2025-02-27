# Écrire une réponse

Nous allons implémenter l'envoi de données en réponse à une demande du client. Les réponses ont le format suivant :

    Version-HTTP Code-État Phrase-Raison CRLF
    en-têtes CRLF
    corps du message

La première ligne est une _ligne d'état_ qui contient la version HTTP utilisée dans la réponse, un code d'état numérique qui résume le résultat de la demande et une phrase de raison qui fournit une description textuelle du code d'état. Après la séquence CRLF viennent tous les en-têtes, une autre séquence CRLF et le corps de la réponse.

Voici un exemple de réponse qui utilise la version HTTP 1.1, a un code d'état de 200, une phrase de raison OK, aucun en-tête et aucun corps :

```rust
HTTP/1.1 200 OK\r\n\r\n
```

Le code d'état 200 est la réponse de succès standard. Le texte est une petite réponse HTTP réussie. Écrivons cela dans le flux en tant que réponse à une demande réussie! Dans la fonction `handle_connection`, supprimez l'instruction `println!` qui affichait les données de la requête et remplacez-la par le code de la Liste 20-3.

Nom du fichier : `src/main.rs`

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
     .lines()
     .map(|result| result.unwrap())
     .take_while(|line|!line.is_empty())
     .collect();

  1 let response = "HTTP/1.1 200 OK\r\n\r\n";

  2 stream.write_all(response.3 as_bytes()).unwrap();
}
```

Liste 20-3 : Écriture d'une petite réponse HTTP réussie dans le flux

La première nouvelle ligne définit la variable `response` qui contient les données du message de succès \[1\]. Ensuite, nous appelons `as_bytes` sur notre `response` pour convertir les données de chaîne en octets \[3\]. La méthode `write_all` sur `stream` prend un `&[u8]` et envoie directement ces octets sur la connexion \[2\]. Comme l'opération `write_all` pourrait échouer, nous utilisons `unwrap` sur tout résultat d'erreur comme auparavant. Encore une fois, dans une application réelle, vous ajouteriez la gestion des erreurs ici.

Avec ces modifications, exécutons notre code et effectuons une demande. Nous n'affichons plus aucune donnée dans le terminal, donc nous ne verrons aucun résultat autre que la sortie de Cargo. Lorsque vous chargez _127.0.0.1:7878_ dans un navigateur web, vous devriez obtenir une page blanche au lieu d'une erreur. Vous venez d'écrire manuellement la réception d'une requête HTTP et l'envoi d'une réponse!
