# Testcase: unit clarification

Une méthode utile de conversions d'unités peut être examinée en implémentant `Add` avec un paramètre de type fantôme. Le trait `Add` est examiné ci-dessous :

```rust
// Cette construction imposerait : `Self + RHS = Output`
// où RHS est la valeur par défaut de Self si elle n'est pas spécifiée dans l'implémentation.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` doit être `T<U>` pour que `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
  ...
}
```

L'implémentation complète :

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// Crée des énumérations vides pour définir les types d'unités.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` est un type avec un paramètre de type fantôme `Unit`,
/// et n'est pas générique sur le type de longueur (c'est-à-dire `f64`).
///
/// `f64` implémente déjà les traits `Clone` et `Copy`.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// Le trait `Add` définit le comportement de l'opérateur `+`.
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() renvoie une nouvelle structure `Length` contenant la somme.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` appelle l'implémentation de `Add` pour `f64`.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // Spécifie que `one_foot` a un paramètre de type fantôme `Inch`.
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` a un paramètre de type fantôme `Mm`.
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` appelle la méthode `add()` que nous avons implémentée pour `Length<Unit>`.
    //
    // Étant donné que `Length` implémente `Copy`, `add()` ne consomme pas
    // `one_foot` et `one_meter` mais les copie dans `self` et `rhs`.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // L'addition fonctionne.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // Les opérations absurdes échouent comme elles devraient :
    // Erreur de compilation : mismatch de type.
    //let one_feter = one_foot + one_meter;
}
```
