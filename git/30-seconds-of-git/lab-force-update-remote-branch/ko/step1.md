# 기록 재작성 후 원격 브랜치 업데이트

로컬에서 기록을 재작성하면 다른 SHA-1 해시를 가진 새로운 커밋이 생성됩니다. 이는 로컬 브랜치의 커밋 기록이 원격 브랜치의 커밋 기록과 다르다는 것을 의미합니다. 변경 사항을 원격 브랜치로 푸시하려고 하면 Git 은 커밋 기록이 분기된 것으로 간주하여 푸시를 거부합니다. 이 문제를 해결하려면 원격 브랜치를 강제로 업데이트해야 합니다.

이 랩을 완료하려면 GitHub 계정에서 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다.

1. `git-playground` 저장소를 로컬 머신으로 클론합니다.

```shell
git clone https://github.com/your-username/git-playground.git
```

2. "Added file2.txt" 메시지를 가진 커밋을 "Update file2.txt" 메시지를 가진 커밋으로 업데이트합니다.

```shell
git commit --amend
```

3. 로컬 브랜치의 변경 사항을 원격 저장소로 푸시합니다.

```shell
git push
```

4. 푸시에 성공하지 못하면 강제로 푸시합니다.

```shell
git push -f origin master
```

`-f` 플래그는 커밋 기록이 분기되었더라도 Git 이 변경 사항으로 원격 브랜치를 강제로 업데이트하도록 합니다.

최종 결과는 다음과 같습니다.

```shell
[object Object]
```
