# Vérification des règles d'emprunt à l'exécution avec RefCell`<T>`

Contrairement à `Rc<T>`, le type `RefCell<T>` représente une propriété exclusive des données qu'il stocke. Alors, en quoi `RefCell<T>` diffère-t-il d'un type comme `Box<T>`? Rappelez-vous les règles d'emprunt que vous avez apprises au chapitre 4 :

- À tout moment donné, vous pouvez avoir _soit_ une référence mutable, _soit_ un nombre quelconque de références immuables (mais pas les deux).
- Les références doivent toujours être valides.

Avec les références et `Box<T>`, les invariants des règles d'emprunt sont vérifiés à la compilation. Avec `RefCell<T>`, ces invariants sont vérifiés _à l'exécution_. Avec les références, si vous violez ces règles, vous obtiendrez une erreur du compilateur. Avec `RefCell<T>`, si vous violez ces règles, votre programme plantera et sortira.

Les avantages de la vérification des règles d'emprunt à la compilation sont que les erreurs seront détectées plus tôt dans le processus de développement et qu'il n'y a pas d'impact sur les performances à l'exécution car toutes les analyses sont effectuées à l'avance. Pour ces raisons, la vérification des règles d'emprunt à la compilation est le meilleur choix dans la majorité des cas, ce qui est pourquoi c'est la valeur par défaut de Rust.

L'avantage de la vérification des règles d'emprunt à l'exécution est que certaines situations sécuritaires en matière de mémoire sont alors autorisées, tandis que la vérification à la compilation les aurait interdites. L'analyse statique, comme le compilateur Rust, est intrinsèquement conservatrice. Certaines propriétés du code sont impossibles à détecter en analysant le code : l'exemple le plus célèbre est le problème de l'arrêt, qui est en dehors des limites de ce livre mais est un sujet intéressant à étudier.

Parce que certaines analyses sont impossibles, si le compilateur Rust n'est pas sûr que le code respecte les règles de propriété, il peut rejeter un programme correct ; de cette manière, il est conservateur. Si Rust acceptait un programme incorrect, les utilisateurs ne pourraient pas faire confiance aux garanties offertes par Rust. Cependant, si Rust rejette un programme correct, le programmeur sera dérangé, mais rien de catastrophique ne peut se produire. Le type `RefCell<T>` est utile lorsque vous êtes sûr que votre code suit les règles d'emprunt, mais que le compilateur est incapable de le comprendre et de le garantir.

De manière similaire à `Rc<T>`, `RefCell<T>` n'est destiné qu'à être utilisé dans des scénarios mono-threadés et vous donnera une erreur de compilation si vous essayez de l'utiliser dans un contexte multi-threadé. Nous parlerons de la manière d'obtenir la fonctionnalité de `RefCell<T>` dans un programme multi-threadé au chapitre 16.

Voici un récapitulatif des raisons de choisir `Box<T>`, `Rc<T>` ou `RefCell<T>` :

- `Rc<T>` permet plusieurs propriétaires des mêmes données ; `Box<T>` et `RefCell<T>` ont une propriété exclusive.
- `Box<T>` permet des emprunts immuables ou mutables vérifiés à la compilation ; `Rc<T>` permet seulement des emprunts immuables vérifiés à la compilation ; `RefCell<T>` permet des emprunts immuables ou mutables vérifiés à l'exécution.
- Parce que `RefCell<T>` permet des emprunts mutables vérifiés à l'exécution, vous pouvez modifier la valeur à l'intérieur de `RefCell<T>` même lorsque `RefCell<T>` est immuable.

Modifier la valeur à l'intérieur d'une valeur immuable est le **modèle de mutabilité interne**. Examnons une situation dans laquelle la mutabilité interne est utile et voyons comment cela est possible.
