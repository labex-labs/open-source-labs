# Schreiben eines fehlgeschlagenen Tests für die case-insensitive-Suchfunktion

Wir fügen zunächst eine neue `search_case_insensitive`-Funktion hinzu, die aufgerufen wird, wenn die Umgebungsvariable einen Wert hat. Wir werden weiterhin den TDD-Prozess befolgen, also ist der erste Schritt wiederum, einen fehlgeschlagenen Test zu schreiben. Wir fügen einen neuen Test für die neue `search_case_insensitive`-Funktion hinzu und benennen unseren alten Test von `one_result` in `case_sensitive` um, um die Unterschiede zwischen den beiden Tests zu verdeutlichen, wie in Listing 12-20 gezeigt.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

Listing 12-20: Hinzufügen eines neuen fehlgeschlagenen Tests für die case-insensitive-Funktion, die wir hinzufügen werden

Beachten Sie, dass wir auch den `Inhalt` des alten Tests bearbeitet haben. Wir haben eine neue Zeile mit dem Text `"Duct tape."` hinzugefügt, wobei der Buchstabe _D_ groß geschrieben ist, der nicht mit der Abfrage `"duct"` übereinstimmen sollte, wenn wir in einer case-sensitive-Manner suchen. Die Änderung des alten Tests auf diese Weise hilft sicherzustellen, dass wir die case-sensitive-Suchfunktionalität, die wir bereits implementiert haben, nicht versehentlich brechen. Dieser Test sollte jetzt bestehen und sollte weiterhin bestehen, während wir an der case-insensitive-Suche arbeiten.

Der neue Test für die case-_insensitive_-Suche verwendet `"rUsT"` als Abfrage. In der `search_case_insensitive`-Funktion, die wir hinzufügen werden, sollte die Abfrage `"rUsT"` der Zeile mit dem Text `"Rust:"` mit einem großen _R_ entsprechen und der Zeile `"Trust me."` entsprechen, obwohl beide eine andere Groß-/Kleinschreibung als die Abfrage haben. Dies ist unser fehlgeschlagener Test, und er wird fehlschlagen, weil wir die `search_case_insensitive`-Funktion noch nicht definiert haben. Fügen Sie gerne eine Skelett-Implementierung hinzu, die immer einen leeren Vektor zurückgibt, ähnlich wie wir es für die `search`-Funktion in Listing 12-16 getan haben, um zu sehen, dass der Test kompiliert und fehlschlägt.
