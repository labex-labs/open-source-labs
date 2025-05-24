# 커밋되지 않은 변경 사항 폐기

로컬 Git 저장소에 몇 가지 변경 사항을 적용했지만 아직 커밋하지 않았습니다. 그러나 이러한 변경 사항을 더 이상 유지하고 싶지 않아 폐기하기로 결정했습니다. 문제는 현재 브랜치에 대한 모든 커밋되지 않은 변경 사항을 폐기하는 방법을 찾는 것입니다.

이 챌린지를 완료하려면 `https://github.com/labex-labs/git-playground` 디렉토리라는 Git 저장소를 사용합니다. 아래 단계를 따르세요.

1. `git clone https://github.com/labex-labs/git-playground.git` 명령을 사용하여 저장소를 로컬 머신에 복제합니다.
2. `cd git-playground` 명령을 사용하여 복제된 저장소로 이동합니다.
3. `echo "hello,world" > hello.txt` 및 `git add .` 명령을 사용하여 저장소의 파일에 몇 가지 변경 사항을 적용하지만 커밋하지는 않습니다.
4. `git status` 명령을 사용하여 변경 사항을 확인합니다.
5. `git reset --hard HEAD` 명령을 사용하여 모든 커밋되지 않은 변경 사항을 폐기합니다.
6. `git status` 명령을 다시 사용하여 모든 변경 사항이 폐기되었는지 확인합니다.

다음은 `git status`를 실행한 결과입니다.

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
