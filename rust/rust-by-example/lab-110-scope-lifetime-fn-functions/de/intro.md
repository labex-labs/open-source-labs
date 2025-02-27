# Einführung

In diesem Lab werden wir mit Lebensdauern in Rust auf Funktionssignaturen eingestuft, wobei jede Referenz eine annotierte Lebensdauer haben muss und jede zurückgegebene Referenz die gleiche Lebensdauer wie eine Eingabe haben muss oder `static` sein muss. Es ist wichtig zu beachten, dass das Zurückgeben von Referenzen ohne Eingabe verboten ist, wenn dies zu einem Zurückgeben von Referenzen auf ungültige Daten führen würde. Die bereitgestellten Beispiele veranschaulichen gültige Formen von Funktionen mit Lebensdauern, einschließlich Funktionen mit einer Eingabereferenz, Funktionen mit mutablen Referenzen, Funktionen mit mehreren Elementen und unterschiedlicher Lebensdauer sowie Funktionen, die Referenzen zurückgeben, die als Parameter übergeben wurden.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
