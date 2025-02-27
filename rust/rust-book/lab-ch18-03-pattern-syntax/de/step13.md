# Teile eines Werts mit einem geschachtelten `_`

Wir können auch `_` innerhalb eines anderen Musters verwenden, um nur einen Teil eines Werts zu ignorieren. Beispielsweise, wenn wir nur einen Teil eines Werts testen möchten, aber die anderen Teile in dem entsprechenden Code, den wir ausführen möchten, nicht benötigen. Listing 18-18 zeigt den Code, der für das Verwalten eines Einstellungs-Werts verantwortlich ist. Die geschäftlichen Anforderungen sind, dass der Benutzer nicht in der Lage sein soll, eine vorhandene Anpassung einer Einstellung zu überschreiben, aber die Einstellung aufheben und ihr einen Wert zuweisen kann, wenn sie derzeit nicht gesetzt ist.

Dateiname: `src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("Kann einen vorhandenen benutzerdefinierten Wert nicht überschreiben");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("Einstellung ist {:?}", setting_value);
```

Listing 18-18: Verwendung eines Unterstrich-Zeichens innerhalb von Mustern, die `Some`-Varianten abgleichen, wenn wir den Wert innerhalb von `Some` nicht verwenden müssen

Dieser Code wird `Kann einen vorhandenen benutzerdefinierten Wert nicht überschreiben` ausgeben und dann `Einstellung ist Some(5)`. Im ersten `match`-Arm müssen wir nicht auf die Werte innerhalb der `Some`-Variante abgleichen oder verwenden, aber wir müssen den Fall testen, wenn `setting_value` und `new_setting_value` die `Some`-Variante sind. In diesem Fall geben wir den Grund aus, warum `setting_value` nicht geändert wird, und es wird nicht geändert.

In allen anderen Fällen (wenn entweder `setting_value` oder `new_setting_value` `None` ist), die durch das `_`-Muster im zweiten Arm ausgedrückt werden, möchten wir, dass `new_setting_value` `setting_value` wird.

Wir können auch Unterstrich-Zeichen an mehreren Stellen innerhalb eines Musters verwenden, um bestimmte Werte zu ignorieren. Listing 18-19 zeigt ein Beispiel dafür, wie der zweite und vierte Wert in einem Tupel aus fünf Elementen ignoriert werden.

Dateiname: `src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Einige Zahlen: {first}, {third}, {fifth}");
    }
}
```

Listing 18-19: Ignorieren mehrerer Teile eines Tupels

Dieser Code wird `Einige Zahlen: 2, 8, 32` ausgeben, und die Werte `4` und `16` werden ignoriert.
