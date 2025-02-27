# Les objets contiennent des données et un comportement

Le livre _Design Patterns: Elements of Reusable Object-Oriented Software_ d'Erich Gamma, Richard Helm, Ralph Johnson et John Vlissides (Addison-Wesley, 1994), surnommé le livre des _Gang of Four_, est un catalogue de modèles de conception orientés objet. Il définit la programmation orientée objet de la manière suivante :

Les programmes orientés objet sont composés d'objets. Un _objet_ regroupe à la fois des données et les procédures qui opèrent sur ces données. Les procédures sont généralement appelées _méthodes_ ou _opérations_.

En utilisant cette définition, Rust est orienté objet : les structs et les enums ont des données, et les blocs `impl` fournissent des méthodes sur les structs et les enums. Même si les structs et les enums avec des méthodes ne sont pas _appelés_ des objets, ils fournissent la même fonctionnalité, selon la définition des objets des _Gang of Four_.
