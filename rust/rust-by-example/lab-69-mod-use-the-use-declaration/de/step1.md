# Die `use`-Anweisung

Die `use`-Anweisung kann verwendet werden, um einen vollständigen Pfad an einen neuen Namen zu binden, um den Zugang zu erleichtern. Sie wird oft so verwendet:

```rust
use crate::deeply::nested::{
    my_first_function,
    my_second_function,
    AndATraitType
};

fn main() {
    my_first_function();
}
```

Sie können das `as`-Schlüsselwort verwenden, um Imports an einen anderen Namen zu binden:

```rust
// Binde den Pfad `deeply::nested::function` an `other_function`.
use deeply::nested::function as other_function;

fn function() {
    println!("called `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("called `deeply::nested::function()`");
        }
    }
}

fn main() {
    // Einfacherer Zugang zu `deeply::nested::function`
    other_function();

    println!("Entering block");
    {
        // Dies ist äquivalent zu `use deeply::nested::function as function`.
        // Diese `function()` wird die äußere überschreiben.
        use crate::deeply::nested::function;

        // `use`-Bindungen haben einen lokalen Gültigkeitsbereich. In diesem Fall
        // ist das Überschreiben von `function()` nur in diesem Block.
        function();

        println!("Leaving block");
    }

    function();
}
```
