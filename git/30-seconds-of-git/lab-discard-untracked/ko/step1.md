# 추적되지 않은 변경 사항 폐기

Git 을 사용하여 프로젝트를 진행 중이며 작업 디렉토리에 몇 가지 변경 사항을 적용했습니다. 하지만 이러한 변경 사항이 필요 없다는 것을 깨닫고 이를 폐기하고 싶습니다. 현재 브랜치에 대한 추적되지 않은 모든 변경 사항을 폐기하려고 합니다.

이 랩을 완료하려면 `https://github.com/labex-labs/git-playground`라는 Git 저장소를 사용합니다. 다음 단계를 따르세요.

1. 저장소 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. 작업 디렉토리의 상태를 확인합니다.

```shell
git status
```

다음과 같은 출력을 볼 수 있습니다.

```shell
[object Object]
```

3. 현재 브랜치에 대한 추적되지 않은 모든 변경 사항을 폐기합니다.

```shell
git clean -f -d
```

4. 작업 디렉토리의 상태를 다시 확인합니다.

```shell
git status
```

다음과 같은 출력을 볼 수 있습니다.

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

`git clean -f -d` 명령은 현재 브랜치에 대한 추적되지 않은 모든 변경 사항을 폐기했습니다.
