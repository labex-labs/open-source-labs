# 최신 Stash 적용하기

Git 저장소에서 프로젝트 작업을 진행 중이며 아직 커밋할 준비가 되지 않은 변경 사항이 있습니다. 하지만 다른 기능을 작업하기 위해 다른 브랜치 또는 커밋으로 전환해야 합니다. 변경 사항을 잃고 싶지 않으므로 stash 를 하기로 결정합니다. 나중에 변경 사항 작업을 계속할 준비가 되면 최신 stash 를 작업 디렉토리에 적용해야 합니다.

최신 stash 를 Git 저장소에 적용하려면 다음 단계를 따르세요.

1. `https://github.com/labex-labs/git-playground`라는 Git 저장소를 로컬 머신에 복제합니다.
2. `git-playground` 디렉토리로 이동합니다.
3. `README.md` 파일을 변경합니다. 예를 들어, `README.md` 파일에 "This is a new line"을 작성합니다.
4. `git stash` 명령을 실행하여 변경 사항을 stash 합니다.
5. `git stash list` 명령을 실행하여 stash 목록을 확인합니다. 목록에 하나의 stash 가 표시되어야 합니다.
6. `git stash apply` 명령을 실행하여 최신 stash 를 작업 디렉토리에 적용합니다.
7. `README.md` 파일을 확인하여 변경 사항이 적용되었는지 확인합니다.

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

다음은 `cat README.md`를 실행한 결과입니다.

```shell
# git-playground
Git Playground
This is a new line
```
