# Deprecieren von Versionen von Crates.io mit cargo yank

Obwohl Sie frühere Versionen einer Crate nicht entfernen können, können Sie verhindern, dass zukünftige Projekte sie als neue Abhängigkeit hinzufügen. Dies ist nützlich, wenn eine Crate-Version aus irgendeinem Grund fehlerhaft ist. In solchen Situationen unterstützt Cargo das Entfernen (Yanken) einer Crate-Version.

Das Entfernen (Yanken) einer Version verhindert, dass neue Projekte von dieser Version abhängen, während es allen bestehenden Projekten ermöglicht, die davon abhängen, weiterhin zu funktionieren. Im Wesentlichen bedeutet ein Entfernen (Yanken), dass alle Projekte mit einer _Cargo.lock_ nicht abstürzen und dass alle zukünftig generierten _Cargo.lock_-Dateien die entfernte (geyankte) Version nicht verwenden werden.

Um eine Version einer Crate zu entfernen (yanken), führen Sie in dem Verzeichnis der zuvor veröffentlichten Crate `cargo yank` aus und geben an, welche Version Sie entfernen (yanken) möchten. Beispielsweise, wenn wir eine Crate namens `guessing_game` in Version 1.0.1 veröffentlicht haben und wir sie entfernen (yanken) möchten, würden wir im Projektverzeichnis von `guessing_game` folgendes ausführen:

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

Indem Sie `--undo` zum Befehl hinzufügen, können Sie auch das Entfernen (Yanken) rückgängig machen und erlauben, dass Projekte wieder von einer Version abhängen:

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

Ein Entfernen (Yanken) löscht _keinen_ Code. Es kann beispielsweise keine versehentlich hochgeladenen Geheimnisse löschen. Wenn das passiert, müssen Sie diese Geheimnisse sofort zurücksetzen.
