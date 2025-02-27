# Superrasgos

Rust no tiene "herencia", pero puede definir un rasgo como un superconjunto de otro rasgo. Por ejemplo:

```rust
trait Person {
    fn name(&self) -> String;
}

// Person es un superrasgo de Student.
// Implementar Student requiere que también implementes Person.
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent (estudiante de informática) es un subtipo de tanto Programmer
// como Student. Implementar CompSciStudent requiere que implementes ambos superrasgos.
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
