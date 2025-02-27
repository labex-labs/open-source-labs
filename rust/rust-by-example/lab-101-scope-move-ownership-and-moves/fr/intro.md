# Introduction

Dans ce laboratoire, il est expliqué que dans Rust, les variables ont la propriété des ressources et ne peuvent avoir qu'un seul propriétaire, ce qui empêche les ressources d'être libérées plusieurs fois. Lorsque des variables sont assignées ou que des arguments de fonction sont passés par valeur, la propriété des ressources est transférée, ce qui est appelé un _move_. Après le _move_, l'ancien propriétaire ne peut plus être utilisé pour éviter de créer des pointeurs faussaires. L'exemple de code illustre ces concepts en montrant comment la propriété des variables allouées sur la pile et sur le tas est transférée et comment accéder à une variable après que sa propriété a été transférée entraîne des erreurs.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
