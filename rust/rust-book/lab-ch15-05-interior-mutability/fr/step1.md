# RefCell`<T>`{=html} et le modèle de mutabilité interne

La **mutabilité interne** est un modèle de conception en Rust qui vous permet de modifier des données même lorsqu'il existe des références immuables à ces données ; normalement, cette action est interdite par les règles d'emprunt. Pour modifier des données, le modèle utilise du code `unsafe` à l'intérieur d'une structure de données pour contourner les règles habituelles de Rust qui gouvernent la mutation et l'emprunt. Le code `unsafe` indique au compilateur que nous vérifions les règles manuellement au lieu de compter sur le compilateur pour les vérifier pour nous ; nous aborderons le code `unsafe` plus en détail au chapitre 19.

Nous ne pouvons utiliser des types qui utilisent le modèle de mutabilité interne que lorsque nous pouvons nous assurer que les règles d'emprunt seront respectées à l'exécution, même si le compilateur ne peut pas le garantir. Le code `unsafe` impliqué est ensuite encapsulé dans une API sécurisée, et le type externe reste immuable.

Explorons ce concept en examinant le type `RefCell<T>` qui suit le modèle de mutabilité interne.
