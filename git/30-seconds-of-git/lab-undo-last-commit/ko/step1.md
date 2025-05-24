# 마지막 커밋 취소

Git 저장소에 변경 사항을 커밋했지만 실수를 했다는 것을 깨달았습니다. 변경 사항을 잃지 않고 마지막 커밋을 취소하고 싶습니다. 어떻게 할 수 있을까요?

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따르세요:

1. 저장소를 복제하고, 디렉토리로 이동하여 신원을 구성합니다:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. 커밋 기록을 확인합니다:

```shell
git log
```

3. 마지막 커밋을 취소하고, 커밋의 변경 사항을 반전시킨 새로운 커밋을 생성합니다:

```shell
git revert HEAD
```

4. 다시 커밋 기록을 확인합니다:

```shell
git log
```

다음은 `git log --oneline` 명령을 실행한 결과입니다:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
