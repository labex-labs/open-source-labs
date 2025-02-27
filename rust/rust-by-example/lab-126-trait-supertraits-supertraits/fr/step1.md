# Supertraits

Rust n'a pas d'"héritage", mais vous pouvez définir un trait comme étant un superensemble d'un autre trait. Par exemple :

```rust
trait Person {
    fn name(&self) -> String;
}

// Person est un supertrait de Student.
// Implémenter Student nécessite également d'implémenter Person.
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent (étudiant en informatique) est un sous-trait à la fois de Programmer
// et de Student. Implémenter CompSciStudent nécessite d'implémenter les deux supertraits.
trait CompSciStudent: Programmer + Student {
    fn git_username(&self) -> String;
}

fn comp_sci_student_greeting(student: &dyn CompSciStudent) -> String {
    format!(
        "My name is {} and I attend {}. My favorite language is {}. My Git username is {}",
        student.name(),
        student.university(),
        student.fav_language(),
        student.git_username()
    )
}

fn main() {}
```
