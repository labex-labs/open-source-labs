# Validieren der Anfrage und selektiv reagieren

Im Moment gibt unser Webserver das HTML in der Datei zurück, egal was der Client angefordert hat. Fügen wir die Funktionalität hinzu, um zu überprüfen, ob der Browser _/_ anfordert, bevor wir die HTML-Datei zurückgeben, und geben einen Fehler zurück, wenn der Browser etwas anderes anfordert. Dazu müssen wir `handle_connection` ändern, wie in Listing 20-6 gezeigt. Dieser neue Code überprüft den Inhalt der empfangenen Anfrage gegen das, was wir wissen, wie eine Anfrage an _/_ aussieht, und fügt `if`- und `else`-Blöcke hinzu, um Anfragen unterschiedlich zu behandeln.

Dateiname: `src/main.rs`

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

Listing 20-6: Andere Behandlung von Anfragen an _/_ als von anderen Anfragen

Wir werden nur die erste Zeile der HTTP-Anfrage betrachten, daher lesen wir nicht die gesamte Anfrage in einen Vektor, sondern rufen `next` auf, um das erste Element aus dem Iterator zu erhalten \[1\]. Die erste `unwrap` kümmert sich um die `Option` und stoppt das Programm, wenn der Iterator keine Elemente hat. Die zweite `unwrap` behandelt das `Result` und hat die gleiche Wirkung wie die `unwrap`, die in der `map` in Listing 20-2 hinzugefügt wurde.

Als nächstes überprüfen wir die `request_line`, um zu sehen, ob sie der Anfragezeile einer GET-Anfrage zum _/_-Pfad entspricht \[2\]. Wenn ja, gibt der `if`-Block die Inhalte unserer HTML-Datei zurück.

Wenn die `request_line` _nicht_ der GET-Anfrage zum _/_-Pfad entspricht, bedeutet dies, dass wir eine andere Anfrage erhalten haben. Wir werden in einem Moment Code zum `else`-Block hinzufügen \[3\], um auf alle anderen Anfragen zu reagieren.

Führen Sie diesen Code jetzt aus und fragen Sie _127.0.0.1:7878_ an; Sie sollten das HTML in _hello.html_ erhalten. Wenn Sie eine andere Anfrage stellen, wie _127.0.0.1:7878/something-else_, erhalten Sie einen Verbindungsfehler wie die, die Sie beim Ausführen des Codes in Listing 20-1 und Listing 20-2 gesehen haben.

Nun fügen wir den Code in Listing 20-7 zum `else`-Block hinzu, um eine Antwort mit dem Statuscode 404 zurückzugeben, was signalisiert, dass der Inhalt für die Anfrage nicht gefunden wurde. Wir werden auch etwas HTML für eine Seite zurückgeben, die im Browser gerendert werden soll, um die Antwort an den Endbenutzer anzuzeigen.

Dateiname: `src/main.rs`

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

Listing 20-7: Antworten mit Statuscode 404 und einer Fehlerseite, wenn etwas anderes als _/_ angefordert wurde

Hier hat unsere Antwort eine Statuszeile mit dem Statuscode 404 und dem Grundtext `NOT FOUND` \[1\]. Der Körper der Antwort wird das HTML in der Datei _404.html_ sein \[1\]. Sie müssen eine _404.html_-Datei neben _hello.html_ für die Fehlerseite erstellen; Sie können wieder beliebiges HTML verwenden oder das Beispiel-HTML in Listing 20-8 verwenden.

Dateiname: `404.html`

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

Listing 20-8: Beispielinhalt für die Seite, die mit jeder 404-Antwort zurückgeschickt wird

Mit diesen Änderungen führen Sie Ihren Server erneut aus. Das Anfordern von _127.0.0.1:7878_ sollte die Inhalte von _hello.html_ zurückgeben, und jede andere Anfrage, wie _127.0.0.1:7878/foo_, sollte das Fehler-HTML aus _404.html_ zurückgeben.
