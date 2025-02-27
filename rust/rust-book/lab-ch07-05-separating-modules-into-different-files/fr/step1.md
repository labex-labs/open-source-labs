# Séparer les modules dans des fichiers différents

Jusqu'à présent, tous les exemples de ce chapitre ont défini plusieurs modules dans un seul fichier. Lorsque les modules deviennent volumineux, vous pouvez vouloir déplacer leurs définitions dans un fichier séparé pour faciliter la navigation dans le code.

Par exemple, commençons par le code de la Liste 7-17 qui avait plusieurs modules de restaurant. Nous allons extraire les modules dans des fichiers au lieu d'avoir tous les modules définis dans le fichier racine de la boîte à outils. Dans ce cas, le fichier racine de la boîte à outils est `src/lib.rs`, mais cette procédure fonctionne également avec les boîtes à outils binaires dont le fichier racine de la boîte à outils est `src/main.rs`.

Tout d'abord, nous allons extraire le module `front_of_house` dans son propre fichier. Supprimez le code à l'intérieur des accolades pour le module `front_of_house`, ne laissant que la déclaration `mod front_of_house;`, de sorte que `src/lib.rs` contienne le code montré dans la Liste 7-21. Notez que cela ne compilera pas tant que vous n'aurez pas créé le fichier `src/front_of_house.rs` de la Liste 7-22.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Liste 7-21 : Déclaration du module `front_of_house` dont le corps sera dans `src/front_of_house.rs`

Ensuite, placez le code qui était à l'intérieur des accolades dans un nouveau fichier nommé `src/front_of_house.rs`, comme montré dans la Liste 7-22. Le compilateur sait où chercher dans ce fichier car il a rencontré la déclaration de module dans la racine de la boîte à outils avec le nom `front_of_house`.

Nom de fichier : `src/front_of_house.rs`

```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

Liste 7-22 : Définitions à l'intérieur du module `front_of_house` dans `src/front_of_house.rs`

Notez que vous n'avez besoin de charger un fichier qu'une seule fois dans votre arborescence de modules en utilisant une déclaration `mod`. Une fois que le compilateur sait que le fichier est une partie du projet (et sait où dans l'arborescence de modules se trouve le code en fonction de l'endroit où vous avez placé l'instruction `mod`), les autres fichiers de votre projet devraient faire référence au code du fichier chargé en utilisant un chemin vers l'endroit où il a été déclaré, comme décrit dans "Chemins pour faire référence à un élément dans l'arborescence de modules". En d'autres termes, `mod` n'est pas une opération d'"inclusion" que vous avez peut-être vue dans d'autres langages de programmation.

Ensuite, nous allons extraire le module `hosting` dans son propre fichier. Le processus est un peu différent car `hosting` est un module enfant de `front_of_house`, pas du module racine. Nous placerons le fichier pour `hosting` dans un nouveau répertoire qui portera le nom de ses ancêtres dans l'arborescence de modules, dans ce cas _src/front_of_house_.

Pour commencer à déplacer `hosting`, nous modifions `src/front_of_house.rs` pour ne contenir que la déclaration du module `hosting` :

Nom de fichier : `src/front_of_house.rs`

```rust
pub mod hosting;
```

Ensuite, nous créons un répertoire `src/front_of_house` et un fichier `hosting.rs` pour contenir les définitions faites dans le module `hosting` :

Nom de fichier : `src/front_of_house/hosting.rs`

```rust
pub fn add_to_waitlist() {}
```

Si nous plaçons au contraire `hosting.rs` dans le répertoire `src`, le compilateur s'attendra à ce que le code de `hosting.rs` soit dans un module `hosting` déclaré dans la racine de la boîte à outils, et non déclaré comme un module enfant de `front_of_house`. Les règles du compilateur pour savoir quels fichiers vérifier pour le code de quel module signifient que les répertoires et les fichiers correspondent plus étroitement à l'arborescence de modules.

> **Chemins de fichiers alternatifs**
>
> Jusqu'à présent, nous avons abordé les chemins de fichiers les plus idiomatiques utilisés par le compilateur Rust, mais Rust prend également en charge un style plus ancien de chemin de fichier. Pour un module nommé `front_of_house` déclaré dans la racine de la boîte à outils, le compilateur cherchera le code du module dans :
>
> - `src/front_of_house.rs` (ce que nous avons vu)
> - `src/front_of_house/mod.rs` (ancien style, chemin toujours pris en charge)
>
> Pour un module nommé `hosting` qui est un sous-module de `front_of_house`, le compilateur cherchera le code du module dans :
>
> - `src/front_of_house/hosting.rs` (ce que nous avons vu)
> - `src/front_of_house/hosting/mod.rs` (ancien style, chemin toujours pris en charge)
>
> Si vous utilisez les deux styles pour le même module, vous obtiendrez une erreur du compilateur. Il est possible d'utiliser un mélange des deux styles pour différents modules dans le même projet, mais cela peut être confus pour les personnes qui naviguent dans votre projet.
>
> Le principal inconvénient du style qui utilise des fichiers nommés `mod.rs` est que votre projet peut finir par avoir de nombreux fichiers nommés `mod.rs`, ce qui peut être confus lorsque vous les avez ouverts dans votre éditeur en même temps.

Nous avons déplacé le code de chaque module dans un fichier séparé, et l'arborescence de modules reste la même. Les appels de fonction dans `eat_at_restaurant` fonctionneront sans modification, même si les définitions se trouvent dans des fichiers différents. Cette technique vous permet de déplacer les modules vers de nouveaux fichiers à mesure qu'ils grandissent.

Notez que l'instruction `pub use crate::front_of_house::hosting` dans `src/lib.rs` n'a pas non plus changé, ni `use` n'a d'impact sur les fichiers qui sont compilés en tant que partie de la boîte à outils. Le mot clé `mod` déclare les modules, et Rust cherche dans un fichier ayant le même nom que le module pour le code qui va dans ce module.
