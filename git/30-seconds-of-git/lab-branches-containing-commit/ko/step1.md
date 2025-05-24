# 커밋을 포함하는 브랜치 찾기

`https://github.com/labex-labs/git-playground`라는 이름의 Git 저장소가 주어졌습니다. 여러분의 과제는 커밋 메시지가 "Added file2.txt"인 해시를 포함하는 모든 브랜치를 찾는 것입니다.

1. 저장소 디렉토리로 이동합니다:

```shell
cd git-playground
```

2. `git branch --contains` 명령어를 사용하여 커밋 메시지가 "Added file2.txt"인 해시를 포함하는 모든 브랜치를 찾습니다:

```shell
git branch --contains d22f46b
```

출력 결과는 다음과 같아야 합니다:

```shell
* master
new-branch
new-branch-1
new-branch-2
```
