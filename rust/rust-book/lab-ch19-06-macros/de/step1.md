# Makros

Wir haben in diesem Buch Makros wie `println!` verwendet, aber wir haben noch nicht vollständig untersucht, was ein Makro ist und wie es funktioniert. Der Begriff _Makro_ bezieht sich auf eine Familie von Features in Rust: _deklarative_ Makros mit `macro_rules!` und drei Arten von _prozeduralen_ Makros:

- Benutzerdefinierte `#[derive]`-Makros, die den Code angeben, der mit dem `derive`-Attribut hinzugefügt wird, das auf Structs und Enums verwendet wird
- Attributähnliche Makros, die benutzerdefinierte Attribute definieren, die auf jedem Element verwendbar sind
- Funktionähnliche Makros, die wie Funktionsaufrufe aussehen, aber auf den als Argument angegebenen Tokens operieren

Wir werden nacheinander über jedes dieser Punkte sprechen, aber zunächst schauen wir uns an, warum wir überhaupt Makros brauchen, wenn wir bereits Funktionen haben.
