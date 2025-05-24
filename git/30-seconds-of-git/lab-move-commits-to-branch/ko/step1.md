# 새로운 브랜치로 커밋 이동하기

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. `master` 브랜치에서 프로젝트 작업을 진행해 왔습니다. 몇몇 변경 사항이 별도의 브랜치에서 이루어졌어야 한다는 것을 깨달았습니다. 이러한 변경 사항을 `feature`라는 새로운 브랜치로 이동하려고 합니다.

1. 저장소를 복제하고, 디렉토리로 이동한 후, 신원을 구성합니다:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `master` 브랜치를 체크아웃합니다:

```shell
git checkout master
```

3. `hello.txt`라는 파일을 생성하고, "hello, world"를 추가한 다음, 스테이징 영역에 추가하고 "Added hello.txt" 메시지로 커밋합니다:

```shell
echo "hello,world" >> hello.txt
git add .
git commit -m "Added hello.txt"
```

4. `feature`라는 새로운 브랜치를 생성하되, 해당 브랜치로 전환하지는 않습니다. `master` 브랜치에서 새로운 브랜치를 생성하면, 새로운 브랜치의 상태는 `master` 브랜치와 동일합니다. 즉, 새로운 브랜치의 파일은 `master` 브랜치의 파일과 동일하며, 동일한 내용과 버전 기록을 갖습니다:

```shell
git branch feature
```

5. `master`에서 마지막 커밋을 되돌립니다:

```shell
git reset HEAD~1 --hard
```

6. `master` 브랜치의 커밋 기록과 `feature` 브랜치의 커밋 기록을 확인하여 결과를 검증합니다:

```shell
git log
git checkout feature
git log
```

다음은 `git log`를 실행한 결과입니다:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
