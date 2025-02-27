# La différence entre les macros et les fonctions

Fondamentalement, les macros sont un moyen d'écrire du code qui écrit autre code, ce qui est connu sous le nom de _métaprogrammation_. Dans l'annexe C, nous discutons de l'attribut `derive`, qui génère une implémentation de divers traits pour vous. Nous avons également utilisé les macros `println!` et `vec!` tout au long du livre. Toutes ces macros _s'étendent_ pour produire plus de code que le code que vous avez écrit manuellement.

La métaprogrammation est utile pour réduire la quantité de code que vous devez écrire et maintenir, ce qui est également l'un des rôles des fonctions. Cependant, les macros ont quelques pouvoirs additionnels que les fonctions n'ont pas.

La signature d'une fonction doit déclarer le nombre et le type des paramètres que la fonction a. Les macros, en revanche, peuvent prendre un nombre variable de paramètres : nous pouvons appeler `println!("hello")` avec un argument ou `println!("hello {}", name)` avec deux arguments. De plus, les macros sont étendues avant que le compilateur n'interprète le sens du code, donc une macro peut, par exemple, implémenter un trait sur un type donné. Une fonction ne peut pas, car elle est appelée à l'exécution et un trait doit être implémenté à la compilation.

Le désavantage d'utiliser une macro plutôt qu'une fonction est que les définitions de macros sont plus complexes que les définitions de fonctions car vous écrivez du code Rust qui écrit du code Rust. En raison de cette indirection, les définitions de macros sont généralement plus difficiles à lire, à comprendre et à maintenir que les définitions de fonctions.

Une autre différence importante entre les macros et les fonctions est que vous devez définir les macros ou les porter dans le contexte _avant_ de les appeler dans un fichier, contrairement aux fonctions que vous pouvez définir n'importe où et appeler n'importe où.
