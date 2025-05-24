# 특정 커밋으로 되돌리기

개발자로서 코드베이스 (codebase) 에 대한 변경 사항을 실행 취소해야 할 수 있습니다. 예를 들어, 실수를 하여 코드의 이전 버전으로 되돌아가야 할 수 있습니다. 이 챌린지에서는 Git 을 사용하여 리포지토리 (repository) 의 특정 커밋으로 되돌아갑니다.

이 랩 (lab) 을 완료하려면 `https://github.com/labex-labs/git-playground.git`에서 `git-playground` Git 리포지토리를 사용합니다. 다음 단계를 따라 챌린지를 완료하십시오.

1. 리포지토리를 로컬 머신 (local machine) 에 복제합니다.

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 리포지토리로 이동합니다.

```shell
cd git-playground
```

3. 리포지토리의 커밋 기록을 봅니다.

```shell
git log --oneline
```

4. 되돌리려는 커밋 메시지가 "Initial commit" 커밋 해시 (commit hash) 인지 확인합니다.
5. `git reset <commit>` 명령을 사용하여 지정된 커밋으로 되돌립니다. 예를 들어, 해시가 `3050fc0d3`인 커밋으로 되돌리려면 다음과 같이 합니다.

```shell
git reset 3050fc0d3
```

6. 리포지토리의 커밋 기록을 다시 봅니다.

```shell
git log --oneline
```

7. 변경 사항을 삭제하고 코드의 이전 버전으로 되돌리려면 `git reset --hard <commit>` 명령을 사용합니다. 예를 들어, 변경 사항을 삭제하고 해시가 `c0d30f305`인 커밋으로 되돌리려면 다음과 같이 합니다.

```shell
git reset --hard c0d30f305
```

다음은 `git log --oneline`을 실행한 결과입니다.

```shell
c0d30f305 (HEAD -> master) Initial commit
```
