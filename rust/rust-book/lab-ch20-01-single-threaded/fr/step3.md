# Lecture de la requête

Implémentons la fonctionnalité pour lire la requête envoyée par le navigateur! Pour séparer les préoccupations liées à la première étape consistant à obtenir une connexion et à celle consistant à prendre des mesures avec cette connexion, nous allons commencer une nouvelle fonction pour traiter les connexions. Dans cette nouvelle fonction `handle_connection`, nous allons lire les données du flux TCP et les imprimer pour voir les données envoyées par le navigateur. Modifions le code pour qu'il ressemble à la Liste 20-2.

Nom du fichier : `src/main.rs`

```rust
1 use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
  3 let buf_reader = BufReader::new(&mut stream);
  4 let http_request: Vec<_> = buf_reader
      5.lines()
      6.map(|result| result.unwrap())
      7.take_while(|line|!line.is_empty())
       .collect();

  8 println!("Request: {:#?}", http_request);
}
```

Liste 20-2 : Lecture du `TcpStream` et impression des données

Nous importons `std::io::prelude` et `std::io::BufReader` pour avoir accès à des traits et des types qui nous permettent de lire et d'écrire dans le flux \[1\]. Dans la boucle `for` de la fonction `main`, au lieu d'imprimer un message indiquant que nous avons établi une connexion, nous appelons maintenant la nouvelle fonction `handle_connection` et lui passons le `stream` \[2\].

Dans la fonction `handle_connection`, nous créons une nouvelle instance de `BufReader` qui encapsule une référence mutable au `stream` \[3\]. `BufReader` ajoute un buffering en gérant les appels aux méthodes du trait `std::io::Read` pour nous.

Nous créons une variable nommée `http_request` pour collecter les lignes de la requête que le navigateur envoie à notre serveur. Nous indiquons que nous souhaitons collecter ces lignes dans un vecteur en ajoutant l'annotation de type `Vec<_>` \[4\].

`BufReader` implémente le trait `std::io::BufRead`, qui fournit la méthode `lines` \[5\]. La méthode `lines` renvoie un itérateur de `Result<String, std::io::Error>` en divisant le flux de données chaque fois qu'elle voit un octet de nouvelle ligne. Pour obtenir chaque `String`, nous appliquons une fonction de transformation et utilisons `unwrap` sur chaque `Result` \[6\]. Le `Result` peut être une erreur si les données ne sont pas de la forme UTF-8 valide ou s'il y a eu un problème lors de la lecture du flux. Encore une fois, un programme de production devrait gérer ces erreurs de manière plus élégante, mais nous choisissons de stopper le programme en cas d'erreur pour la simplicité.

Le navigateur indique la fin d'une requête HTTP en envoyant deux caractères de nouvelle ligne l'un après l'autre, donc pour obtenir une seule requête à partir du flux, nous prenons les lignes jusqu'à ce que nous obtenions une ligne vide \[7\]. Une fois que nous avons collecté les lignes dans le vecteur, nous les imprimons en utilisant un formatage de débogage agréable \[8\] pour pouvoir examiner les instructions que le navigateur web envoie à notre serveur.

Essayons ce code! Démarrez le programme et effectuez à nouveau une requête dans un navigateur web. Notez que nous obtiendrons toujours une page d'erreur dans le navigateur, mais la sortie de notre programme dans le terminal ressemblera maintenant à ceci :

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello`
Request: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0)
Gecko/20100101 Firefox/99.0",
    "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navigate",
    "Sec-Fetch-Site: none",
    "Sec-Fetch-User:?1",
    "Cache-Control: max-age=0",
]
```

Selon votre navigateur, vous pouvez obtenir une sortie légèrement différente. Maintenant que nous imprimons les données de la requête, nous pouvons voir pourquoi nous obtenons plusieurs connexions à partir d'une seule requête de navigateur en examinant le chemin après `GET` dans la première ligne de la requête. Si les connexions répétées demandent toutes _/_, nous savons que le navigateur essaie de récupérer _/_ plusieurs fois parce qu'il ne reçoit pas de réponse de notre programme.

Analysons ces données de requête pour comprendre ce que le navigateur demande à notre programme.
