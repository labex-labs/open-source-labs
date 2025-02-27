# Path

La structure `Path` représente les chemins de fichiers dans le système de fichiers sous-jacent. Il existe deux variantes de `Path` : `posix::Path` pour les systèmes UNIX et `windows::Path` pour Windows. Le préambule exporte la variante `Path` appropriée spécifique à la plateforme.

Un `Path` peut être créé à partir d'un `OsStr` et fournit plusieurs méthodes pour obtenir des informations sur le fichier/répertoire auquel le chemin pointe.

Un `Path` est immuable. La version propriétaire de `Path` est `PathBuf`. La relation entre `Path` et `PathBuf` est similaire à celle de `str` et `String` : un `PathBuf` peut être modifié in situ et peut être déréférencé en un `Path`.

Notez qu'un `Path` n'est _pas_ représenté en interne comme une chaîne UTF-8, mais est stocké comme un `OsString`. Par conséquent, convertir un `Path` en un `&str` n'est _pas_ gratuit et peut échouer (une `Option` est renvoyée). Cependant, un `Path` peut être converti librement en un `OsString` ou `&OsStr` en utilisant respectivement `into_os_string` et `as_os_str`.

```rust
use std::path::Path;

fn main() {
    // Crée un `Path` à partir d'un `&'static str`
    let path = Path::new(".");

    // La méthode `display` renvoie une structure `Display`able
    let _display = path.display();

    // `join` fusionne un chemin avec un conteneur d'octets en utilisant le séparateur
    // spécifique à l'OS, et renvoie un `PathBuf`
    let mut new_path = path.join("a").join("b");

    // `push` étend le `PathBuf` avec un `&Path`
    new_path.push("c");
    new_path.push("myfile.tar.gz");

    // `set_file_name` met à jour le nom de fichier du `PathBuf`
    new_path.set_file_name("package.tgz");

    // Convertit le `PathBuf` en une tranche de chaîne
    match new_path.to_str() {
        None => panic!("new path is not a valid UTF-8 sequence"),
        Some(s) => println!("new path is {}", s),
    }
}
```

Assurez-vous de consulter les autres méthodes de `Path` (`posix::Path` ou `windows::Path`) et la structure `Metadata`.
