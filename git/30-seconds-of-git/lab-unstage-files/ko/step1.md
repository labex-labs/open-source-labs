# 스테이징 영역에서 파일 제거하기

`git-playground` 리포지토리에서 프로젝트 작업을 하고 있습니다. 파일에 몇 가지 변경 사항을 적용하고 `git add` 명령을 사용하여 스테이징 영역에 추가했습니다. 하지만 실수로 커밋하고 싶지 않은 파일을 추가했다는 것을 깨달았습니다. 이 파일을 스테이징 영역에서 제거해야 합니다.

1. 현재 작업 디렉토리 상태 보기:

```shell
git status
```

2. `git restore --staged` 명령을 사용하여 `newfile.txt` 파일을 스테이징 영역에서 제거합니다:

```shell
git restore --staged newfile.txt
```

3. `git status` 명령을 사용하여 파일이 스테이징 영역에서 제거되었는지 확인합니다:

```shell
git status
```

최종 결과는 다음과 같습니다:

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
