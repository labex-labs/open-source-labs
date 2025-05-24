# Git 브랜치를 날짜별로 정렬하기

여러 개의 브랜치를 가진 Git 레포지토리가 있고, 이를 날짜별로 정렬하고 싶을 때가 있습니다. 이렇게 하면 어떤 브랜치가 최근에 업데이트되었고, 그렇지 않은지 쉽게 확인할 수 있습니다. 또한, 날짜별로 브랜치를 정렬하면 주의가 필요하거나 병합 (merging) 해야 할 브랜치를 식별하는 데 도움이 될 수 있습니다.

이 랩에서는 `https://github.com/labex-labs/git-playground` 레포지토리를 사용해 보겠습니다.

1. 레포지토리를 로컬 머신 (local machine) 에 클론 (clone) 합니다:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. 레포지토리 디렉토리로 이동하여 GitHub ID 를 구성합니다:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `one`이라는 브랜치를 생성하고, 코드를 수정하고 커밋 (commit) 합니다:

```shell
git checkout -b one
touch hello.txt
git add .
git commit -m "hello.txt"
```

4. `master` 브랜치로 전환하고 `two`라는 브랜치를 생성합니다:

```shell
git checkout master
git checkout -b two
```

5. 이제 브랜치를 날짜별로 정렬하려면 다음 명령을 사용합니다:

```shell
git branch --sort=-committerdate
```

이 명령은 모든 로컬 브랜치의 목록을 표시하고 마지막 커밋 날짜를 기준으로 정렬합니다. 화살표 키를 사용하여 목록을 탐색하고, <kbd>Q</kbd>를 눌러 종료할 수 있습니다.

다음은 최종 결과입니다:

![sorted git branches list](../assets/challenge-sort-branches-by-date.png)
