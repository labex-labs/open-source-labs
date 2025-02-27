# `read_lines`

## Une approche naive

Cela pourrait être une première tentative raisonnable pour la première implémentation d'un débutant pour lire les lignes d'un fichier.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

Depuis que la méthode `lines()` renvoie un itérateur sur les lignes du fichier, nous pouvons également effectuer une opération de carte en ligne et collecter les résultats, donnant une expression plus concise et fluide.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
     .unwrap()  // déclenche une panique en cas d'erreur possible lors de la lecture du fichier
     .lines()  // divise la chaîne en un itérateur de fragments de chaîne
     .map(String::from)  // transforme chaque fragment en une chaîne
     .collect()  // rassemble tout dans un vecteur
}
```

Notez que dans les deux exemples ci-dessus, nous devons convertir la référence `&str` renvoyée par `lines()` en type propriétaire `String`, en utilisant `.to_string()` et `String::from` respectivement.

## Une approche plus efficace

Ici, nous passons la propriété du `File` ouvert à une structure `BufReader`. `BufReader` utilise un tampon interne pour réduire les allocations intermédiaires.

Nous mettons également à jour `read_lines` pour renvoyer un itérateur au lieu d'allouer de nouveaux objets `String` en mémoire pour chaque ligne.

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Le fichier hosts.txt doit exister dans le chemin courant
    if let Ok(lines) = read_lines("./hosts.txt") {
        // Consomme l'itérateur, renvoie une chaîne (Optionnelle)
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// La sortie est encapsulée dans un Result pour permettre de matcher sur les erreurs
// Renvoie un Itérateur vers le Reader des lignes du fichier.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

Exécuter ce programme imprime simplement les lignes individuellement.

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(Notez que puisque `File::open` attend un `AsRef<Path>` générique en tant qu'argument, nous définissons notre méthode générique `read_lines()` avec la même contrainte générique, en utilisant le mot clé `where`.)

Ce processus est plus efficace que de créer une `String` en mémoire avec tout le contenu du fichier. Cela peut entraîner en particulier des problèmes de performances lorsqu'on travaille avec de plus grands fichiers.
