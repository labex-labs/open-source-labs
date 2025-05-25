# 슈퍼트레이트 (Supertraits)

Rust 는 "상속 (inheritance)"을 가지고 있지 않지만, 트레이트를 다른 트레이트의 상위 집합으로 정의할 수 있습니다. 예를 들어:

```rust
trait Person {
    fn name(&self) -> String;
}

// Person 은 Student 의 슈퍼트레이트입니다.
// Student 를 구현하려면 Person 도 구현해야 합니다.
trait Student: Person {
    fn university(&self) -> String;
}

trait Programmer {
    fn fav_language(&self) -> String;
}

// CompSciStudent (컴퓨터 과학 학생) 는 Programmer 와 Student 의 하위 트레이트입니다. CompSciStudent 를 구현하려면 두 슈퍼트레이트 모두 구현해야 합니다.
trait CompSciStudent: Programmer + Student {
    fn git_username(&self) -> String;
}

fn comp_sci_student_greeting(student: &dyn CompSciStudent) -> String {
    format!(
        "제 이름은 {}이고, {}에 다닙니다. 제가 가장 좋아하는 언어는 {}입니다. 제 Git 사용자 이름은 {}입니다.",
        student.name(),
        student.university(),
        student.fav_language(),
        student.git_username()
    )
}

fn main() {}
```
