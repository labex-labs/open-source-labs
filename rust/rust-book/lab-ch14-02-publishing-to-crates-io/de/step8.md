# Hinzufügen von Metadaten zu einer neuen Crate

Angenommen, Sie haben eine Crate, die Sie veröffentlichen möchten. Bevor Sie veröffentlichen, müssen Sie einige Metadaten im Abschnitt `[package]` der `Cargo.toml`-Datei der Crate hinzufügen.

Ihre Crate muss einen eindeutigen Namen haben. Während Sie lokal an einer Crate arbeiten, können Sie eine Crate wie Sie möchten benennen. Auf *https://crates.io* werden jedoch Crate-Namen auf einen ersten-kommt, ersten-dient-Basis zugewiesen. Wenn ein Crate-Name bereits vergeben ist, kann niemand else eine Crate mit diesem Namen veröffentlichen. Bevor Sie versuchen, eine Crate zu veröffentlichen, suchen Sie nach dem Namen, den Sie verwenden möchten. Wenn der Name bereits verwendet wurde, müssen Sie einen anderen Namen finden und das `name`-Feld in der `Cargo.toml`-Datei unter dem Abschnitt `[package]` bearbeiten, um den neuen Namen für die Veröffentlichung zu verwenden, wie folgt:

Dateiname: `Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

Auch wenn Sie einen eindeutigen Namen gewählt haben, wenn Sie `cargo publish` ausführen, um die Crate zu veröffentlichen, erhalten Sie eine Warnung und dann einen Fehler:

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

Dies führt zu einem Fehler, weil Sie einige wichtige Informationen fehlen: Eine Beschreibung und eine Lizenz sind erforderlich, damit die Menschen wissen, was Ihre Crate macht und unter welchen Bedingungen sie sie verwenden können. In `Cargo.toml` fügen Sie eine Beschreibung hinzu, die nur ein oder zwei Sätze umfasst, da sie in den Suchergebnissen mit Ihrer Crate erscheinen wird. Für das `license`-Feld müssen Sie einen _Lizenzbezeichnerwert_ angeben. Die Software Package Data Exchange (SPDX) der Linux Foundation auf *http://spdx.org/licenses* listet die Bezeichner, die Sie für diesen Wert verwenden können. Beispielsweise um anzugeben, dass Sie Ihre Crate unter der MIT-Lizenz lizenziert haben, fügen Sie den Bezeichner `MIT` hinzu:

Dateiname: `Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

Wenn Sie eine Lizenz verwenden möchten, die nicht in der SPDX erscheint, müssen Sie den Text dieser Lizenz in eine Datei platzieren, die Datei in Ihrem Projekt einbeziehen und dann `license-file` verwenden, um den Namen dieser Datei anzugeben, anstatt den `license`-Schlüssel zu verwenden.

Die Beratung darüber, welche Lizenz für Ihr Projekt geeignet ist, liegt außerhalb des Rahmens dieses Buches. Viele Menschen in der Rust-Community lizenzieren ihre Projekte auf die gleiche Weise wie Rust, indem sie eine doppelte Lizenz von `MIT OR Apache-2.0` verwenden. Diese Praxis zeigt, dass Sie auch mehrere Lizenzbezeichner getrennt durch `OR` angeben können, um mehrere Lizenzen für Ihr Projekt zu haben.

Mit einem eindeutigen Namen, der Version, Ihrer Beschreibung und einer Lizenz hinzugefügt, könnte die `Cargo.toml`-Datei eines Projekts, das bereit zum Veröffentlichen ist, wie folgt aussehen:

Dateiname: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

Die Dokumentation von Cargo auf *https://doc.rust-lang.org/cargo* beschreibt andere Metadaten, die Sie angeben können, um sicherzustellen, dass andere Ihre Crate leichter entdecken und verwenden können.
