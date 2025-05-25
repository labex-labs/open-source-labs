# 새 크레이트에 메타데이터 추가하기

게시하려는 크레이트가 있다고 가정해 보겠습니다. 게시하기 전에 크레이트의 `Cargo.toml` 파일의 `[package]` 섹션에 몇 가지 메타데이터를 추가해야 합니다.

크레이트에는 고유한 이름이 필요합니다. 로컬에서 크레이트를 작업하는 동안 원하는 대로 크레이트의 이름을 지정할 수 있습니다. 그러나 *https://crates.io*의 크레이트 이름은 선착순으로 할당됩니다. 크레이트 이름이 사용되면 다른 사람은 해당 이름으로 크레이트를 게시할 수 없습니다. 크레이트를 게시하기 전에 사용하려는 이름을 검색하십시오. 이름이 사용된 경우 다른 이름을 찾아 `Cargo.toml` 파일의 `[package]` 섹션에서 `name` 필드를 편집하여 게시할 새 이름을 사용해야 합니다.

파일 이름: `Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

고유한 이름을 선택했더라도 이 시점에서 `cargo publish`를 실행하여 크레이트를 게시하면 경고와 오류가 발생합니다.

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

이것은 몇 가지 중요한 정보가 누락되었기 때문에 오류가 발생합니다. 설명과 라이선스는 필수이므로 사람들이 크레이트가 무엇을 하는지, 어떤 조건으로 사용할 수 있는지 알 수 있습니다. `Cargo.toml`에서 크레이트가 검색 결과에 표시되므로 한두 문장으로 된 설명을 추가합니다. `license` 필드의 경우 *라이선스 식별자 값*을 제공해야 합니다. *http://spdx.org/licenses*의 Linux Foundation 의 Software Package Data Exchange (SPDX) 는 이 값에 사용할 수 있는 식별자를 나열합니다. 예를 들어, MIT 라이선스를 사용하여 크레이트에 라이선스를 부여했음을 지정하려면 `MIT` 식별자를 추가합니다.

파일 이름: `Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

SPDX 에 나타나지 않는 라이선스를 사용하려면 해당 라이선스의 텍스트를 파일에 넣고, 해당 파일을 프로젝트에 포함한 다음, `license` 키를 사용하는 대신 `license-file`을 사용하여 해당 파일의 이름을 지정해야 합니다.

프로젝트에 적합한 라이선스에 대한 지침은 이 책의 범위를 벗어납니다. Rust 커뮤니티의 많은 사람들은 `MIT OR Apache-2.0`의 이중 라이선스를 사용하여 Rust 와 동일한 방식으로 프로젝트에 라이선스를 부여합니다. 이 관행은 `OR`로 구분된 여러 라이선스 식별자를 지정하여 프로젝트에 여러 라이선스를 가질 수도 있음을 보여줍니다.

고유한 이름, 버전, 설명 및 라이선스가 추가된 게시 준비가 된 프로젝트의 `Cargo.toml` 파일은 다음과 같습니다.

파일 이름: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

*https://doc.rust-lang.org/cargo*의 Cargo 문서는 다른 사람이 크레이트를 더 쉽게 발견하고 사용할 수 있도록 지정할 수 있는 다른 메타데이터를 설명합니다.
