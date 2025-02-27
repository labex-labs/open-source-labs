# Generieren einer Geheimzahl

Als nächstes müssen wir eine Geheimzahl generieren, die der Benutzer erraten wird. Die Geheimzahl sollte jedes Mal unterschiedlich sein, damit das Spiel mehrmals amüsant zu spielen ist. Wir werden eine Zufallszahl zwischen 1 und 100 verwenden, damit das Spiel nicht zu schwierig ist. Rust enthält noch keine Zufallszahl-Funktionalität in seiner Standardbibliothek. Der Rust-Team bietet jedoch eine `rand`-Kiste auf *https://crates.io/crates/rand* mit der genannten Funktionalität an.
