# Assemblage en ligne

Rust prend en charge l'assemblage en ligne via le macro `asm!`. Il peut être utilisé pour intégrer un assemblage écrit à la main dans la sortie d'assemblage générée par le compilateur. Généralement, cela ne devrait pas être nécessaire, mais peut l'être dans les cas où les performances ou le chronométrage requis ne peuvent pas être obtenus autrement. L'accès à des primitives matérielles de bas niveau, par exemple dans le code du noyau, peut également nécessiter cette fonctionnalité.

> **Note** : les exemples ici sont donnés en assemblage x86/x86-64, mais d'autres architectures sont également prises en charge.

L'assemblage en ligne est actuellement pris en charge sur les architectures suivantes :

- x86 et x86-64
- ARM
- AArch64
- RISC-V

## Utilisation de base

Commencons par l'exemple le plus simple possible :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

unsafe {
    asm!("nop");
}
# }
```

Cela insérera une instruction NOP (no operation) dans l'assemblage généré par le compilateur. Notez que toutes les invo cations de `asm!` doivent être dans un bloc `unsafe`, car elles pourraient insérer des instructions arbitraires et casser diverses invariants. Les instructions à insérer sont listées dans le premier argument du macro `asm!` sous forme de littéral de chaîne.

## Entrées et sorties

Maintenant, insérer une instruction qui ne fait rien est plutôt ennuyeux. Faisons quelque chose qui agit réellement sur les données :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64;
unsafe {
    asm!("mov {}, 5", out(reg) x);
}
assert_eq!(x, 5);
# }
```

Cela écrira la valeur `5` dans la variable `u64` `x`. Vous pouvez voir que la littéral de chaîne que nous utilisons pour spécifier les instructions est en fait une chaîne de modèle. Elle est gouvernée par les mêmes règles que les chaînes de format Rust. Les arguments qui sont insérés dans le modèle ont cependant un aspect un peu différent de ce avec quoi vous êtes peut-être familier. Tout d'abord, nous devons spécifier si la variable est une entrée ou une sortie de l'assemblage en ligne. Dans ce cas, il s'agit d'une sortie. Nous l'avons déclarée en écrivant `out`. Nous devons également spécifier dans quel type de registre l'assemblage attend la variable. Dans ce cas, nous la plaçons dans un registre général quelconque en spécifiant `reg`. Le compilateur choisira un registre approprié pour insérer dans le modèle et lira la variable à partir de là une fois que l'assemblage en ligne aura fini d'exécuter.

Voyons un autre exemple qui utilise également une entrée :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let i: u64 = 3;
let o: u64;
unsafe {
    asm!(
        "mov {0}, {1}",
        "add {0}, 5",
        out(reg) o,
        in(reg) i,
    );
}
assert_eq!(o, 8);
# }
```

Cela ajoutera `5` à l'entrée dans la variable `i` et écrira le résultat dans la variable `o`. La manière particulière dont cet assemblage le fait est d'abord de copier la valeur de `i` dans la sortie, puis d'y ajouter `5`.

L'exemple montre plusieurs choses :

Tout d'abord, nous pouvons voir que `asm!` permet plusieurs arguments de chaîne de modèle ; chacun est traité comme une ligne séparée de code d'assemblage, comme s'ils étaient tous joints ensemble avec des sauts de ligne entre eux. Cela facilite la mise en forme du code d'assemblage.

Deuxièmement, nous pouvons voir que les entrées sont déclarées en écrivant `in` au lieu de `out`.

Troisièmement, nous pouvons voir que nous pouvons spécifier un numéro d'argument, ou un nom comme dans n'importe quelle chaîne de format. Pour les modèles d'assemblage en ligne, cela est particulièrement utile car les arguments sont souvent utilisés plusieurs fois. Pour un assemblage en ligne plus complexe, il est généralement recommandé d'utiliser cette fonctionnalité, car elle améliore la lisibilité et permet de réordonner les instructions sans changer l'ordre des arguments.

Nous pouvons raffiner davantage l'exemple ci-dessus pour éviter l'instruction `mov` :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u64 = 3;
unsafe {
    asm!("add {0}, 5", inout(reg) x);
}
assert_eq!(x, 8);
# }
```

Nous pouvons voir que `inout` est utilisé pour spécifier un argument qui est à la fois une entrée et une sortie. Cela est différent de spécifier une entrée et une sortie séparément en ce sens qu'il est garanti d'affecter les deux au même registre.

Il est également possible de spécifier des variables différentes pour les parties d'entrée et de sortie d'un opérande `inout` :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64 = 3;
let y: u64;
unsafe {
    asm!("add {0}, 5", inout(reg) x => y);
}
assert_eq!(y, 8);
# }
```

## Opérandes de sortie tardive

Le compilateur Rust est prudent dans son allocation d'opérandes. Il est supposé qu'une `out` peut être écrite à tout moment et ne peut donc pas partager sa position avec aucun autre argument. Cependant, pour garantir des performances optimales, il est important d'utiliser le moins de registres possible, de sorte qu'ils n'aient pas à être sauvegardés et rechargés autour du bloc d'assemblage en ligne. Pour y arriver, Rust fournit un spécificateur `lateout`. Cela peut être utilisé pour toute sortie qui n'est écrite qu'après que toutes les entrées ont été consommées. Il existe également une variante `inlateout` de ce spécificateur.

Voici un exemple où `inlateout` _ne peut pas_ être utilisé en mode `release` ou dans d'autres cas optimisés :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
let c: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        "add {0}, {2}",
        inout(reg) a,
        in(reg) b,
        in(reg) c,
    );
}
assert_eq!(a, 12);
# }
```

Le précédent pourrait fonctionner bien dans des cas non optimisés (`Debug` mode), mais si vous voulez des performances optimisées (`release` mode ou d'autres cas optimisés), cela ne pourrait pas fonctionner.

Cela est parce que dans des cas optimisés, le compilateur est libre d'allouer le même registre pour les entrées `b` et `c` car il sait qu'elles ont la même valeur. Cependant, il doit allouer un registre séparé pour `a` car il utilise `inout` et non `inlateout`. Si `inlateout` avait été utilisé, alors `a` et `c` pourraient être alloués au même registre, auquel cas la première instruction pour écraser la valeur de `c` ferait en sorte que le code d'assemblage produise le résultat incorrect.

Cependant, l'exemple suivant peut utiliser `inlateout` car la sortie n'est modifiée que après que tous les registres d'entrée ont été lus :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!("add {0}, {1}", inlateout(reg) a, in(reg) b);
}
assert_eq!(a, 8);
# }
```

Comme vous pouvez le voir, ce fragment d'assemblage fonctionnera toujours correctement si `a` et `b` sont assignés au même registre.

## Opérandes de registre explicites

Certaines instructions nécessitent que les opérandes soient dans un registre spécifique. Par conséquent, l'assemblage en ligne Rust fournit des spécificateurs de contrainte plus spécifiques. Alors que `reg` est généralement disponible sur n'importe quelle architecture, les registres explicites sont fortement spécifiques à l'architecture. Par exemple, pour x86, les registres généraux `eax`, `ebx`, `ecx`, `edx`, `ebp`, `esi` et `edi` peuvent être adressés par leur nom.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let cmd = 0xd1;
unsafe {
    asm!("out 0x64, eax", in("eax") cmd);
}
# }
```

Dans cet exemple, nous appelons l'instruction `out` pour sortir le contenu de la variable `cmd` sur le port `0x64`. Puisque l'instruction `out` ne prend que `eax` (et ses sous-registres) comme opérande, nous avons dû utiliser le spécificateur de contrainte `eax`.

> **Note** : contrairement à d'autres types d'opérandes, les opérandes de registre explicites ne peuvent pas être utilisés dans la chaîne de modèle : vous ne pouvez pas utiliser `{}` et devriez écrire le nom du registre directement à la place. De plus, ils doivent apparaître à la fin de la liste d'opérandes après tous les autres types d'opérandes.

Considérez cet exemple qui utilise l'instruction `mul` x86 :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn mul(a: u64, b: u64) -> u128 {
    let lo: u64;
    let hi: u64;

    unsafe {
        asm!(
            // L'instruction mul x86 prend rax comme entrée implicite et écrit
            // le résultat de la multiplication sur 128 bits dans rax:rdx.
            "mul {}",
            in(reg) a,
            inlateout("rax") b => lo,
            lateout("rdx") hi
        );
    }

    ((hi as u128) << 64) + lo as u128
}
# }
```

Cela utilise l'instruction `mul` pour multiplier deux entrées sur 64 bits avec un résultat sur 128 bits. L'unique opérande explicite est un registre, que nous remplissons à partir de la variable `a`. Le second opérande est implicite et doit être le registre `rax`, que nous remplissons à partir de la variable `b`. Les 64 bits inférieurs du résultat sont stockés dans `rax` à partir duquel nous remplissons la variable `lo`. Les 64 bits supérieurs sont stockés dans `rdx` à partir duquel nous remplissons la variable `hi`.

## Registres modifiés

Dans de nombreux cas, l'assemblage en ligne modifiera l'état qui n'est pas nécessaire en tant que sortie. Généralement, c'est soit parce que nous devons utiliser un registre temporaire dans l'assemblage soit parce que les instructions modifient l'état que nous n'avons pas besoin d'examiner plus avant. Cet état est généralement appelé être "modifié". Nous devons le dire au compilateur car il peut devoir sauvegarder et restaurer cet état autour du bloc d'assemblage en ligne.

```rust
use std::arch::asm;

# #[cfg(target_arch = "x86_64")]
fn main() {
    // trois entrées de quatre octets chacune
    let mut name_buf = [0_u8; 12];
    // La chaîne est stockée en ASCII dans ebx, edx, ecx dans cet ordre
    // Comme ebx est réservé, l'asm doit préserver la valeur de celui-ci.
    // Donc, nous l'empilons et le dépilons autour de l'asm principal.
    // Le mode 64 bits sur les processeurs 64 bits ne permet pas d'empiler/dépiler
    // des registres 32 bits (comme ebx), donc nous devons utiliser le registre rbx étendu à la place.

    unsafe {
        asm!(
            "push rbx",
            "cpuid",
            "mov [rdi], ebx",
            "mov [rdi + 4], edx",
            "mov [rdi + 8], ecx",
            "pop rbx",
            // Nous utilisons un pointeur vers un tableau pour stocker les valeurs pour simplifier
            // le code Rust au détriment de quelques instructions d'assemblage supplémentaires
            // Cela est plus explicite sur la manière dont l'asm fonctionne cependant, contrairement
            // aux sorties de registre explicites telles que `out("ecx") val`
            // Le *pointeur lui-même* n'est qu'une entrée même s'il est écrit derrière
            in("rdi") name_buf.as_mut_ptr(),
            // Sélectionnez cpuid 0, également spécifiez eax comme modifié
            inout("eax") 0 => _,
            // cpuid modifie également ces registres
            out("ecx") _,
            out("edx") _,
        );
    }

    let name = core::str::from_utf8(&name_buf).unwrap();
    println!("CPU Manufacturer ID: {}", name);
}

# #[cfg(not(target_arch = "x86_64"))]
# fn main() {}
```

Dans l'exemple ci-dessus, nous utilisons l'instruction `cpuid` pour lire l'ID du fabricant du CPU. Cette instruction écrit dans `eax` avec l'argument `cpuid` maximal supporté et dans `ebx`, `edx` et `ecx` avec l'ID du fabricant du CPU sous forme d'octets ASCII dans cet ordre.

Même si `eax` n'est jamais lu, nous devons toujours dire au compilateur que le registre a été modifié afin que le compilateur puisse sauvegarder toutes les valeurs qui étaient dans ces registres avant l'asm. Cela se fait en le déclarant comme une sortie mais avec `_` au lieu d'un nom de variable, ce qui indique que la valeur de sortie doit être rejetée.

Ce code contourne également la limitation selon laquelle `ebx` est un registre réservé par LLVM. Cela signifie que LLVM suppose qu'il a le contrôle total sur le registre et qu'il doit être restauré à son état initial avant de quitter le bloc d'asm, donc il ne peut pas être utilisé comme entrée ou sortie **sauf** si le compilateur l'utilise pour remplir une classe de registre générale (par exemple `in(reg)`). Cela rend les opérandes `reg` dangereuses lorsqu'on utilise des registres réservés car nous pourrions accidentellement corrompre notre entrée ou notre sortie car ils partagent le même registre.

Pour contourner cela, nous utilisons `rdi` pour stocker le pointeur vers le tableau de sortie, sauvegardons `ebx` via `push`, lisons à partir de `ebx` dans le bloc d'asm dans le tableau puis restaurons `ebx` à son état initial via `pop`. Les `push` et `pop` utilisent la version 64 bits complète du registre `rbx` pour vous assurer que l'ensemble du registre est sauvegardé. Sur des cibles 32 bits, le code utiliserait `ebx` dans le `push`/`pop` à la place.

Cela peut également être utilisé avec une classe de registre générale pour obtenir un registre temporaire pour être utilisé dans le code d'asm :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

// Multipliez x par 6 en utilisant des décalages et des additions
let mut x: u64 = 4;
unsafe {
    asm!(
        "mov {tmp}, {x}",
        "shl {tmp}, 1",
        "shl {x}, 2",
        "add {x}, {tmp}",
        x = inout(reg) x,
        tmp = out(reg) _,
    );
}
assert_eq!(x, 4 * 6);
# }
```

## Opérandes de symbole et modifications ABI

Par défaut, `asm!` suppose que tout registre non spécifié comme une sortie aura son contenu préservé par le code d'assemblage. L'argument \[`clobber_abi`\] de `asm!` indique au compilateur d'insérer automatiquement les opérandes de modification nécessaires selon la convention d'appel ABI donnée : tout registre qui n'est pas entièrement préservé dans cette ABI sera considéré comme modifié. Plusieurs arguments `clobber_abi` peuvent être fournis et toutes les modifications de toutes les ABIs spécifiées seront insérées.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

extern "C" fn foo(arg: i32) -> i32 {
    println!("arg = {}", arg);
    arg * 2
}

fn call_foo(arg: i32) -> i32 {
    unsafe {
        let result;
        asm!(
            "call {}",
            // Pointeur de fonction à appeler
            in(reg) foo,
            // 1er argument dans rdi
            in("rdi") arg,
            // Valeur de retour dans rax
            out("rax") result,
            // Marquez tous les registres qui ne sont pas préservés par la convention d'appel
            // "C" comme modifiés.
            clobber_abi("C"),
        );
        result
    }
}
# }
```

## Modificateurs de modèle de registre

Dans certains cas, une commande fine est nécessaire sur la manière dont un nom de registre est formaté lorsqu'il est inséré dans la chaîne de modèle. Cela est nécessaire lorsque le langage d'assemblage d'une architecture a plusieurs noms pour le même registre, chacun étant généralement une "vue" sur un sous-ensemble du registre (par exemple, les 32 bits inférieurs d'un registre 64 bits).

Par défaut, le compilateur choisira toujours le nom qui fait référence à la taille totale du registre (par exemple, `rax` sur x86-64, `eax` sur x86, etc).

Ceci peut être remplacé en utilisant des modificateurs sur les opérandes de chaîne de modèle, tout comme vous le feriez avec des chaînes de format :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u16 = 0xab;

unsafe {
    asm!("mov {0:h}, {0:l}", inout(reg_abcd) x);
}

assert_eq!(x, 0xabab);
# }
```

Dans cet exemple, nous utilisons la classe de registre `reg_abcd` pour restreindre l'allocateur de registre aux 4 anciens registres x86 (`ax`, `bx`, `cx`, `dx`) dont les deux premiers octets peuvent être adressés indépendamment.

Supposons que l'allocateur de registres ait choisi d'allouer `x` dans le registre `ax`. Le modificateur `h` émettra le nom du registre pour le haut octet de ce registre et le modificateur `l` émettra le nom du registre pour le bas octet. Le code d'assemblage sera donc étendu en `mov ah, al` qui copie le bas octet de la valeur dans le haut octet.

Si vous utilisez un type de données plus petit (par exemple, `u16`) avec un opérande et oubliez d'utiliser des modificateurs de modèle, le compilateur émettra un avertissement et suggérera le modificateur correct à utiliser.

## Opérandes d'adresse mémoire

Parfois, les instructions d'assemblage nécessitent des opérandes passées via des adresses mémoire/emplacements mémoire. Vous devrez manuellement utiliser la syntaxe d'adresse mémoire spécifiée par l'architecture cible. Par exemple, sur x86/x86_64 en utilisant la syntaxe d'assemblage Intel, vous devriez entourer les entrées/sorties de `[]` pour indiquer qu'il s'agit d'opérandes mémoire :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn load_fpu_control_word(control: u16) {
    unsafe {
        asm!("fldcw [{}]", in(reg) &control, options(nostack));
    }
}
# }
```

## Etiquettes

Toute réutilisation d'une étiquette nommée, locale ou non, peut entraîner une erreur d'assembleur ou de lieur ou peut causer d'autres comportements étranges. La réutilisation d'une étiquette nommée peut se produire de diverses manières, y compris :

- explicitement : en utilisant une étiquette plusieurs fois dans un bloc `asm!`, ou plusieurs fois dans différents blocs.
- implicitement via l'inlining : le compilateur est autorisé à instancier plusieurs copies d'un bloc `asm!`, par exemple lorsque la fonction le contenant est en ligne dans plusieurs emplacements.
- implicitement via LTO : LTO peut entraîner le placement du code de _d'autres crates_ dans la même unité de génération de code, et pourrait donc introduire des étiquettes arbitraires.

En conséquence, vous devriez seulement utiliser des \[étiquettes locales numériques\] de l'assembleur GNU à l'intérieur du code d'assemblage en ligne. La définition de symboles dans le code d'assemblage peut entraîner des erreurs d'assembleur et/ou de lieur en raison de définitions de symboles dupliquées.

De plus, sur x86, lorsqu'on utilise la syntaxe Intel par défaut, en raison d'un \[bogue LLVM\], vous ne devriez pas utiliser des étiquettes constituées exclusivement de chiffres `0` et `1`, par exemple `0`, `11` ou `101010`, car elles risquent d'être interprétées comme des valeurs binaires. L'utilisation de `options(att_syntax)` évitera toute ambiguïté, mais cela affecte la syntaxe de _tout_ le bloc `asm!`. (Voir [Options](#options), ci-dessous, pour en savoir plus sur `options`.)

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a = 0;
unsafe {
    asm!(
        "mov {0}, 10",
        "2:",
        "sub {0}, 1",
        "cmp {0}, 3",
        "jle 2f",
        "jmp 2b",
        "2:",
        "add {0}, 2",
        out(reg) a
    );
}
assert_eq!(a, 5);
# }
```

Cela diminuera la valeur du registre `{0}` de 10 à 3, puis ajoutera 2 et la stockera dans `a`.

Cet exemple montre plusieurs choses :

- Tout d'abord, qu'un même nombre peut être utilisé comme étiquette plusieurs fois dans le même bloc d'assemblage en ligne.
- Deuxièmement, que lorsqu'une étiquette numérique est utilisée comme référence (par exemple, en tant qu'opérande d'instruction), les suffixes "b" ("vers l'arrière") ou "f" ("vers l'avant") devraient être ajoutés à l'étiquette numérique. Elle se référera alors à la plus proche étiquette définie par ce nombre dans cette direction.

## Options

Par défaut, un bloc d'assemblage en ligne est traité de la même manière qu'un appel de fonction FFI externe avec une convention d'appel personnalisée : il peut lire/écrire dans la mémoire, avoir des effets de bord observables, etc. Cependant, dans de nombreux cas, il est souhaitable de fournir plus d'informations au compilateur sur ce que le code d'assemblage fait réellement afin qu'il puisse optimiser mieux.

Prenons notre exemple précédent d'une instruction `add` :

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        inlateout(reg) a, in(reg) b,
        options(pure, nomem, nostack),
    );
}
assert_eq!(a, 8);
# }
```

Les options peuvent être fournies en tant qu'argument final optionnel du macro `asm!`. Nous avons spécifié trois options ici :

- `pure` signifie que le code d'assemblage n'a pas d'effets de bord observables et que sa sortie dépend seulement de ses entrées. Cela permet au compilateur d'optimiser d'appeler le code d'assemblage en ligne moins souvent ou même de l'éliminer complètement.
- `nomem` signifie que le code d'assemblage ne lit ni n'écrit dans la mémoire. Par défaut, le compilateur supposera que l'assemblage en ligne peut lire ou écrire n'importe quelle adresse mémoire accessible à lui (par exemple, via un pointeur passé en tant qu'opérande, ou une variable globale).
- `nostack` signifie que le code d'assemblage n'empile aucun données sur la pile. Cela permet au compilateur d'utiliser des optimisations telles que la zone rouge de pile sur x86-64 pour éviter les ajustements du pointeur de pile.

Cela permet au compilateur d'optimiser mieux le code utilisant `asm!`, par exemple en éliminant les blocs `asm!` purs dont les sorties ne sont pas nécessaires.

Voir la [référence](https://doc.rust-lang.org/stable/reference/inline-assembly.html) pour la liste complète des options disponibles et de leurs effets.
