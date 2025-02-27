# Iterieren über die Werte in einem Vektor

Um nacheinander auf jedes Element in einem Vektor zuzugreifen, würden wir durch alle Elemente iterieren, anstatt Indizes zu verwenden, um eines nach dem anderen zuzugreifen. Listing 8-7 zeigt, wie man eine `for`-Schleife verwendet, um unveränderliche Referenzen auf jedes Element in einem Vektor von `i32`-Werten zu erhalten und sie auszugeben.

```rust
let v = vec![100, 32, 57];
for i in &v {
    println!("{i}");
}
```

Listing 8-7: Ausgabe jedes Elements in einem Vektor, indem man über die Elemente mit einer `for`-Schleife iteriert

Wir können auch über veränderliche Referenzen auf jedes Element in einem veränderlichen Vektor iterieren, um Änderungen an allen Elementen vorzunehmen. Die `for`-Schleife in Listing 8-8 wird jedem Element `50` hinzufügen.

```rust
let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
```

Listing 8-8: Iterieren über veränderliche Referenzen auf Elemente in einem Vektor

Um den Wert, auf den die veränderliche Referenz zeigt, zu ändern, müssen wir den Dereferenzierungsoperator `*` verwenden, um auf den Wert in `i` zu gelangen, bevor wir den `+=`-Operator verwenden können. Wir werden im Abschnitt "Following the Pointer to the Value" mehr über den Dereferenzierungsoperator sprechen.

Iterieren über einen Vektor, ob unveränderlich oder veränderlich, ist sicher aufgrund der Regeln des Entleihensprüfers. Wenn wir versuchten, Elemente in den `for`-Schleifenkörpern in Listing 8-7 und Listing 8-8 einzufügen oder zu entfernen, würden wir einen Compilerfehler erhalten, ähnlich dem, den wir mit dem Code in Listing 8-6 bekamen. Die Referenz auf den Vektor, die die `for`-Schleife hält, verhindert die gleichzeitige Modifikation des gesamten Vektors.
