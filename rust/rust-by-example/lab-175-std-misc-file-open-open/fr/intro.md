# Introduction

Dans ce laboratoire, la fonction `open` est présentée comme un moyen d'ouvrir un fichier en mode lecture seule en fournissant le chemin vers le fichier souhaité. La fonction renvoie un objet `File` qui possède le descripteur de fichier et prend soin de fermer le fichier lorsqu'il n'est plus nécessaire.

Pour utiliser la fonction `open`, il est nécessaire d'importer les modules nécessaires tels que `std::fs::File`, `std::io::prelude::*` et `std::path::Path`. La méthode `File::open` est ensuite appelée avec le chemin en tant qu'argument. Si le fichier est ouvert avec succès, la fonction renvoie un objet `Result<File, io::Error>`, sinon, elle panique avec un message d'erreur.

Une fois le fichier ouvert, son contenu peut être lu en utilisant la méthode `read_to_string`. Cette méthode lit le contenu du fichier dans une chaîne de caractères et renvoie un `Result<usize, io::Error>`. Si l'opération de lecture est réussie, la chaîne de caractères contiendra le contenu du fichier. Sinon, elle panique avec un message d'erreur.

Dans l'exemple fourni, le contenu du fichier `hello.txt` est lu et affiché à la console. Le trait `drop` est utilisé pour s'assurer que le fichier est fermé lorsque l'objet `file` sort de portée.

> **Note:** Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
