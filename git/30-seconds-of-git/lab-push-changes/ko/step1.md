# 로컬 변경 사항을 원격 저장소로 푸시하기

개발자는 다른 팀원과 작업을 공유하거나 코드를 프로덕션 환경에 배포하기 위해 로컬 변경 사항을 원격 저장소로 푸시해야 할 수 있습니다. `git push` 명령은 로컬 브랜치에서 최신 변경 사항을 원격 저장소로 푸시하는 데 사용됩니다. 그러나 변경 사항을 푸시하기 전에 로컬 브랜치가 원격 브랜치와 최신 상태인지 확인해야 합니다. 로컬 브랜치와 원격 브랜치 사이에 충돌이 있는 경우 변경 사항을 푸시하기 전에 이를 해결해야 합니다.

이 랩을 완료하려면 GitHub 계정의 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. `master` 브랜치에 몇 가지 변경 사항을 적용했으며 이를 원격 저장소로 푸시하려고 합니다. 다음 단계를 따라야 합니다.

1. 다음 명령을 실행하여 저장소를 로컬 머신에 복제하고 디렉토리로 이동합니다.

```shell
git clone https://github.com/your-username/git-playground
cd git-playground
```

2. 다음 명령을 실행하여 로컬 브랜치가 원격 브랜치와 최신 상태인지 확인합니다.

```shell
git pull origin master
```

3. 원격 브랜치에서 최신 변경 사항을 가져온 후 로컬 브랜치에 변경 사항을 적용할 수 있습니다.

```shell
echo "hello,world" >> file1.txt
```

4. 변경 사항을 적용한 후 `git add` 명령을 사용하여 스테이징합니다.

```shell
git add .
```

5. `git commit` 명령을 사용하여 변경 사항을 커밋합니다.

```shell
git commit -m "Added new feature"
```

6. 마지막으로 `git push` 명령을 사용하여 변경 사항을 원격 저장소로 푸시합니다.

```shell
git push origin master
```

다음은 `git log`를 실행한 결과입니다.

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
