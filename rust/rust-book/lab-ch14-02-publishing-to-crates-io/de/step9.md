# Veröffentlichen auf Crates.io

Jetzt, nachdem Sie ein Konto erstellt haben, Ihren API-Token gespeichert haben, einen Namen für Ihre Crate gewählt haben und die erforderlichen Metadaten angegeben haben, sind Sie bereit zum Veröffentlichen! Beim Veröffentlichen einer Crate wird eine bestimmte Version auf *https://crates.io* hochgeladen, damit andere sie verwenden können.

Achten Sie darauf, denn ein Veröffentlichung ist _permanent_. Die Version kann niemals überschrieben werden und der Code kann nicht gelöscht werden. Ein wichtiges Ziel von Crates.io ist es, als permanenter Codearchiv zu fungieren, damit die Builds aller Projekte, die von Crates von *https://crates.io* abhängen, weiterhin funktionieren. Die Erlaubnis von Versionlöschungen würde das Erreichen dieses Ziels unmöglich machen. Es gibt jedoch keine Beschränkung für die Anzahl der Crate-Versionen, die Sie veröffentlichen können.

Führen Sie den Befehl `cargo publish` erneut aus. Es sollte jetzt erfolgreich sein:

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

Herzlichen Glückwunsch! Sie haben jetzt Ihren Code mit der Rust-Community geteilt, und jeder kann Ihre Crate als Abhängigkeit ihres Projekts leicht hinzufügen.
