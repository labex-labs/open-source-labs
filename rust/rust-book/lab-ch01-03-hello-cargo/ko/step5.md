# 규칙으로서의 Cargo

단순한 프로젝트의 경우, Cargo 는 `rustc`를 사용하는 것보다 많은 가치를 제공하지 않지만, 프로그램이 더 복잡해짐에 따라 그 가치를 증명할 것입니다. 프로그램이 여러 파일로 확장되거나 의존성이 필요한 경우, Cargo 가 빌드를 조정하도록 하는 것이 훨씬 쉽습니다.

`hello_cargo` 프로젝트는 단순하지만, 이제 나머지 Rust 경력에서 사용할 실제 도구의 많은 부분을 사용합니다. 실제로, 기존 프로젝트에서 작업하려면 다음 명령을 사용하여 Git 으로 코드를 체크아웃하고, 해당 프로젝트의 디렉토리로 이동한 다음 빌드할 수 있습니다.

```bash
git clone example.org/someproject
cd someproject
cargo build
```

Cargo 에 대한 자세한 내용은 *https://doc.rust-lang.org/cargo*에서 문서를 확인하십시오.
