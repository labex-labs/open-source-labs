# Supertraits (Super-características)

Rust não possui "herança" (inheritance), mas você pode definir uma trait (característica) como sendo um superconjunto de outra trait. Por exemplo:

```rust
trait Person {
    fn name(&self) -> String;
}

// Person é uma supertrait de Student.
// Implementar Student requer que você também implemente Person.
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent (estudante de ciência da computação) é uma subtrait de Programmer
// e Student. Implementar CompSciStudent requer que você implemente ambas as supertraits.
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
