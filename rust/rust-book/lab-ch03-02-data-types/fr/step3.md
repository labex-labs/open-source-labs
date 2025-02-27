# Types entiers

Un _entier_ est un nombre sans composant fractionnaire. Nous avons utilisé un type entier dans le chapitre 2, le type `u32`. Cette déclaration de type indique que la valeur associée devrait être un entier non signé (les types entiers signés commencent par `i` au lieu de `u`) qui occupe 32 bits d'espace. Le tableau 3-1 montre les types entiers intégrés en Rust. Nous pouvons utiliser n'importe laquelle de ces variantes pour déclarer le type d'une valeur entière.

Tableau 3-1 : Types entiers en Rust

Longueur Signé Non signé

---

8 bits `i8` `u8`
16 bits `i16` `u16`
32 bits `i32` `u32`
64 bits `i64` `u64`
128 bits `i128` `u128`
architecture `isize` `usize`

Chaque variant peut être signé ou non signé et a une taille explicite. _Signé_ et _non signé_ se réfèrent au fait qu'il est possible ou non pour le nombre d'être négatif - en d'autres termes, si le nombre doit avoir un signe (signé) ou s'il ne sera jamais que positif et peut donc être représenté sans signe (non signé). C'est comme écrire des nombres sur papier : lorsque le signe compte, un nombre est affiché avec un signe plus ou un signe moins ; cependant, lorsqu'il est sûr d'assumer que le nombre est positif, il est affiché sans signe. Les nombres signés sont stockés en utilisant la représentation à complément à deux.

Chaque variant signé peut stocker des nombres allant de -(2`<sup>`{=html}n - 1`</sup>`{=html}) à 2`<sup>`{=html}n - 1`</sup>`{=html} inclus, où _n_ est le nombre de bits que ce variant utilise. Ainsi, un `i8` peut stocker des nombres allant de -(2`<sup>`{=html}7`</sup>`{=html}) à 2`<sup>`{=html}7`</sup>`{=html} - 1, ce qui équivaut à -128 à 127. Les variants non signés peuvent stocker des nombres allant de 0 à 2`<sup>`{=html}n`</sup>`{=html} - 1, donc un `u8` peut stocker des nombres allant de 0 à 2`<sup>`{=html}8`</sup>`{=html} - 1, ce qui équivaut à 0 à 255.

De plus, les types `isize` et `usize` dépendent de l'architecture de l'ordinateur sur lequel votre programme s'exécute, ce qui est indiqué dans le tableau par "architecture" : 64 bits si vous êtes sur une architecture 64 bits et 32 bits si vous êtes sur une architecture 32 bits.

Vous pouvez écrire des littéraux entiers sous n'importe quelle des formes montrées dans le tableau 3-2. Notez que les littéraux numériques qui peuvent être de plusieurs types numériques autorisent un suffixe de type, tel que `57u8`, pour désigner le type. Les littéraux numériques peuvent également utiliser `_` comme séparateur visuel pour faciliter la lecture du nombre, tel que `1_000`, qui aura la même valeur que si vous aviez spécifié `1000`.

Tableau 3-2 : Littéraux entiers en Rust

Littéraux numériques Exemple

---

Décimal `98_222`
Hexadécimal `0xff`
Octal `0o77`
Binaire `0b1111_0000`
Octet (`u8` seulement) `b'A'`

Alors, comment savoir quel type d'entier utiliser? Si vous n'êtes pas sûr, les valeurs par défaut de Rust sont généralement de bonnes bases pour commencer : les types entiers par défaut sont `i32`. La principale situation dans laquelle vous utiliseriez `isize` ou `usize` est lorsque vous indexez une sorte de collection.

> **Dépassement d'entier**
>
> Disons que vous avez une variable de type `u8` qui peut stocker des valeurs entre 0 et 255. Si vous essayez de changer la variable pour une valeur en dehors de cette plage, par exemple 256, un _dépassement d'entier_ se produira, ce qui peut entraîner l'un des deux comportements suivants. Lorsque vous compilez en mode débogage, Rust inclut des vérifications pour le dépassement d'entier qui font en sorte que votre programme _crash_ à l'exécution si ce comportement se produit. Rust utilise le terme _crash_ lorsqu'un programme se termine avec une erreur ; nous aborderons les crashes en détail dans "Erreurs irrécupérables avec panic!".
>
> Lorsque vous compilez en mode release avec le drapeau `--release`, Rust _n'inclut pas_ de vérifications pour le dépassement d'entier qui entraînent des crashes. Au lieu de cela, si un dépassement se produit, Rust effectue un _enroulement au complément à deux_. En bref, les valeurs supérieures à la valeur maximale que le type peut stocker "reviennent" à la valeur minimale que le type peut stocker. Dans le cas d'un `u8`, la valeur 256 devient 0, la valeur 257 devient 1, et ainsi de suite. Le programme ne va pas crash, mais la variable aura une valeur qui n'est probablement pas celle que vous attendiez. Compter sur le comportement d'enroulement du dépassement d'entier est considéré comme une erreur.
>
> Pour gérer explicitement la possibilité de dépassement, vous pouvez utiliser ces familles de méthodes fournies par la bibliothèque standard pour les types numériques primitifs :
>
> - Enrouler dans tous les modes avec les méthodes `wrapping_*`, telles que `wrapping_add`.
> - Retourner la valeur `None` s'il y a dépassement avec les méthodes `checked_*`.
> - Retourner la valeur et un booléen indiquant s'il y a eu dépassement avec les méthodes `overflowing_*`.
> - Saturer à la valeur minimale ou maximale de la valeur avec les méthodes `saturating_*`.
