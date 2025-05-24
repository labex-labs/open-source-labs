# 병합된 브랜치 삭제

귀하의 과제는 `https://github.com/labex-labs/git-playground` 저장소의 `master` 브랜치에 병합된 모든 로컬 브랜치를 삭제하는 것입니다.

1. 저장소 디렉토리로 이동합니다:

```shell
cd git-playground
```

2. `master`에 병합된 모든 로컬 브랜치를 나열합니다:

```shell
git branch --merged
```

출력:

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. 병합된 모든 브랜치를 삭제합니다:

```shell
git branch --merged master | awk '!/^[ *]*$/ && !/master/ {print $1}' | xargs git branch -d
```

4. 모든 브랜치를 다시 나열합니다:

```shell
git branch
```

최종 결과는 다음과 같습니다:

```
* master
```
