# 超级 trait

Rust 没有“继承”，但你可以将一个 trait 定义为另一个 trait 的超集。例如：

```rust
trait Person {
    fn name(&self) -> String;
}

// Person 是 Student 的超级 trait。
// 实现 Student 要求你同时实现 Person。
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent（计算机科学专业的学生）是 Programmer 和 Student 的子 trait。
// 实现 CompSciStudent 要求你实现这两个超级 trait。
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
