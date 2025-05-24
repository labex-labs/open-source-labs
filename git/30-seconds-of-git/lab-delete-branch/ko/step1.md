# 브랜치 삭제

Git 저장소에서 로컬 브랜치를 생성했는데 더 이상 필요하지 않습니다. 저장소를 깨끗하고 정리된 상태로 유지하기 위해 해당 브랜치를 삭제하려고 합니다.

1. 복제된 저장소로 이동합니다:

```shell
cd git-playground
```

2. 현재 브랜치를 확인합니다:

```shell
git branch
```

3. `feature-1` 브랜치를 삭제합니다:

```shell
git branch -d feature-1
```

4. 브랜치가 삭제되었는지 확인합니다:

```shell
git branch
```

다음은 `git branch` 명령 실행 결과입니다:

```
* master
```
