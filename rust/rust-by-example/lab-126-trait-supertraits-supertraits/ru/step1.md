# Надтрейты

В Rust нет "наследования", но вы можете определить трейт как надмножество другого трейта. Например:

```rust
trait Person {
    fn name(&self) -> String;
}

// Person - надтрейт для Student.
// При реализации Student вам также нужно реализовать Person.
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent (студент компьютерных наук) - подтрейт как для Programmer,
// так и для Student. При реализации CompSciStudent вам нужно реализовать оба надтрейта.
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
