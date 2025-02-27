# Introduction

Dans ce laboratoire, nous allons explorer le concept de chaînes de caractères en Rust. Rust a deux types de chaînes : `String` et `&str`.

Une `String` est une chaîne allouée sur le tas, pouvant grandir, qui est garantie être une séquence UTF-8 valide. D'un autre côté, `&str` est une tranche qui pointe vers une séquence UTF-8 valide et peut être utilisée pour examiner une `String`.

En Rust, les littéraux de chaîne de caractères peuvent être écrits de différentes manières, y compris en utilisant des caractères d'échappement pour représenter des caractères spéciaux. Par exemple, `\x3F` représente le caractère point d'interrogation et `\u{211D}` représente un point de code Unicode. Les littéraux de chaîne de caractères brutes peuvent également être utilisés si vous voulez écrire une chaîne telle quelle sans caractères d'échappement.

Si vous avez besoin de travailler avec des chaînes d'octets, Rust fournit des littéraux de chaîne d'octets en utilisant le préfixe `b`. Les chaînes d'octets peuvent avoir des caractères d'échappement d'octet, mais pas d'échappements Unicode. Les chaînes d'octets brutes peuvent également être utilisées de manière similaire aux littéraux de chaîne de caractères brutes.

Il est important de noter que `str` et `String` doivent toujours être des séquences UTF-8 valides. Si vous avez besoin de travailler avec des chaînes dans différentes encodages, vous pouvez utiliser des boîtes à outils externes comme `encoding` pour effectuer des conversions entre les encodages de caractères.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
