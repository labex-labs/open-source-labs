# 기존 크레이트의 새 버전 게시하기

크레이트를 변경하고 새 버전을 출시할 준비가 되면 `Cargo.toml` 파일에 지정된 `version` 값을 변경하고 다시 게시합니다. 변경 사항의 종류에 따라 적절한 다음 버전 번호를 결정하기 위해 *http://semver.org*의 Semantic Versioning 규칙을 사용합니다. 그런 다음 `cargo publish`를 실행하여 새 버전을 업로드합니다.
