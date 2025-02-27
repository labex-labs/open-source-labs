# Rückgabe von echten HTML

Implementieren wir die Funktionalität, um mehr als eine leere Seite zurückzugeben. Erstellen Sie die neue Datei _hello.html_ im Stammverzeichnis Ihres Projekts, nicht im `src`-Verzeichnis. Sie können beliebiges HTML eingeben; Listing 20-4 zeigt eine Möglichkeit.

Dateiname: `hello.html`

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

Listing 20-4: Eine Beispiel-HTML-Datei, die in einer Antwort zurückgegeben wird

Dies ist eine minimale HTML5-Dokument mit einem Überschrift und etwas Text. Um dies vom Server zurückzugeben, wenn eine Anfrage empfangen wird, werden wir `handle_connection` wie in Listing 20-5 ändern, um die HTML-Datei zu lesen, sie als Körper zur Antwort hinzuzufügen und zu senden.

Dateiname: `src/main.rs`

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

Listing 20-5: Senden der Inhalte von _hello.html_ als Körper der Antwort

Wir haben `fs` zum `use`-Statement hinzugefügt, um das Dateisystemmodul der Standardbibliothek in den Gültigkeitsbereich zu bringen \[1\]. Der Code zum Lesen der Inhalte einer Datei in eine Zeichenfolge sollte Ihnen vertraut sein; wir haben ihn verwendet, als wir die Inhalte einer Datei für unser I/O-Projekt in Listing 12-4 gelesen haben.

Als nächstes verwenden wir `format!`, um die Dateiinhalte als Körper der Erfolgsantwort hinzuzufügen \[2\]. Um eine gültige HTTP-Antwort zu gewährleisten, fügen wir den `Content-Length`-Header hinzu, der auf die Größe unseres Antwortkörpers, in diesem Fall die Größe von `hello.html`, gesetzt wird.

Führen Sie diesen Code mit `cargo run` aus und laden Sie _127.0.0.1:7878_ in Ihrem Browser; Sie sollten Ihr HTML gerendert sehen!

Derzeit ignorieren wir die Anfragedaten in `http_request` und senden einfach die Inhalte der HTML-Datei unbedingt zurück. Das bedeutet, dass Sie, wenn Sie versuchen, _127.0.0.1:7878/something-else_ in Ihrem Browser anzufragen, immer noch dieselbe HTML-Antwort erhalten. Momentan ist unser Server sehr eingeschränkt und macht nicht das, was die meisten Webserver tun. Wir möchten unsere Antworten je nach Anfrage anpassen und nur die HTML-Datei für eine gut geformte Anfrage an _/_ zurücksenden.
