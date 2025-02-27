# Veröffentlichen einer neuen Version einer bestehenden Crate

Wenn Sie Änderungen an Ihrer Crate vorgenommen haben und bereit sind, eine neue Version zu veröffentlichen, ändern Sie den in Ihrer `Cargo.toml`-Datei angegebenen `version`-Wert und veröffentlichen Sie erneut. Verwenden Sie die Semantic Versioning-Regeln auf *http://semver.org*, um zu bestimmen, welche passende nächste Versionsnummer ist, basierend auf den Art der Änderungen, die Sie vorgenommen haben. Anschließend führen Sie `cargo publish` aus, um die neue Version hochzuladen.
