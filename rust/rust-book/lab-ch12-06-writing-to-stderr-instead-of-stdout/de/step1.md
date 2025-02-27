# Schreiben von Fehlermeldungen an die Standardfehlerausgabe statt an die Standardausgabe

Im Moment schreiben wir all unsere Ausgabe an den Terminal mit der `println!`-Makro. In den meisten Terminals gibt es zwei Arten von Ausgabe: _Standardausgabe_ (`stdout`) für allgemeine Informationen und _Standardfehlerausgabe_ (`stderr`) für Fehlermeldungen. Diese Unterscheidung ermöglicht es Benutzern, die erfolgreiche Ausgabe eines Programms in eine Datei zu leiten, aber trotzdem Fehlermeldungen auf dem Bildschirm auszugeben.

Das `println!`-Makro ist nur in der Lage, an die Standardausgabe zu drucken, also müssen wir etwas anderes verwenden, um an die Standardfehlerausgabe zu drucken.
