# Einführung

In diesem Lab wird die `open`-Funktion als Möglichkeit eingeführt, um eine Datei im schreibgeschützten Modus zu öffnen, indem ein Pfad zur gewünschten Datei angegeben wird. Die Funktion gibt ein `File`-Objekt zurück, das den Dateidescriptor besitzt und sich um das Schließen der Datei kümmert, wenn sie nicht mehr benötigt wird.

Um die `open`-Funktion zu verwenden, muss man die erforderlichen Module wie `std::fs::File`, `std::io::prelude::*` und `std::path::Path` importieren. Die `File::open`-Methode wird dann mit dem Pfad als Argument aufgerufen. Wenn die Datei erfolgreich geöffnet wird, gibt die Funktion ein `Result<File, io::Error>`-Objekt zurück, andernfalls bricht sie mit einer Fehlermeldung ab.

Sobald die Datei geöffnet ist, können ihre Inhalte mit der `read_to_string`-Methode gelesen werden. Diese Methode liest die Inhalte der Datei in einen String und gibt ein `Result<usize, io::Error>` zurück. Wenn der Lesevorgang erfolgreich ist, enthält der String die Dateiinhalte. Andernfalls bricht er mit einer Fehlermeldung ab.

Im bereitgestellten Beispiel werden die Inhalte der `hello.txt`-Datei gelesen und auf der Konsole ausgegeben. Das `drop`-Trait wird verwendet, um sicherzustellen, dass die Datei geschlossen wird, wenn das `file`-Objekt außer Gültigkeitsbereich gelangt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
