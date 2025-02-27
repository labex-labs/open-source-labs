# Das Lesen der Anfrage

Implementieren wir die Funktionalität, um die Anfrage aus dem Browser zu lesen! Um die Aufgaben von erstmalig das Herstellen einer Verbindung und dann das Ausführen von Aktionen mit der Verbindung zu trennen, starten wir eine neue Funktion zur Verarbeitung von Verbindungen. In dieser neuen `handle_connection`-Funktion werden wir Daten aus dem TCP-Strom lesen und ausgeben, damit wir die von dem Browser gesendeten Daten sehen können. Ändern Sie den Code, sodass er wie Listing 20-2 aussieht.

Dateiname: `src/main.rs`

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

Listing 20-2: Lesen aus dem `TcpStream` und Ausgabe der Daten

Wir bringen `std::io::prelude` und `std::io::BufReader` in den Gültigkeitsbereich, um auf Traits und Typen zuzugreifen, die uns ermöglichen, in und aus dem Stream zu lesen und zu schreiben \[1\]. In der `for`-Schleife in der `main`-Funktion geben wir statt einer Nachricht aus, dass wir eine Verbindung hergestellt haben, jetzt die neue `handle_connection`-Funktion aufrufen und dem `stream` übergeben \[2\].

In der `handle_connection`-Funktion erstellen wir eine neue `BufReader`-Instanz, die eine mutabile Referenz auf den `stream` umschließt \[3\]. `BufReader` fügt Puffering hinzu, indem es die Aufrufe an die `std::io::Read`-Trait-Methoden für uns verwaltet.

Wir erstellen eine Variable namens `http_request`, um die Zeilen der Anfrage zu sammeln, die der Browser an unseren Server sendet. Wir geben an, dass wir diese Zeilen in einem Vektor sammeln möchten, indem wir die `Vec<_>`-Typangabe hinzufügen \[4\].

`BufReader` implementiert das `std::io::BufRead`-Trait, das die `lines`-Methode bereitstellt \[5\]. Die `lines`-Methode gibt einen Iterator von `Result<String, std::io::Error>` zurück, indem sie den Datenstrom jedes Mal, wenn sie ein Zeilenumbruch-Byte sieht, aufspaltet. Um jedes `String` zu erhalten, mappen und `unwrap` wir jedes `Result` \[6\]. Das `Result` kann ein Fehler sein, wenn die Daten kein gültiges UTF-8 sind oder wenn es ein Problem beim Lesen aus dem Stream gab. Wiederum sollte ein Produktionsprogramm diese Fehler eleganter behandeln, aber wir wählen, das Programm im Fehlerfall zu stoppen, um es einfacher zu halten.

Der Browser signalisiert das Ende einer HTTP-Anfrage, indem er zwei Zeilenumbrüche nacheinander sendet, daher um eine Anfrage aus dem Stream zu erhalten, nehmen wir Zeilen, bis wir eine Zeile erhalten, die die leere Zeichenkette ist \[7\]. Nachdem wir die Zeilen in den Vektor gesammelt haben, geben wir sie mit einer schönen Debug-Formatierung aus \[8\], sodass wir uns die Anweisungen ansehen können, die der Webbrowser an unseren Server sendet.

Probieren wir diesen Code aus! Starten Sie das Programm und machen Sie erneut eine Anfrage in einem Webbrowser. Beachten Sie, dass wir immer noch eine Fehlerseite im Browser erhalten, aber die Ausgabe unseres Programms in der Konsole sieht jetzt ähnlich aus wie dies:

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

Je nach Browser können Sie leicht unterschiedliche Ausgabe erhalten. Jetzt, da wir die Anfragedaten ausgeben, können wir sehen, warum wir aus einer Browseranfrage mehrere Verbindungen erhalten, indem wir uns den Pfad nach `GET` in der ersten Zeile der Anfrage ansehen. Wenn die wiederholten Verbindungen alle _/_ anfordern, wissen wir, dass der Browser versucht, _/_ wiederholt abzurufen, weil er keine Antwort von unserem Programm erhält.

Zerlegen wir diese Anfragedaten, um zu verstehen, was der Browser von unserem Programm verlangt.
