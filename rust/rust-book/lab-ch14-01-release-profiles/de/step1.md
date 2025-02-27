# Customizing Builds with Release Profiles

In Rust sind _Releaseprofile_ vordefinierte und anpassbare Profile mit unterschiedlichen Konfigurationen, die es einem Programmierer ermöglichen, mehr Kontrolle über verschiedene Optionen für die Codekompilierung zu haben. Jedes Profil wird unabhängig voneinander konfiguriert.

Cargo hat zwei Hauptprofile: das `dev`-Profil, das Cargo verwendet, wenn Sie `cargo build` ausführen, und das `release`-Profil, das Cargo verwendet, wenn Sie `cargo build --release` ausführen. Das `dev`-Profil ist mit guten Standardwerten für die Entwicklung definiert, und das `release`-Profil hat gute Standardwerte für Release-Builds.

Diese Profilnamen sollten Ihnen aus der Ausgabe Ihrer Builds bekannt sein:

```bash
$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s
```

`dev` und `release` sind diese unterschiedlichen Profile, die vom Compiler verwendet werden.

Cargo hat Standardwerte für jedes der Profile, die gelten, wenn Sie in der `Cargo.toml`-Datei Ihres Projekts keine `[profile.*]`-Abschnitte explizit hinzugefügt haben. Indem Sie `[profile.*]`-Abschnitte für jedes Profil hinzufügen, das Sie anpassen möchten, überschreiben Sie einen beliebigen Teils der Standardwerte. Beispielsweise sind hier die Standardwerte für die `opt-level`-Einstellung für die `dev`- und `release`-Profile:

Dateiname: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 0

[profile.release]
opt-level = 3
```

Die `opt-level`-Einstellung steuert die Anzahl der Optimierungen, die Rust auf Ihren Code anwenden wird, mit einem Bereich von 0 bis 3. Die Anwendung mehrerer Optimierungen verlängert die Kompilierungszeit, daher sollten Sie bei der Entwicklung und häufigen Kompilierung Ihres Codes weniger Optimierungen anwenden, um schneller zu kompilieren, auch wenn der resultierende Code langsamer läuft. Der Standardwert für `opt-level` für `dev` ist daher `0`. Wenn Sie bereit sind, Ihren Code zu veröffentlichen, ist es am besten, mehr Zeit für die Kompilierung zu verwenden. Sie werden den Code nur einmal im Release-Modus kompilieren, aber Sie werden das kompilierte Programm viele Male ausführen, daher wird der Release-Modus längere Kompilierungszeiten gegen schneller laufenden Code eintauschen. Deshalb ist der Standardwert für `opt-level` für das `release`-Profil `3`.

Sie können einen Standardwert überschreiben, indem Sie einen anderen Wert für ihn in `Cargo.toml` hinzufügen. Beispielsweise können wir diese beiden Zeilen zu unserer `Cargo.toml`-Datei unseres Projekts hinzufügen, um Optimierungsstufe 1 im Entwicklungs-Profil zu verwenden:

Dateiname: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 1
```

Dieser Code überschreibt den Standardwert von `0`. Wenn wir jetzt `cargo build` ausführen, wird Cargo die Standardwerte für das `dev`-Profil plus unsere Anpassung von `opt-level` verwenden. Da wir `opt-level` auf `1` gesetzt haben, wird Cargo mehr Optimierungen anwenden als der Standard, aber nicht so viele wie bei einem Release-Build.

Für die vollständige Liste der Konfigurationsoptionen und Standardwerte für jedes Profil finden Sie die Dokumentation von Cargo unter *https://doc.rust-lang.org/cargo/reference/profiles.html*.
