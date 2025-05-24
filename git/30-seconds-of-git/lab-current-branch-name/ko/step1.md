# 현재 브랜치 이름 가져오기

Git 레포지토리에서 현재 브랜치의 이름을 출력하는 명령어를 작성합니다.

`https://github.com/labex-labs/git-playground` 레포지토리에 저장된 프로젝트를 작업하고 있다고 가정해 봅시다. `README.md` 파일을 변경하고 현재 브랜치에 커밋 (commit) 하려 합니다. 하지만, 그 전에 올바른 브랜치에 있는지 확인하고 싶습니다.

현재 브랜치를 확인하려면 다음 명령어를 사용할 수 있습니다.

```shell
git rev-parse --abbrev-ref HEAD
```

이 명령어는 현재 브랜치의 이름을 콘솔에 출력합니다. 예를 들어, 현재 `master` 브랜치에 있다면, 출력 결과는 다음과 같습니다.

```shell
master
```

`feature-branch`와 같은 다른 브랜치로 전환하면, 출력 결과가 그에 따라 변경됩니다.

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

이 명령어는 다음을 출력합니다.

```shell
feature-branch
```
