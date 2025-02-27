# Verwendung einer Kiste, um weitere Funktionalität zu erhalten

Denken Sie daran, dass eine Kiste eine Sammlung von Rust-Quellcode-Dateien ist. Das Projekt, das wir bisher gebaut haben, ist eine _Binärkiste_, das heißt, es ist ein ausführbares Programm. Die `rand`-Kiste ist eine _Bibliothekskiste_, die Code enthält, der für andere Programme verwendet werden soll und nicht eigenständig ausgeführt werden kann.

Die Koordination von externen Kisten durch Cargo ist der Bereich, in dem Cargo wirklich aufleuchtet. Bevor wir Code schreiben können, der `rand` verwendet, müssen wir die `Cargo.toml`-Datei ändern, um die `rand`-Kiste als Abhängigkeit hinzuzufügen. Öffnen Sie jetzt diese Datei und fügen Sie die folgende Zeile am Ende unterhalb der `[dependencies]`-Abschnittshöhe hinzu, die Cargo für Sie erstellt hat. Stellen Sie sicher, dass Sie `rand` genau so angeben wie hier, mit dieser Versionsnummer, sonst können die Codebeispiele in diesem Tutorial möglicherweise nicht funktionieren:

Dateiname: `Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

In der `Cargo.toml`-Datei ist alles, was einem Abschnittshöhe folgt, Teil dieses Abschnitts, der bis zu einem neuen Abschnitt anhält. In `[dependencies]` sagen Sie Cargo, welche externen Kisten Ihr Projekt von sich abhängt und welche Versionen dieser Kisten Sie benötigen. In diesem Fall geben wir die `rand`-Kiste mit dem semantischen Versionsbezeichner `0.8.5` an. Cargo versteht Semantic Versioning (manchmal auch als _SemVer_ bezeichnet), das eine Standard für das Schreiben von Versionsnummern ist. Der Bezeichner `0.8.5` ist eigentlich eine Abkürzung für `^0.8.5`, was bedeutet, dass jede Version mindestens 0.8.5, aber unter 0.9.0 ist.

Cargo betrachtet diese Versionen als mit einer öffentlichen API kompatibel mit Version 0.8.5, und diese Spezifikation stellt sicher, dass Sie die neueste Patchversion erhalten, die noch mit dem Code in diesem Kapitel kompilieren wird. Keine Version 0.9.0 oder höher ist gewährleistet, die gleiche API zu haben wie diejenige, die die folgenden Beispiele verwenden.

Lassen Sie uns jetzt das Projekt erstellen, ohne den Code zu ändern, wie in Listing 2-2 gezeigt.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

Listing 2-2: Die Ausgabe von `cargo build` nach Hinzufügen der `rand`-Kiste als Abhängigkeit

Sie können andere Versionsnummern sehen (aber alle werden mit dem Code kompatibel sein, dank SemVer!) und andere Zeilen (abhängig von dem Betriebssystem), und die Zeilen können in einer anderen Reihenfolge sein.

Wenn wir eine externe Abhängigkeit hinzufügen, holt Cargo die neuesten Versionen von allem, was diese Abhängigkeit benötigt, aus dem _Registrierungsverzeichnis_, das eine Kopie der Daten von Crates.io auf *https://crates.io* ist. Crates.io ist der Ort, an dem Menschen in der Rust-Ekosystem ihre Open-Source-Rust-Projekte für andere zur Verwendung stellen.

Nachdem das Registrierungsverzeichnis aktualisiert wurde, überprüft Cargo den `[dependencies]`-Abschnitt und lädt alle aufgelisteten Kisten herunter, die noch nicht heruntergeladen wurden. In diesem Fall hat Cargo auch andere Kisten abgerufen, auf die `rand` angewiesen ist, um zu funktionieren, obwohl wir nur `rand` als Abhängigkeit aufgelistet haben. Nachdem die Kisten heruntergeladen wurden, kompiliert Rust sie und kompiliert dann das Projekt mit den verfügbaren Abhängigkeiten.

Wenn Sie sofort erneut `cargo build` ausführen, ohne Änderungen vorzunehmen, erhalten Sie keine Ausgabe außer der `Finished`-Zeile. Cargo weiß, dass es die Abhängigkeiten bereits heruntergeladen und kompiliert hat, und Sie haben nichts in Ihrer `Cargo.toml`-Datei geändert. Cargo weiß auch, dass Sie nichts an Ihrem Code geändert haben, daher kompiliert es auch nicht erneut. Da es nichts zu tun hat, beendet es sich einfach.

Wenn Sie die `src/main.rs`-Datei öffnen, eine unbedeutende Änderung vornehmen, speichern Sie sie und bauen erneut, sehen Sie nur zwei Ausgabelines:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

Diese Zeilen zeigen, dass Cargo nur die Build mit Ihrer kleinen Änderung an der `src/main.rs`-Datei aktualisiert. Ihre Abhängigkeiten haben sich nicht geändert, daher weiß Cargo, dass es das Reusen kann, was es bereits heruntergeladen und kompiliert hat für diese.
