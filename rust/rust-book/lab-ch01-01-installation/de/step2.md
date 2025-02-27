# Installation von rustup auf Linux oder macOS

Wenn du Linux oder macOS verwendest, öffne ein Terminal und gib den folgenden Befehl ein:

```bash
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

Der Befehl lädt ein Skript herunter und startet die Installation des `rustup`-Tools, das die neueste stabile Version von Rust installiert. Du wirst möglicherweise nach dein Passwort gefragt. Wenn die Installation erfolgreich ist, wird die folgende Zeile erscheinen:

```rust
Rust is installed now. Great!
```

Du benötigst auch einen _Linker_, ein Programm, das Rust verwendet, um seine kompilierten Ausgaben zu einer Datei zusammenzufügen. Es ist wahrscheinlich, dass du bereits einen hast. Wenn du Linkerfehler erhältst, solltest du einen C-Compiler installieren, der normalerweise auch einen Linker enthält. Ein C-Compiler ist auch nützlich, da einige gängige Rust-Pakete von C-Code abhängen und einen C-Compiler benötigen werden.

Linux-Benutzer sollten im Allgemeinen GCC oder Clang gemäß der Dokumentation ihrer Distribution installieren. Beispielsweise kannst du, wenn du Ubuntu verwendest, das Paket `build-essential` installieren.
