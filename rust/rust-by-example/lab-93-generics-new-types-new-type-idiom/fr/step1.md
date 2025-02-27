# New Type Idiom

L'idiome `newtype` offre des garanties au moment de la compilation pour s'assurer que le bon type de valeur est fourni à un programme.

Par exemple, une fonction de vérification d'âge qui vérifie l'âge en années _doit_ recevoir une valeur de type `Years`.

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// tronque les années fractionnaires
    pub fn to_years(&self) -> Years {
        Years(self.0 / 365)
    }
}

fn old_enough(age: &Years) -> bool {
    age.0 >= 18
}

fn main() {
    let age = Years(5);
    let age_days = age.to_days();
    println!("Old enough {}", old_enough(&age));
    println!("Old enough {}", old_enough(&age_days.to_years()));
    // println!("Old enough {}", old_enough(&age_days));
}
```

Décommentez la dernière instruction `println!` pour constater que le type fourni doit être `Years`.

Pour obtenir la valeur du `newtype` sous forme de type de base, vous pouvez utiliser la syntaxe de tuple ou de décomposition comme ceci :

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // Tuple
    let Years(years_as_primitive_2) = years; // Destructuring
}
```
