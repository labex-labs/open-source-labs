#Constantes

Comme les variables immuables, les **constantes** sont des valeurs qui sont liées à un nom et ne sont pas autorisées à changer, mais il existe quelques différences entre les constantes et les variables.

Tout d'abord, vous n'êtes pas autorisé à utiliser `mut` avec les constantes. Les constantes ne sont pas seulement immuables par défaut - elles sont toujours immuables. Vous déclarez les constantes en utilisant le mot clé `const` au lieu du mot clé `let`, et le type de la valeur **doit** être annoté. Nous aborderons les types et les annotations de type dans "Types de données", donc ne vous inquiétez pas des détails pour l'instant. Sachez seulement que vous devez toujours annoter le type.

Les constantes peuvent être déclarées dans n'importe quel contexte, y compris le contexte global, ce qui les rend utiles pour les valeurs dont de nombreuses parties du code ont besoin de savoir.

La dernière différence est que les constantes peuvent seulement être définies à une expression constante, pas au résultat d'une valeur qui ne pourrait être calculée qu'à l'exécution.

Voici un exemple de déclaration de constante :

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

Le nom de la constante est `THREE_HOURS_IN_SECONDS` et sa valeur est définie au résultat de la multiplication de 60 (le nombre de secondes dans une minute) par 60 (le nombre de minutes dans une heure) par 3 (le nombre d'heures que nous voulons compter dans ce programme). La convention de nommage des constantes en Rust est d'utiliser toutes les majuscules avec des tirets du bas entre les mots. Le compilateur est capable d'évaluer un ensemble limité d'opérations à la compilation, ce qui nous permet de choisir d'écrire cette valeur d'une manière plus facile à comprendre et à vérifier, plutôt que de définir cette constante à la valeur `10 800`. Consultez la section de la référence Rust sur l'évaluation des constantes à *https://doc.rust-lang.org/reference/const_eval.html* pour plus d'informations sur les opérations qui peuvent être utilisées lors de la déclaration des constantes.

Les constantes sont valides pour toute la durée de l'exécution d'un programme, dans le contexte dans lequel elles ont été déclarées. Cette propriété rend les constantes utiles pour les valeurs dans votre domaine d'application dont plusieurs parties du programme pourraient avoir besoin de savoir, comme le nombre maximal de points que n'importe quel joueur d'un jeu est autorisé à gagner, ou la vitesse de la lumière.

Donner un nom aux valeurs codées en dur utilisées tout au long de votre programme en tant que constantes est utile pour communiquer la signification de cette valeur aux futurs mainteneurs du code. Cela aide également à n'avoir qu'un seul endroit dans votre code où vous devriez modifier si la valeur codée en dur devait être mise à jour à l'avenir.
