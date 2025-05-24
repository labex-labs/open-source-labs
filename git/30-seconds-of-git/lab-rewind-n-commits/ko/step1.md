# 커밋 되돌리기

개발자로서 프로젝트를 진행하면서 여러 개의 커밋을 만들었습니다. 하지만, 마지막 몇 개의 커밋에 오류가 포함되어 있고 이전 버전의 코드로 되돌아가야 한다는 것을 깨달았습니다. Git 을 사용하여 커밋을 되돌리고 이전 버전의 코드로 돌아가야 합니다.

이 실습을 완료하려면 GitHub 계정의 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. 다음 단계를 따르세요:

1. 로컬 머신에 저장소를 클론합니다:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. `rewind-commits`라는 새 브랜치를 생성합니다:

```shell
git checkout -b rewind-commits
```

3. 저장소의 커밋 기록을 보고 마지막 커밋에 오류가 포함되어 있고 이전 버전의 코드로 돌아가야 함을 확인합니다:

```shell
git log
```

4. Git 을 사용하여 커밋을 1 개 되돌립니다:

```shell
git reset HEAD~1 --hard
```

5. 커밋을 성공적으로 되돌렸는지 확인합니다:

```shell
git log
```

6. 변경 사항을 `rewind-commits` 브랜치로 푸시합니다:

```shell
git push --force origin rewind-commits
```

최종 결과는 다음과 같습니다:

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
