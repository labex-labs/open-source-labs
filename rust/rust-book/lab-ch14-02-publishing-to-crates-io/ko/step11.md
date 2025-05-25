# cargo yank 를 사용하여 Crates.io 에서 버전 사용 중단

크레이트의 이전 버전을 제거할 수는 없지만, 향후 프로젝트에서 해당 버전을 새 종속성으로 추가하는 것을 방지할 수 있습니다. 이는 크레이트 버전이 어떤 이유로든 손상된 경우에 유용합니다. 이러한 상황에서 Cargo 는 크레이트 버전의 yank 를 지원합니다.

버전을 *yank*하면 새 프로젝트가 해당 버전에 종속되는 것을 방지하는 동시에, 이에 종속된 모든 기존 프로젝트는 계속 사용할 수 있습니다. 본질적으로 yank 는 *Cargo.lock*이 있는 모든 프로젝트가 중단되지 않으며, 생성될 모든 향후 _Cargo.lock_ 파일이 yank 된 버전을 사용하지 않음을 의미합니다.

크레이트의 버전을 yank 하려면, 이전에 게시한 크레이트의 디렉토리에서 `cargo yank`를 실행하고 yank 하려는 버전을 지정합니다. 예를 들어, `guessing_game` 버전 1.0.1 이라는 크레이트를 게시했고 이를 yank 하려는 경우, `guessing_game` 프로젝트 디렉토리에서 다음을 실행합니다.

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

명령에 `--undo`를 추가하면 yank 를 실행 취소하고 프로젝트가 다시 버전에 종속되도록 허용할 수도 있습니다.

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

Yank 는 코드를 _삭제하지_ 않습니다. 예를 들어, 실수로 업로드된 비밀을 삭제할 수 없습니다. 그런 경우, 즉시 해당 비밀을 재설정해야 합니다.
