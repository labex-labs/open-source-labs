# 문제 해결

Rust 가 올바르게 설치되었는지 확인하려면 **새 셸 (shell)**을 열고 다음 줄을 입력하십시오.

```bash
# Open a new terminal first!
rustc --version
```

다음 형식으로 릴리스된 최신 안정 버전의 버전 번호, 커밋 해시 (commit hash), 커밋 날짜를 볼 수 있습니다.

```bash
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

이 정보를 확인하면 Rust 가 성공적으로 설치된 것입니다! 이 정보가 표시되지 않으면 다음과 같이 Rust 가 `%PATH%` 시스템 변수에 있는지 확인하십시오.

Linux 에서 사용:

```bash
echo $PATH
```

모두 올바른데도 Rust 가 여전히 작동하지 않으면 도움을 받을 수 있는 여러 곳이 있습니다. *https://www.rust-lang.org/community*의 커뮤니티 페이지에서 다른 Rust 사용자 (우리 스스로를 부르는 어리석은 별명) 와 연락하는 방법을 알아보십시오.
