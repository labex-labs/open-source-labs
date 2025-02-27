# Grouping Configuration Values

Nous pouvons prendre une autre petite étape pour améliorer encore la fonction `parse_config`. En ce moment, nous renvoyons un tuple, mais ensuite, nous le brisons immédiatement à nouveau en parties individuelles. Ceci est un signe que peut-être nous n'avons pas encore la bonne abstraction.

Un autre indicateur qui montre qu'il y a des possibilités d'amélioration est la partie `config` de `parse_config`, ce qui implique que les deux valeurs que nous renvoyons sont liées et font toutes les deux partie d'une seule valeur de configuration. Nous ne communiquons pas actuellement ce sens dans la structure des données autrement que en groupant les deux valeurs dans un tuple ; nous allons plutôt placer les deux valeurs dans une seule structure et donner à chacun des champs de la structure un nom significatif. Cela facilitera la compréhension pour les futurs maintaineurs de ce code de la manière dont les différentes valeurs sont liées les unes aux autres et de leur but.

Le Listing 12-6 montre les améliorations apportées à la fonction `parse_config`.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Searching for {}", 2 config.query);
    println!("In file {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
       .expect("Should have been able to read the file");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

Listing 12-6 : Refactoring de `parse_config` pour renvoyer une instance d'une structure `Config`

Nous avons ajouté une structure nommée `Config` définie pour avoir des champs nommés `query` et `file_path` \[5\]. La signature de `parse_config` indique désormais qu'elle renvoie une valeur `Config` \[6\]. Dans le corps de `parse_config`, où nous renvoyions auparavant des fragments de chaîne qui faisaient référence à des valeurs `String` dans `args`, nous définissons désormais `Config` pour contenir des valeurs `String` propriétaires. La variable `args` dans `main` est le propriétaire des valeurs d'arguments et ne permet qu'à la fonction `parse_config` de les emprunter, ce qui signifie que nous violerions les règles d'emprunt de Rust si `Config` essayait de prendre la propriété des valeurs dans `args`.

Il existe plusieurs façons de gérer les données `String` ; la plus simple, bien que quelque peu inefficace, est d'appeler la méthode `clone` sur les valeurs \[7\] \[8\]. Cela créera une copie complète des données pour que l'instance `Config` puisse les posséder, ce qui prend plus de temps et de mémoire que de stocker une référence aux données de chaîne. Cependant, cloner les données rend également notre code très simple car nous n'avons pas à gérer les durées de vie des références ; dans cette circonstance, sacrifier un peu de performance pour gagner en simplicité est un compromis rentable.

> **Les compromis de l'utilisation de clone**
>
> Beaucoup de Rustaceans ont tendance à éviter d'utiliser `clone` pour résoudre les problèmes d'appartenance en raison de son coût exécutif. Dans le chapitre 13, vous apprendrez à utiliser des méthodes plus efficaces dans ce type de situation. Mais pour le moment, il est acceptable de copier quelques chaînes pour continuer à progresser car vous ne ferez ces copies qu'une seule fois et votre chemin de fichier et votre chaîne de requête sont très petites. Il vaut mieux avoir un programme fonctionnel un peu inefficace que de chercher à hyperoptimiser le code lors de votre première passe. Lorsque vous serez plus expérimenté avec Rust, il sera plus facile de commencer par la solution la plus efficace, mais pour le moment, appeler `clone` est parfaitement acceptable.

Nous avons mis à jour `main` pour qu'il place l'instance de `Config` renvoyée par `parse_config` dans une variable nommée `config` \[1\], et nous avons mis à jour le code qui utilisait précédemment les variables `query` et `file_path` séparées pour qu'il utilise désormais les champs de la structure `Config` à la place \[2\] \[3\] \[4\].

Maintenant, notre code communique plus clairement que `query` et `file_path` sont liés et que leur but est de configurer la manière dont le programme fonctionnera. Tout code qui utilise ces valeurs sait où les trouver dans l'instance `config` dans les champs nommés pour leur but.
