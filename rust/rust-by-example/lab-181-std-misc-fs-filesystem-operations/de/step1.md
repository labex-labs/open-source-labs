# Dateisystemoperationen

Das Modul `std::fs` enthält mehrere Funktionen, die sich mit dem Dateisystem befassen.

```rust
use std::fs;
use std::fs::{File, OpenOptions};
use std::io;
use std::io::prelude::*;
use std::os::unix;
use std::path::Path;

// Eine einfache Implementierung von `% cat path`
fn cat(path: &Path) -> io::Result<String> {
    let mut f = File::open(path)?;
    let mut s = String::new();
    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}

// Eine einfache Implementierung von `% echo s > path`
fn echo(s: &str, path: &Path) -> io::Result<()> {
    let mut f = File::create(path)?;

    f.write_all(s.as_bytes())
}

// Eine einfache Implementierung von `% touch path` (ignoriert vorhandene Dateien)
fn touch(path: &Path) -> io::Result<()> {
    match OpenOptions::new().create(true).write(true).open(path) {
        Ok(_) => Ok(()),
        Err(e) => Err(e),
    }
}

fn main() {
    println!("`mkdir a`");
    // Erstellt ein Verzeichnis, gibt `io::Result<()>` zurück
    match fs::create_dir("a") {
        Err(why) => println!("! {:?}", why.kind()),
        Ok(_) => {},
    }

    println!("`echo hello > a/b.txt`");
    // Die vorherige Übereinstimmung kann mit der Methode `unwrap_or_else` vereinfacht werden
    echo("hello", &Path::new("a/b.txt")).unwrap_or_else(|why| {
        println!("! {:?}", why.kind());
    });

    println!("`mkdir -p a/c/d`");
    // Erstellt rekursiv ein Verzeichnis, gibt `io::Result<()>` zurück
    fs::create_dir_all("a/c/d").unwrap_or_else(|why| {
        println!("! {:?}", why.kind());
    });

    println!("`touch a/c/e.txt`");
    touch(&Path::new("a/c/e.txt")).unwrap_or_else(|why| {
        println!("! {:?}", why.kind());
    });

    println!("`ln -s../b.txt a/c/b.txt`");
    // Erstellt einen Symbolischen Link, gibt `io::Result<()>` zurück
    if cfg!(target_family = "unix") {
        unix::fs::symlink("../b.txt", "a/c/b.txt").unwrap_or_else(|why| {
            println!("! {:?}", why.kind());
        });
    }

    println!("`cat a/c/b.txt`");
    match cat(&Path::new("a/c/b.txt")) {
        Err(why) => println!("! {:?}", why.kind()),
        Ok(s) => println!("> {}", s),
    }

    println!("`ls a`");
    // Liest den Inhalt eines Verzeichnisses, gibt `io::Result<Vec<Path>>` zurück
    match fs::read_dir("a") {
        Err(why) => println!("! {:?}", why.kind()),
        Ok(paths) => for path in paths {
            println!("> {:?}", path.unwrap().path());
        },
    }

    println!("`rm a/c/e.txt`");
    // Löscht eine Datei, gibt `io::Result<()>` zurück
    fs::remove_file("a/c/e.txt").unwrap_or_else(|why| {
        println!("! {:?}", why.kind());
    });

    println!("`rmdir a/c/d`");
    // Löscht ein leeres Verzeichnis, gibt `io::Result<()>` zurück
    fs::remove_dir("a/c/d").unwrap_or_else(|why| {
        println!("! {:?}", why.kind());
    });
}
```

Hier ist die erwartete erfolgreiche Ausgabe:

```shell
$ rustc fs.rs && ./fs
$(mkdir a)
$(echo hello > a/b.txt)
$(mkdir -p a/c/d)
$(touch a/c/e.txt)
$(ln -s../b.txt a/c/b.txt)
$(cat a/c/b.txt)
> hello
$(ls a)
> "a/b.txt"
> "a/c"
$(rm a/c/e.txt)
$(rmdir a/c/d)
```

Und der endgültige Zustand des Verzeichnisses `a` ist:

```shell
$ tree a
a
|-- b.txt
`-- c
    `-- b.txt ->../b.txt

1 Verzeichnis, 2 Dateien
```

Eine alternative Möglichkeit, die Funktion `cat` zu definieren, ist mit der `?`-Notation:

```rust
fn cat(path: &Path) -> io::Result<String> {
    let mut f = File::open(path)?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}
```
