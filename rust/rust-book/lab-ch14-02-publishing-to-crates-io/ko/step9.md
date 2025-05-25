# Crates.io 에 게시하기

이제 계정을 만들고, API 토큰을 저장하고, 크레이트의 이름을 선택하고, 필요한 메타데이터를 지정했으므로 게시할 준비가 되었습니다! 크레이트를 게시하면 특정 버전이 다른 사용자가 사용할 수 있도록 *https://crates.io*에 업로드됩니다.

게시는 *영구적*이므로 주의하십시오. 버전은 절대 덮어쓸 수 없으며 코드를 삭제할 수 없습니다. Crates.io 의 주요 목표 중 하나는 *https://crates.io*의 크레이트에 의존하는 모든 프로젝트의 빌드가 계속 작동하도록 코드의 영구 보관소 역할을 하는 것입니다. 버전 삭제를 허용하면 해당 목표를 달성할 수 없습니다. 그러나 게시할 수 있는 크레이트 버전 수에는 제한이 없습니다.

`cargo publish` 명령을 다시 실행합니다. 이제 성공해야 합니다.

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

축하합니다! 이제 Rust 커뮤니티와 코드를 공유했으며, 누구나 크레이트를 프로젝트의 종속성으로 쉽게 추가할 수 있습니다.
