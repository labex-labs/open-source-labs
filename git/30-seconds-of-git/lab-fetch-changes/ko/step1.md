# 원격 저장소에서 최신 변경 사항 가져오기

팀 개발자와 함께 프로젝트를 진행하고 있고, 해당 프로젝트가 원격 저장소에 저장되어 있다고 가정해 보겠습니다. 로컬 저장소에 적용하지 않고 원격 저장소에서 최신 변경 사항을 가져오고 싶을 수 있습니다. 이럴 때 `git fetch` 명령어가 유용합니다.

`git fetch` 명령어는 원격 저장소에서 최신 변경 사항을 로컬 저장소로 다운로드하지만, 작업 디렉토리에는 적용하지 않습니다. 즉, 로컬 저장소에 병합하기 전에 변경 사항을 검토할 수 있습니다.

원격 저장소에서 최신 변경 사항을 가져오는 방법을 보여주기 위해, GitHub 계정의 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. 다음 단계를 따르세요.

1. 저장소를 복제하고, 디렉토리로 이동합니다.

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. GitHub 웹사이트에서 계정의 `git-playground` 저장소를 찾고, `fetch-branch`라는 브랜치를 생성하고 전환한 다음, `hello.txt` 파일을 생성하고 "hello, world"를 추가하고 "Create hello.txt" 메시지로 커밋합니다.
3. 원격 저장소의 브랜치를 확인합니다.

```shell
git branch -r
```

4. 원격 저장소에서 최신 변경 사항을 가져옵니다.

```shell
git fetch
```

5. 다시 원격 저장소의 브랜치를 확인하고 최신 변경 사항이 가져와졌는지 확인합니다.

```shell
git branch -r
git log origin/fetch-branch
```

이렇게 하면 `origin/fetch-branch` 브랜치의 최신 커밋이 표시됩니다. 다음은 `git log origin/fetch-branch`를 실행한 결과입니다.

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
