# Erstellen benutzerdefinierter Typen für die Validierung

Lassen Sie uns die Idee, das Typsystem von Rust zu verwenden, um sicherzustellen, dass wir einen gültigen Wert haben, einen Schritt weiter verfolgen und uns ansehen, wie wir einen benutzerdefinierten Typ für die Validierung erstellen. Denken Sie sich das Raten-Spiel aus Kapitel 2 zurück, in dem unser Code den Benutzer aufforderte, eine Zahl zwischen 1 und 100 zu erraten. Wir haben nie überprüft, ob der vom Benutzer geratene Wert zwischen diesen Zahlen lag, bevor wir ihn mit unserer Geheimzahl verglichen; wir haben nur überprüft, dass die Vermutung positiv war. In diesem Fall waren die Folgen nicht sehr schlimm: Unsere Ausgabe von "Zu hoch" oder "Zu niedrig" wäre immer noch korrekt. Aber es wäre eine nützliche Verbesserung, den Benutzer zu leiten, auf gültige Vermutungen zu kommen, und unterschiedliches Verhalten zu haben, wenn der Benutzer eine Zahl ausserhalb des Bereichs errät, im Gegensatz zu dem, wenn der Benutzer beispielsweise Buchstaben eingibt.

Eine Möglichkeit, dies zu tun, wäre, die Vermutung als `i32` statt nur als `u32` zu parsen, um potenziell negative Zahlen zuzulassen, und dann eine Prüfung hinzuzufügen, ob die Zahl im Bereich liegt, wie folgt:

Dateiname: `src/main.rs`

```rust
loop {
    --snip--

    let guess: i32 = match guess.trim().parse() {
        Ok(num) => num,
        Err(_) => continue,
    };

    if guess < 1 || guess > 100 {
        println!("The secret number will be between 1 and 100.");
        continue;
    }

    match guess.cmp(&secret_number) {
        --snip--
}
```

Der `if`-Ausdruck prüft, ob unser Wert ausserhalb des Bereichs liegt, informiert den Benutzer über das Problem und ruft `continue` auf, um die nächste Iteration der Schleife zu starten und nach einer weiteren Vermutung zu fragen. Nach dem `if`-Ausdruck können wir mit den Vergleichen zwischen `guess` und der Geheimzahl fortfahren, indem wir wissen, dass `guess` zwischen 1 und 100 liegt.

Dies ist jedoch keine ideale Lösung: Wenn es absolut entscheidend wäre, dass das Programm nur auf Werten zwischen 1 und 100 operiert, und es viele Funktionen mit dieser Anforderung hätte, wäre es lästig, eine solche Prüfung in jeder Funktion durchzuführen (und könnte die Leistung beeinträchtigen).

Stattdessen können wir einen neuen Typ erstellen und die Validierungen in einer Funktion ablegen, um eine Instanz des Typs zu erstellen, anstatt die Validierungen überall zu wiederholen. Auf diese Weise ist es sicher für Funktionen, den neuen Typ in ihren Signaturen zu verwenden und die Werte, die sie erhalten, vertrauensvoll zu verwenden. Listing 9-13 zeigt eine Möglichkeit, einen `Guess`-Typ zu definieren, der nur eine Instanz von `Guess` erstellen wird, wenn die `new`-Funktion einen Wert zwischen 1 und 100 erhält.

Dateiname: `src/lib.rs`

```rust
1 pub struct Guess {
    value: i32,
}

impl Guess {
  2 pub fn new(value: i32) -> Guess {
      3 if value < 1 || value > 100 {
          4 panic!(
                "Guess value must be between 1 and 100, got {}.",
                value
            );
        }

      5 Guess { value }
    }

  6 pub fn value(&self) -> i32 {
        self.value
    }
}
```

Listing 9-13: Ein `Guess`-Typ, der nur mit Werten zwischen 1 und 100 fortfahren wird

Zuerst definieren wir eine Struktur namens `Guess`, die ein Feld namens `value` hat, das eine `i32` enthält \[1\]. Hier wird die Zahl gespeichert.

Dann implementieren wir eine assoziierte Funktion namens `new` auf `Guess`, die Instanzen von `Guess`-Werten erstellt \[2\]. Die `new`-Funktion ist definiert, einen Parameter namens `value` vom Typ `i32` zu haben und einen `Guess` zurückzugeben. Der Code im Körper der `new`-Funktion testet `value`, um sicherzustellen, dass es zwischen 1 und 100 liegt \[3\]. Wenn `value` diese Prüfung nicht besteht, rufen wir `panic!` auf \[4\], was den Programmierer, der den aufrufenden Code schreibt, darüber informieren wird, dass er einen Bug hat, den er beheben muss, da das Erstellen eines `Guess` mit einem `value` ausserhalb dieses Bereichs den Vertrag verletzen würde, auf den `Guess::new` zurückgreift. Die Bedingungen, unter denen `Guess::new` in Panik geraten könnte, sollten in ihrer öffentlich zugänglichen API-Dokumentation diskutiert werden; wir werden die Dokumentationskonventionen behandeln, die die Möglichkeit eines `panic!` in der API-Dokumentation anzeigen, die Sie im Kapitel 14 erstellen. Wenn `value` die Prüfung besteht, erstellen wir einen neuen `Guess` mit seinem `value`-Feld auf den `value`-Parameter gesetzt und geben den `Guess` zurück \[5\].

Als nächstes implementieren wir eine Methode namens `value`, die `self` borrrowt, keine weiteren Parameter hat und eine `i32` zurückgibt \[6\]. Diese Art von Methode wird manchmal als _Getter_ bezeichnet, weil ihr Zweck darin besteht, einige Daten aus ihren Feldern zu erhalten und zurückzugeben. Diese öffentliche Methode ist notwendig, weil das `value`-Feld der `Guess`-Struktur privat ist. Es ist wichtig, dass das `value`-Feld privat ist, damit der Code, der die `Guess`-Struktur verwendet, nicht direkt `value` setzen darf: Der Code außerhalb des Moduls _muss_ die `Guess::new`-Funktion verwenden, um eine Instanz von `Guess` zu erstellen, wodurch sichergestellt wird, dass es keine Möglichkeit gibt, dass ein `Guess` ein `value` hat, das nicht von den Bedingungen in der `Guess::new`-Funktion überprüft wurde.

Eine Funktion, die einen Parameter hat oder nur Zahlen zwischen 1 und 100 zurückgibt, könnte dann in ihrer Signatur erklären, dass sie einen `Guess` nimmt oder zurückgibt, anstatt eine `i32`, und müsste keine weiteren Prüfungen in ihrem Körper vornehmen.
