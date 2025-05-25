# Crates.io 계정 설정

크레이트를 게시하기 전에 *https://crates.io*에서 계정을 만들고 API 토큰을 받아야 합니다. 이렇게 하려면 *https://crates.io*의 홈페이지를 방문하여 GitHub 계정을 통해 로그인하십시오. (GitHub 계정은 현재 필수 사항이지만, 사이트에서 향후 다른 계정 생성 방법을 지원할 수 있습니다.) 로그인한 후 *https://crates.io/me*에서 계정 설정을 방문하여 API 키를 검색하십시오. 그런 다음 API 키를 사용하여 `cargo login` 명령을 실행합니다.

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

이 명령은 Cargo 에 API 토큰을 알리고 로컬로 *\~/.cargo/credentials*에 저장합니다. 이 토큰은 *비밀*이므로 다른 사람과 공유하지 마십시오. 어떤 이유로든 다른 사람과 공유하는 경우, 해당 토큰을 해지하고 *https://crates.io*에서 새 토큰을 생성해야 합니다.
