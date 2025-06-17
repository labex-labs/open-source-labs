# Types Entiers

Un _entier_ (integer) est un nombre sans composante fractionnaire. Nous avons utilisé un type entier au Chapitre 2, le type `u32`. Cette déclaration de type indique que la valeur qui lui est associée doit être un entier non signé (les types entiers signés commencent par `i` au lieu de `u`) qui occupe 32 bits d'espace. Le Tableau 3-1 montre les types entiers intégrés en Rust. Nous pouvons utiliser n'importe laquelle de ces variantes pour déclarer le type d'une valeur entière.

Tableau 3-1 : Types Entiers en Rust

Longueur Signé Non signé

---

8 bits `i8` `u8`
16 bits `i16` `u16`
32 bits `i32` `u32`
64 bits `i64` `u64`
128 bits `i128` `u128`
arch `isize` `usize`

Chaque variante peut être signée ou non signée et a une taille explicite. _Signé_ (signed) et _non signé_ (unsigned) se réfèrent à la possibilité pour le nombre d'être négatif - en d'autres termes, si le nombre doit avoir un signe avec lui (signé) ou s'il ne sera jamais que positif et peut donc être représenté sans signe (non signé). C'est comme écrire des nombres sur papier : lorsque le signe est important, un nombre est affiché avec un signe plus ou un signe moins ; cependant, lorsqu'il est sûr de supposer que le nombre est positif, il est affiché sans signe. Les nombres signés sont stockés en utilisant la représentation en complément à deux (two's complement).

Chaque variante signée peut stocker des nombres de -(2^(n-1)) à 2^(n-1) - 1 inclus, où _n_ est le nombre de bits que cette variante utilise. Ainsi, un `i8` peut stocker des nombres de -(2^7) à 2^7 - 1, ce qui équivaut à -128 à 127. Les variantes non signées peuvent stocker des nombres de 0 à 2^n - 1, donc un `u8` peut stocker des nombres de 0 à 2^8 - 1, ce qui équivaut à 0 à 255.

De plus, les types `isize` et `usize` dépendent de l'architecture de l'ordinateur sur lequel votre programme s'exécute, ce qui est indiqué dans le tableau par "arch" : 64 bits si vous êtes sur une architecture 64 bits et 32 bits si vous êtes sur une architecture 32 bits.

Vous pouvez écrire des littéraux entiers sous l'une des formes présentées dans le Tableau 3-2. Notez que les littéraux numériques qui peuvent être de plusieurs types numériques autorisent un suffixe de type, tel que `57u8`, pour désigner le type. Les littéraux numériques peuvent également utiliser `_` comme séparateur visuel pour faciliter la lecture du nombre, comme `1_000`, qui aura la même valeur que si vous aviez spécifié `1000`.

Tableau 3-2 : Littéraux Entiers en Rust

Littéraux numériques Exemple

---

Décimal `98_222`
Hexadécimal `0xff`
Octal `0o77`
Binaire `0b1111_0000`
Octet (Byte) (uniquement `u8`) `b'A'`

Alors, comment savoir quel type d'entier utiliser ? Si vous n'êtes pas sûr, les valeurs par défaut de Rust sont généralement de bons points de départ : les types entiers sont par défaut `i32`. La principale situation dans laquelle vous utiliseriez `isize` ou `usize` est lors de l'indexation d'une sorte de collection.

> **Dépassement de capacité (Integer Overflow)**
>
> Disons que vous avez une variable de type `u8` qui peut contenir des valeurs entre 0 et 255. Si vous essayez de changer la variable en une valeur en dehors de cette plage, comme 256, un _dépassement de capacité_ (integer overflow) se produira, ce qui peut entraîner l'un des deux comportements. Lorsque vous compilez en mode débogage, Rust inclut des vérifications de dépassement de capacité qui font que votre programme _panique_ (panic) au moment de l'exécution si ce comportement se produit. Rust utilise le terme _paniquer_ (panicking) lorsqu'un programme se termine avec une erreur ; nous discuterons des paniques plus en détail dans "Erreurs irrécupérables avec panic!".
>
> Lorsque vous compilez en mode release avec l'indicateur `--release`, Rust n'inclut _pas_ de vérifications de dépassement de capacité qui provoquent des paniques. Au lieu de cela, si un dépassement de capacité se produit, Rust effectue un _wrapping en complément à deux_ (two's complement wrapping). En bref, les valeurs supérieures à la valeur maximale que le type peut contenir "s'enroulent" (wrap around) vers le minimum des valeurs que le type peut contenir. Dans le cas d'un `u8`, la valeur 256 devient 0, la valeur 257 devient 1, et ainsi de suite. Le programme ne paniquera pas, mais la variable aura une valeur qui n'est probablement pas celle que vous attendiez. Se fier au comportement d'enroulement du dépassement de capacité est considéré comme une erreur.
>
> Pour gérer explicitement la possibilité d'un dépassement de capacité, vous pouvez utiliser ces familles de méthodes fournies par la bibliothèque standard pour les types numériques primitifs :
>
> - Enrouler dans tous les modes avec les méthodes `wrapping_*`, telles que `wrapping_add`.
> - Retourner la valeur `None` s'il y a dépassement de capacité avec les méthodes `checked_*`.
> - Retourner la valeur et un booléen indiquant s'il y a eu dépassement de capacité avec les méthodes `overflowing_*`.
> - Saturer aux valeurs minimales ou maximales de la valeur avec les méthodes `saturating_*`.
