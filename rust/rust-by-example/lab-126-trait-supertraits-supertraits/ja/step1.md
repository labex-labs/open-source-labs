# スーパートレイト

Rust には「継承」はありませんが、あるトレイトを別のトレイトのスーパーセットとして定義することができます。たとえば：

```rust
trait Person {
    fn name(&self) -> String;
}

// Person は Student のスーパートレイトです。
// Student を実装するには、Person も実装する必要があります。
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent（コンピュータサイエンスの学生）は、Programmer
// と Student の両方のサブトレイトです。CompSciStudent を実装するには、両方のスーパートレイトを実装する必要があります。
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
