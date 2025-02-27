# Ein Arbeitsbereich erstellen

Ein _Arbeitsbereich_ ist eine Gruppe von Paketen, die die gleiche _Cargo.lock_ und Ausgabeverzeichnis teilen. Lassen Sie uns ein Projekt mit einem Arbeitsbereich erstellen - wir werden einfache Code verwenden, damit wir uns auf die Struktur des Arbeitsbereichs konzentrieren können. Es gibt mehrere Möglichkeiten, einen Arbeitsbereich zu strukturieren, daher zeigen wir nur eine häufige Methode. Wir werden einen Arbeitsbereich haben, der eine Binärdatei und zwei Bibliotheken enthält. Die Binärdatei, die die Hauptfunktionalität bereitstellen wird, wird von den beiden Bibliotheken abhängen. Eine Bibliothek wird eine `add_one`-Funktion und die andere Bibliothek eine `add_two`-Funktion bereitstellen. Diese drei Kraten werden Teil des gleichen Arbeitsbereichs sein. Wir beginnen, indem wir ein neues Verzeichnis für den Arbeitsbereich erstellen:

```bash
mkdir add
cd add
```

Als nächstes erstellen wir in das Verzeichnis `add` die Datei `Cargo.toml`, die den gesamten Arbeitsbereich konfigurieren wird. Diese Datei wird keinen `[package]`-Abschnitt haben. Stattdessen beginnt sie mit einem `[workspace]`-Abschnitt, der es uns ermöglicht, Mitglieder zum Arbeitsbereich hinzuzufügen, indem wir den Pfad zum Paket mit unserem Binärkraten angeben; in diesem Fall ist dieser Pfad _adder_:

Dateiname: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

Als nächstes erstellen wir den Binärkraten `adder`, indem wir `cargo new` im Verzeichnis `add` ausführen:

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

An diesem Punkt können wir den Arbeitsbereich erstellen, indem wir `cargo build` ausführen. Die Dateien in Ihrem Verzeichnis `add` sollten so aussehen:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

Der Arbeitsbereich hat ein `target`-Verzeichnis auf der obersten Ebene, in das die kompilierten Artefakte platziert werden; das `adder`-Paket hat kein eigenes `target`-Verzeichnis. Auch wenn wir `cargo build` aus dem `adder`-Verzeichnis ausführen würden, würden die kompilierten Artefakte immer noch in _add/target_ landen, statt in `add/adder/target`. Cargo strukturiert das `target`-Verzeichnis in einem Arbeitsbereich so, weil die Kraten in einem Arbeitsbereich voneinander abhängen sollen. Wenn jedes Kraten sein eigenes `target`-Verzeichnis hätte, müsste jedes Kraten jedes andere Kraten im Arbeitsbereich erneut kompilieren, um die Artefakte in seinem eigenen `target`-Verzeichnis zu platzieren. Indem sie ein gemeinsames `target`-Verzeichnis teilen, können die Kraten unnötiges Neukompilieren vermeiden.
