# 브랜치로 전환하기

`https://github.com/labex-labs/git-playground`라는 Git 저장소에서 프로젝트를 작업하고 있습니다. 팀은 새로운 기능을 작업하기 위해 `feature-1`이라는 새로운 브랜치를 생성했습니다. 해당 기능을 계속 작업하려면 `feature-1` 브랜치로 전환해야 합니다.

1. Git 저장소를 복제합니다:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 저장소 디렉토리로 이동합니다:

```shell
cd git-playground
```

3. 저장소의 모든 브랜치를 나열합니다:

```shell
git branch
```

출력:

```shell
feature-1
* master
```

4. `feature-1` 브랜치로 전환합니다:

```shell
git checkout feature-1
```

출력:

```shell
Switched to branch 'feature-1'
```

5. 현재 `feature-1` 브랜치에 있는지 확인합니다:

```shell
git branch
```

출력:

```shell
* feature-1
master
```
