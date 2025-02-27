# Paramètres de type fantôme

Un paramètre de type fantôme est un paramètre qui ne s'affiche pas au moment de l'exécution, mais est vérifié statiquement (et seulement) au moment de la compilation.

Les types de données peuvent utiliser des paramètres de type génériques supplémentaires pour servir de marqueurs ou pour effectuer des vérifications de type au moment de la compilation. Ces paramètres supplémentaires ne contiennent pas de valeurs de stockage et n'ont aucun comportement exécuté au moment de l'exécution.

Dans l'exemple suivant, nous combinons \[std::marker::PhantomData\] avec le concept de paramètre de type fantôme pour créer des tuples contenant différents types de données.

```rust
use std::marker::PhantomData;

// Une struct de tuple fantôme qui est générique sur `A` avec un paramètre caché `B`.
#[derive(PartialEq)] // Autorise le test d'égalité pour ce type.
struct PhantomTuple<A, B>(A, PhantomData<B>);

// Une struct de type fantôme qui est générique sur `A` avec un paramètre caché `B`.
#[derive(PartialEq)] // Autorise le test d'égalité pour ce type.
struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }

// Note : La mémoire est allouée pour le type générique `A`, mais pas pour `B`.
//       Par conséquent, `B` ne peut pas être utilisé dans les calculs.

fn main() {
    // Ici, `f32` et `f64` sont les paramètres cachés.
    // Le type PhantomTuple spécifié comme `<char, f32>`.
    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);
    // Le type PhantomTuple spécifié comme `<char, f64>`.
    let _tuple2: PhantomTuple<char, f64> = PhantomTuple('Q', PhantomData);

    // Le type spécifié comme `<char, f32>`.
    let _struct1: PhantomStruct<char, f32> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };
    // Le type spécifié comme `<char, f64>`.
    let _struct2: PhantomStruct<char, f64> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };

    // Erreur de compilation! Les types ne correspondent pas, donc on ne peut pas les comparer :
    // println!("_tuple1 == _tuple2 donne : {}",
    //           _tuple1 == _tuple2);

    // Erreur de compilation! Les types ne correspondent pas, donc on ne peut pas les comparer :
    // println!("_struct1 == _struct2 donne : {}",
    //           _struct1 == _struct2);
}
```
