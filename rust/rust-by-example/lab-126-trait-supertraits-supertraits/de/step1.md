# Supertraits

Rust hat keine "Vererbung", aber Sie können einen Trait als Supermenge eines anderen Traits definieren. Beispielsweise:

```rust
trait Person {
    fn name(&self) -> String;
}

// Person ist ein Supertrait von Student.
// Die Implementierung von Student erfordert auch die Implementierung von Person.
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent (Informatikstudent) ist ein Subtrait sowohl von Programmer
// als auch von Student. Die Implementierung von CompSciStudent erfordert die Implementierung beider Supertraits.
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
