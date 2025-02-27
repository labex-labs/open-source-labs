# Introduction

Dans ce laboratoire, nous apprenons qu'une clause `where` en Rust peut être utilisée pour exprimer des contraintes pour les types génériques séparément de leur déclaration, permettant une syntaxe plus claire, et peut également appliquer des contraintes à des types arbitraires plutôt que seulement aux paramètres de type. La clause `where` est particulièrement utile lorsque les contraintes sont plus expressives que la syntaxe normale, comme dans l'exemple impliquant le trait `PrintInOption`.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
