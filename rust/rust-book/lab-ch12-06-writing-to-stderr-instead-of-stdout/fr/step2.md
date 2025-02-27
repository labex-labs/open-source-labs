# Vérifier où les erreurs sont écrites

Commençons par observer comment le contenu imprimé par `minigrep` est actuellement écrit sur la sortie standard, y compris tous les messages d'erreur que nous souhaitons écrire sur la sortie d'erreur standard à la place. Nous allons le faire en redirigeant le flux de sortie standard vers un fichier tout en provoquant intentionnellement une erreur. Nous ne redirigerons pas le flux de sortie d'erreur, de sorte que tout contenu envoyé à la sortie d'erreur continuera à s'afficher sur l'écran.

On s'attend à ce que les programmes de ligne de commande envoient les messages d'erreur au flux de sortie d'erreur standard, de sorte que nous pouvons toujours voir les messages d'erreur sur l'écran même si nous redirigeons le flux de sortie standard vers un fichier. Notre programme n'est pas actuellement bien comporté : nous allons voir qu'il enregistre la sortie de message d'erreur dans un fichier au lieu de l'afficher sur l'écran!

Pour démontrer ce comportement, nous allons exécuter le programme avec `>` et le chemin du fichier, _output.txt_, vers lequel nous souhaitons rediriger le flux de sortie standard. Nous ne passerons aucun argument, ce qui devrait provoquer une erreur :

```bash
cargo run > output.txt
```

La syntaxe `>` indique au shell d'écrire le contenu de la sortie standard dans _output.txt_ au lieu de l'afficher sur l'écran. Nous n'avons pas vu le message d'erreur que nous attendions s'afficher sur l'écran, ce qui signifie qu'il doit être fini dans le fichier. Voici ce que contient _output.txt_ :

```rust
Problem parsing arguments: not enough arguments
```

Effectivement, notre message d'erreur est imprimé sur la sortie standard. Il est beaucoup plus utile que les messages d'erreur comme celui-ci soient imprimés sur la sortie d'erreur, de sorte que seul les données provenant d'une exécution réussie se retrouvent dans le fichier. Nous allons corriger cela.
