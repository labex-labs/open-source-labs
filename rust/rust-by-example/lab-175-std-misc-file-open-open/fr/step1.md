# `open`

La fonction `open` peut être utilisée pour ouvrir un fichier en mode lecture seule.

Un objet `File` possède une ressource, le descripteur de fichier, et prend soin de fermer le fichier lorsqu'il est détruit (`drop`).

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // Crée un chemin vers le fichier souhaité
    let path = Path::new("hello.txt");
    let display = path.display();

    // Ouvre le chemin en mode lecture seule, renvoie `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("impossible d'ouvrir {}: {}", display, why),
        Ok(file) => file,
    };

    // Lit le contenu du fichier dans une chaîne de caractères, renvoie `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("impossible de lire {}: {}", display, why),
        Ok(_) => print!("{} contient:\n{}", display, s),
    }

    // L'objet `file` sort de portée, et le fichier "hello.txt" est fermé
}
```

Voici la sortie réussie attendue :

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt contient:
Hello World!
```

(On vous encourage à tester l'exemple précédent dans différentes conditions de défaillance : `hello.txt` n'existe pas, ou `hello.txt` n'est pas lisible, etc.)
