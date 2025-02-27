# Ein langsames Anforderung simulieren

Wir werden uns ansehen, wie eine langsam verarbeitete Anforderung andere Anforderungen an unsere aktuelle Serverimplementierung beeinflussen kann. Listing 20-10 implementiert das Behandeln einer Anforderung an _/sleep_ mit einer simulierten langsamen Antwort, die dazu führt, dass der Server fünf Sekunden schläft, bevor er antwortet.

Dateiname: `src/main.rs`

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

Listing 20-10: Ein langsames Anforderung simulieren, indem fünf Sekunden geschlafen wird

Wir haben von `if` zu `match` gewechselt, da wir jetzt drei Fälle haben \[1\]. Wir müssen explizit auf einen Schnitt von `request_line` matchen, um mit den Stringliteral-Werten zu musterabgleichen; `match` führt keine automatische Referenzierung und Dereferenzierung durch, wie die Gleichheitsmethode es tut.

Der erste Arm \[2\] ist der gleiche wie der `if`-Block aus Listing 20-9. Der zweite Arm \[3\] matcht eine Anforderung an _/sleep_. Wenn diese Anforderung empfangen wird, wird der Server fünf Sekunden schlafen, bevor er die erfolgreiche HTML-Seite rendert. Der dritte Arm \[4\] ist der gleiche wie der `else`-Block aus Listing 20-9.

Man kann sehen, wie primitiv unser Server ist: Echte Bibliotheken würden die Erkennung mehrerer Anforderungen auf eine viel weniger umständliche Weise behandeln!

Starten Sie den Server mit `cargo run`. Öffnen Sie dann zwei Browserfenster: eines für *http://127.0.0.1:7878* und das andere für *http://127.0.0.1:7878/sleep*. Wenn Sie die _/_-URI einige Male eingeben, wie zuvor, werden Sie sehen, dass sie schnell antwortet. Aber wenn Sie _/sleep_ eingeben und dann _/_ laden, werden Sie sehen, dass _/_ wartet, bis `sleep` seine volle fünf Sekunden geschlafen hat, bevor es geladen wird.

Es gibt mehrere Techniken, die wir verwenden könnten, um zu vermeiden, dass Anforderungen hinter einer langsamen Anforderung anstecken; die, die wir implementieren werden, ist ein Threadpool.
