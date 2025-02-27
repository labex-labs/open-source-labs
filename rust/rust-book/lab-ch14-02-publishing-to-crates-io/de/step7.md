# Ein Crates.io-Konto einrichten

Bevor Sie irgendwelche Crates veröffentlichen können, müssen Sie ein Konto auf *https://crates.io* erstellen und einen API-Token erhalten. Um dies zu tun, besuchen Sie die Startseite auf *https://crates.io* und melden Sie sich über ein GitHub-Konto an. (Das GitHub-Konto ist derzeit ein Voraussetzung, aber die Website wird möglicherweise in Zukunft auch andere Möglichkeiten des Erstellens eines Kontos unterstützen.) Nachdem Sie sich angemeldet haben, besuchen Sie Ihre Kontoeinstellungen auf *https://crates.io/me* und erhalten Sie Ihren API-Schlüssel. Anschließend führen Sie den Befehl `cargo login` mit Ihrem API-Schlüssel aus, wie folgt:

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

Dieser Befehl wird Cargo über Ihren API-Token informieren und ihn lokal in _\~/.cargo/credentials_ speichern. Beachten Sie, dass dieser Token ein _Geheimnis_ ist: Teilen Sie ihn mit niemandem anderen. Wenn Sie ihn aus irgendeinem Grund mit jemandem teilen, sollten Sie ihn widerrufen und einen neuen Token auf *https://crates.io* generieren.
