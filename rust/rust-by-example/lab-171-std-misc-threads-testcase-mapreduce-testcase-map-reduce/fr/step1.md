# Testcase: map-reduce

Rust facilite grandement la parallélisation du traitement des données, sans les nombreux problèmes traditionnellement associés à une telle tentative.

La bibliothèque standard fournit des primitives de threading performantes prêtes à l'emploi. Associées aux concepts de propriété et de règles d'aliasing de Rust, elles empêchent automatiquement les courses de données.

Les règles d'aliasing (une référence modifiable XOR plusieurs références en lecture) vous empêchent automatiquement de manipuler un état visible par d'autres threads. (Lorsque la synchronisation est nécessaire, il existe des primitives de synchronisation telles que les `Mutex` ou les `Channel`.)

Dans cet exemple, nous allons calculer la somme de tous les chiffres dans un bloc de nombres. Nous le ferons en répartissant des morceaux du bloc dans différents threads. Chaque thread additionnera son petit bloc de chiffres, et ensuite, nous additionnerons les sommes intermédiaires produites par chaque thread.

Notez que, bien que nous passons des références à travers les limites des threads, Rust comprend que nous ne passons que des références en lecture seule, et donc qu'aucune insécurité ou course de données ne peut se produire. De plus, parce que les références que nous passons ont des durées de vie `'static`, Rust comprend que nos données ne seront pas détruites tant que ces threads sont toujours en cours d'exécution. (Lorsque vous devez partager des données non `static` entre les threads, vous pouvez utiliser un pointeur intelligent comme `Arc` pour maintenir les données en vie et éviter les durées de vie non `static`.)

```rust
use std::thread;

// Ceci est le thread `main`
fn main() {

    // Ce sont nos données à traiter.
    // Nous allons calculer la somme de tous les chiffres via un algorithme map-reduce multi-threadé.
    // Chaque morceau séparé par un espace sera traité dans un thread différent.
    //
    // TODO: voir ce qui se passe pour la sortie si vous insérez des espaces!
    let data = "86967897737416471853297327050364959
11861322575564723963297542624962850
70856234701860851907960690014725639
38397966707106094172783238747669219
52380795257888236525459303330302837
58495327135744041048897885734297812
69920216438980873548808413720956532
16278424637452589860345374828574668";

    // Créez un vecteur pour stocker les threads enfants que nous allons créer.
    let mut children = vec![];

    /*************************************************************************
     * Phase "Map"
     *
     * Divisez nos données en segments et appliquez le traitement initial
     ************************************************************************/

    // Divisez nos données en segments pour un calcul individuel
    // chaque morceau sera une référence (&str) dans les données réelles
    let chunked_data = data.split_whitespace();

    // Itérez sur les segments de données.
    //.enumerate() ajoute l'index de boucle actuel à ce qui est itéré
    // le tuple résultant "(index, élément)" est ensuite immédiatement
    // "déstructuré" en deux variables, "i" et "data_segment" avec une
    // "affectation par déstructuration"
    for (i, data_segment) in chunked_data.enumerate() {
        println!("segment de données {} est \"{}\"", i, data_segment);

        // Traitez chaque segment de données dans un thread séparé
        //
        // spawn() renvoie un handle vers le nouveau thread,
        // que nous DEVONS conserver pour accéder à la valeur renvoyée
        //
        //'move || -> u32' est la syntaxe pour une closure qui :
        // * ne prend aucun argument ('||')
        // * prend la propriété de ses variables capturées ('move') et
        // * renvoie un entier non signé de 32 bits ('-> u32')
        //
        // Rust est suffisamment intelligent pour déduire le '-> u32' à partir de
        // la closure elle-même, donc nous aurions pu le laisser de côté.
        //
        // TODO: essayez de supprimer le'move' et voir ce qui se passe
        children.push(thread::spawn(move || -> u32 {
            // Calculez la somme intermédiaire de ce segment :
            let result = data_segment
                       // itérez sur les caractères de notre segment..
                     .chars()
                       //.. convertissez les caractères de texte en leur valeur numérique..
                     .map(|c| c.to_digit(10).expect("doit être un chiffre"))
                       //.. et additionnez l'itérateur résultant de nombres
                     .sum();

            // println! verrouille stdout, donc pas d'entrelacement de texte
            println!("segment traité {}, résultat={}", i, result);

            // "return" n'est pas nécessaire, car Rust est un "langage d'expressions", le
            // dernier expression évaluée dans chaque bloc est automatiquement sa valeur.
            result

        }));
    }


    /*************************************************************************
     * Phase "Reduce"
     *
     * Collectez nos résultats intermédiaires et combinez-les en un résultat final
     ************************************************************************/

    // Combinez les résultats intermédiaires de chaque thread en une seule somme finale.
    //
    // Nous utilisons le "turbofish" ::<> pour fournir un indice de type à sum().
    //
    // TODO: essayez sans le turbofish, en spécifiant explicitement
    // le type de final_result
    let final_result = children.into_iter().map(|c| c.join().unwrap()).sum::<u32>();

    println!("Résultat de la somme finale : {}", final_result);
}

```

## Exercices

Il n'est pas sage de laisser le nombre de threads dépendre des données saisies par l'utilisateur. Et si l'utilisateur décide d'insérer beaucoup d'espaces? Voulons-nous vraiment créer 2 000 threads? Modifiez le programme de sorte que les données soient toujours découpées en un nombre limité de segments, défini par une constante statique au début du programme.
