# Testen

Wir wissen, dass das Testen für jedes Softwarestück unverzichtbar ist! Rust bietet eine erstklassige Unterstützung für Unit- und Integrationstests ([siehe dieses Kapitel](https://doc.rust-lang.org/book/ch11-00-testing.html) in der TRPL).

Aus den verlinkten Testkapiteln oben sehen wir, wie man Unit- und Integrationstests schreibt. Organisationell können wir Unit-Tests in den Modulen platzieren, die sie testen, und Integrationstests im eigenen `tests/`-Verzeichnis:

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

Jede Datei in `tests` ist ein separater [Integrationstest](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests), d.h. ein Test, der das Ziel hat, Ihre Bibliothek so zu testen, als würde sie von einem abhängigen Crate aufgerufen werden.

Das Testkapitel geht auf die drei verschiedenen Teststile ein: Unit, Doc und Integration.

`cargo` bietet natürlich einen einfachen Weg, alle Ihre Tests auszuführen!

```shell
$ cargo test
```

Sie sollten eine Ausgabe wie diese sehen:

```shell

```

Sie können auch Tests ausführen, deren Name einem Muster entspricht:

```shell
$ cargo test test_foo
```

```shell

```

Ein Wort der Vorsicht: Cargo kann mehrere Tests gleichzeitig ausführen, also stellen Sie sicher, dass sie nicht miteinander konkurrieren.

Ein Beispiel dafür, dass diese Konkurrenz zu Problemen führt, ist, wenn zwei Tests in eine Datei schreiben, wie unten:

```rust
#[cfg(test)]
mod tests {
    // Importiere die erforderlichen Module
    use std::fs::OpenOptions;
    use std::io::Write;

    // Dieser Test schreibt in eine Datei
    #[test]
    fn test_file() {
        // Öffnet die Datei ferris.txt oder erstellt sie, wenn sie nicht existiert.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Fehler beim Öffnen von ferris.txt");

        // Druckt "Ferris" 5 Mal.
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
             .expect("Konnte nicht in ferris.txt schreiben");
        }
    }

    // Dieser Test versucht, in die gleiche Datei zu schreiben
    #[test]
    fn test_file_also() {
        // Öffnet die Datei ferris.txt oder erstellt sie, wenn sie nicht existiert.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Fehler beim Öffnen von ferris.txt");

        // Druckt "Corro" 5 Mal.
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
             .expect("Konnte nicht in ferris.txt schreiben");
        }
    }
}
```

Obwohl der Zweck darin besteht, Folgendes zu erhalten:

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

Was tatsächlich in `ferris.txt` geschrieben wird, ist dies:

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
