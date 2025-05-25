# Path

`Path` 구조체는 기본 파일 시스템에서 파일 경로를 나타냅니다. `Path`에는 UNIX 계열 시스템용 `posix::Path`와 Windows 용 `windows::Path` 두 가지 종류가 있습니다. 프리루드 (prelude) 는 적절한 플랫폼별 `Path` 변형을 내보냅니다.

`Path`는 `OsStr`에서 생성될 수 있으며, 경로가 가리키는 파일/디렉터리의 정보를 얻기 위한 여러 메서드를 제공합니다.

`Path`는 불변입니다. `Path`의 소유 버전은 `PathBuf`입니다. `Path`와 `PathBuf`의 관계는 `str`과 `String`의 관계와 유사합니다. `PathBuf`는 자리에서 변경될 수 있으며, `Path`로 참조 해제될 수 있습니다.

`Path`는 내부적으로 UTF-8 문자열로 표현되지 않고 `OsString`으로 저장됩니다. 따라서 `Path`를 `&str`로 변환하는 것은 무료가 아니며 실패할 수 있습니다 (옵션이 반환됩니다). 그러나 `Path`는 `into_os_string`과 `as_os_str`를 사용하여 `OsString` 또는 `&OsStr`로 자유롭게 변환될 수 있습니다.

```rust
use std::path::Path;

fn main() {
    // &'static str 에서 Path 생성
    let path = Path::new(".");

    // display 메서드는 표시 가능한 구조체를 반환합니다.
    let _display = path.display();

    // join 은 OS 특정 구분자를 사용하여 경로와 바이트 컨테이너를 병합하고 PathBuf 를 반환합니다.
    let mut new_path = path.join("a").join("b");

    // push 는 PathBuf 를 &Path 로 확장합니다.
    new_path.push("c");
    new_path.push("myfile.tar.gz");

    // set_file_name 은 PathBuf 의 파일 이름을 업데이트합니다.
    new_path.set_file_name("package.tgz");

    // PathBuf 를 문자열 슬라이스로 변환
    match new_path.to_str() {
        None => panic!("new path 는 유효한 UTF-8 시퀀스가 아닙니다."),
        Some(s) => println!("new path 는 {}", s),
    }
}
```

다른 `Path` 메서드 (`posix::Path` 또는 `windows::Path`) 와 `Metadata` 구조체도 확인하세요.
