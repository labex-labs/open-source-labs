# Grouping Configuration Values

Wir können einen weiteren kleinen Schritt unternehmen, um die `parse_config`-Funktion weiter zu verbessern. Momentan geben wir ein Tuple zurück, aber brechen dieses dann sofort wieder in einzelne Teile auf. Dies ist ein Anzeichen dafür, dass wir vielleicht noch nicht die richtige Abstraktion haben.

Ein weiterer Indikator, der zeigt, dass es Verbesserungspotential gibt, ist der `config`-Teil von `parse_config`, was darauf hindeutet, dass die beiden Werte, die wir zurückgeben, zusammenhängen und beide Teil eines Konfigurationswerts sind. Wir vermitteln diese Bedeutung momentan nicht in der Struktur der Daten, außer indem wir die beiden Werte in ein Tuple gruppieren; stattdessen legen wir die beiden Werte in eine Struktur und geben jedem Strukturfeld einen aussagekräftigen Namen. Dadurch wird es zukünftigen Wartenden dieses Codes einfacher, zu verstehen, wie die verschiedenen Werte miteinander zusammenhängen und was ihr Zweck ist.

Listing 12-6 zeigt die Verbesserungen an der `parse_config`-Funktion.

Dateiname: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Searching for {}", 2 config.query);
    println!("In file {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
       .expect("Should have been able to read the file");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

Listing 12-6: Refactoring `parse_config` to return an instance of a `Config` struct

Wir haben eine Struktur namens `Config` hinzugefügt, die Felder namens `query` und `file_path` definiert \[5\]. Die Signatur von `parse_config` gibt jetzt an, dass sie einen `Config`-Wert zurückgibt \[6\]. Im Körper von `parse_config`, wo wir früher String-Slices zurückgaben, die auf `String`-Werte in `args` verweisen, definieren wir jetzt `Config`, um eigene `String`-Werte zu enthalten. Die Variable `args` in `main` ist der Besitzer der Argumentwerte und lässt die `parse_config`-Funktion nur darauf zugreifen, was bedeutet, dass `Config` die Werte in `args` nicht besitzen darf, um die Rust-Borrowing-Regeln nicht zu verletzen.

Es gibt mehrere Möglichkeiten, wie wir die `String`-Daten verwalten könnten; die einfachste, wenn auch etwas ineffiziente, Möglichkeit ist, die `clone`-Methode auf den Werten aufzurufen \[7\] \[8\]. Dies wird eine vollständige Kopie der Daten für die `Config`-Instanz erzeugen, was mehr Zeit und Speicher benötigt als das Speichern einer Referenz auf die String-Daten. Clonen der Daten macht unseren Code jedoch sehr einfach, da wir die Lebensdauer der Referenzen nicht verwalten müssen; in dieser Situation ist es eine lohnende Kompromissberechnung, etwas Leistung aufzuopfern, um die Einfachheit zu gewinnen.

> **The Trade-Offs of Using clone**
>
> Viele Rust-Entwickler neigen dazu, `clone` zu vermeiden, um Besitzprobleme zu beheben, wegen seiner Laufzeitkosten. Im Kapitel 13 lernen Sie, wie Sie in diesem Typ von Situationen effizientere Methoden verwenden können. Aber für jetzt ist es in Ordnung, ein paar Strings zu kopieren, um Fortschritte zu machen, da Sie diese Kopien nur einmal machen und Ihre Dateipfad- und Suchzeichenfolge sehr klein sind. Es ist besser, ein funktionierendes, etwas ineffizientes Programm zu haben, als zu versuchen, den Code bei der ersten Überarbeitung zu hyperoptimieren. Wenn Sie mehr Erfahrung mit Rust sammeln, wird es einfacher, mit der effizientesten Lösung zu beginnen, aber für jetzt ist es völlig in Ordnung, `clone` aufzurufen.

Wir haben `main` aktualisiert, sodass es die von `parse_config` zurückgegebene `Config`-Instanz in eine Variable namens `config` platziert \[1\], und wir haben den Code aktualisiert, der zuvor die getrennten `query`- und `file_path`-Variablen verwendete, sodass er jetzt die Felder auf der `Config`-Struktur verwendet \[2\] \[3\] \[4\].

Jetzt vermittelt unser Code deutlicher, dass `query` und `file_path` zusammenhängen und dass ihr Zweck darin besteht, die Konfiguration zu bestimmen, wie das Programm arbeiten wird. Jeder Code, der diese Werte verwendet, weiß, sie in der `config`-Instanz in den Feldern zu finden, die nach ihrem Zweck benannt sind.
