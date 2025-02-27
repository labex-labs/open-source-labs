# Receiving User Input

Rappelez-vous que nous avons inclus la fonctionnalité d'entrée/sortie de la bibliothèque standard avec `use std::io;` à la première ligne du programme. Maintenant, nous allons appeler la fonction `stdin` du module `io`, qui nous permettra de gérer l'entrée de l'utilisateur :

```rust
io::stdin()
 .read_line(&mut guess)
```

Si nous n'avions pas importé la bibliothèque `io` avec `use std::io;` au début du programme, nous pourrions toujours utiliser la fonction en écrivant cet appel de fonction comme `std::io::stdin`. La fonction `stdin` renvoie une instance de `std::io::Stdin`, qui est un type qui représente un pointeur vers l'entrée standard de votre terminal.

Ensuite, la ligne `.read_line(&mut guess)` appelle la méthode `read_line` sur le pointeur d'entrée standard pour obtenir l'entrée de l'utilisateur. Nous passons également `&mut guess` en tant qu'argument à `read_line` pour lui dire dans quelle chaîne de caractères stocker l'entrée de l'utilisateur. Le travail complet de `read_line` est de prendre tout ce que l'utilisateur tape dans l'entrée standard et d'ajouter cela à une chaîne de caractères (sans écraser son contenu), nous passons donc cette chaîne de caractères en tant qu'argument. L'argument chaîne de caractères doit être mutable afin que la méthode puisse modifier le contenu de la chaîne.

Le `&` indique que cet argument est une _référence_, qui vous donne un moyen de permettre à plusieurs parties de votre code d'accéder à une partie de données sans avoir besoin de copier ces données dans la mémoire plusieurs fois. Les références sont une fonctionnalité complexe, et l'un des principaux avantages de Rust est à quel point il est sécurisé et facile d'utiliser les références. Vous n'avez pas besoin de connaître beaucoup de ces détails pour terminer ce programme. Pour l'instant, tout ce que vous avez besoin de savoir est que, comme les variables, les références sont immuables par défaut. Par conséquent, vous devez écrire `&mut guess` plutôt que `&guess` pour la rendre mutable. (Le chapitre 4 expliquera plus en détail les références.)
