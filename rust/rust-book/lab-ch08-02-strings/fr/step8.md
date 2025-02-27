# Internal Representation

Une `String` est un wrapper sur un `Vec<u8>`. Regardons quelques-unes de nos chaînes d'exemples correctement encodées en UTF-8 de la Liste 8-14. Tout d'abord, celle-ci :

```rust
let hello = String::from("Hola");
```

Dans ce cas, `len` sera `4`, ce qui signifie que le vecteur stockant la chaîne `"Hola"` est de 4 octets de long. Chacune de ces lettres prend un octet lorsqu'elle est encodée en UTF-8. La ligne suivante, cependant, peut vous surprendre (notez que cette chaîne commence par la lettre cyrillique majuscule _Ze_, pas le chiffre arabe 3) :

```rust
let hello = String::from("Здравствуйте");
```

Si vous étiez demandé(e) quelle est la longueur de la chaîne, vous pourriez répondre 12. En fait, la réponse de Rust est 24 : c'est le nombre d'octets nécessaires pour encoder "Здравствуйте" en UTF-8, car chaque valeur scalaire Unicode dans cette chaîne prend 2 octets de stockage. Par conséquent, un indice dans les octets de la chaîne ne correspondra pas toujours à une valeur scalaire Unicode valide. Pour illustrer, considérez ce code Rust invalide :

```rust
let hello = "Здравствуйте";
let answer = &hello[0];
```

Vous savez déjà que `answer` ne sera pas `З`, la première lettre. Lorsqu'elle est encodée en UTF-8, le premier octet de `З` est `208` et le second est `151`, de sorte que l'on pourrait penser que `answer` devrait en fait être `208`, mais `208` n'est pas un caractère valide en soi. Retourner `208` n'est probablement pas ce que le(s) utilisateur(s) voudrait si elle/ils demandaient la première lettre de cette chaîne ; cependant, c'est la seule donnée que Rust a à l'indice d'octet 0. En général, les utilisateurs ne veulent pas que la valeur d'octet soit retournée, même si la chaîne ne contient que des lettres latines : si `&"hello"[0]` était un code valide qui retournait la valeur d'octet, il retournerait `104`, pas `h`.

La réponse, donc, est que pour éviter de retourner une valeur inattendue et de causer des bugs qui pourraient ne pas être découverts immédiatement, Rust ne compile pas ce code du tout et empêche les malentendus dès le début du processus de développement.
