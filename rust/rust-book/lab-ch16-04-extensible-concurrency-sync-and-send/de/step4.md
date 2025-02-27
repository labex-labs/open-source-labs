# Manuelles Implementieren von Send und Sync ist unsicher

Da Typen, die aus den `Send`- und `Sync`-Traits bestehen, automatisch auch `Send` und `Sync` sind, müssen wir diese Traits nicht manuell implementieren. Als Marker-Traits haben sie sogar keine Methoden, die implementiert werden müssen. Sie sind nur nützlich, um Invarianten in Bezug auf die Concurrency zu erzwingen.

Das manuelle Implementieren dieser Traits erfordert das Schreiben von unsicherem Rust-Code. Wir werden im Kapitel 19 über das Verwenden von unsicherem Rust-Code sprechen; für jetzt ist die wichtigste Information, dass das Erstellen neuer konkurrierender Typen, die nicht aus `Send`- und `Sync`-Teilen bestehen, sorgfältige Überlegungen erfordert, um die Sicherheitsgarantien zu gewährleisten. "The Rustonomicon" unter *https://doc.rust-lang.org/stable/nomicon* enthält weitere Informationen über diese Garantien und wie man sie gewährleistet.
