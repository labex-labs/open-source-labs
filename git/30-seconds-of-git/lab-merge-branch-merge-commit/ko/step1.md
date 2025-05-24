# 브랜치 병합 및 병합 커밋 생성

개발자로서 현재 브랜치에 브랜치를 병합하여 병합 커밋을 생성해야 할 수 있습니다. Git 에 익숙하지 않다면 다소 까다로울 수 있습니다. 문제는 `https://github.com/labex-labs/git-playground` 디렉토리라는 이름의 Git 저장소를 사용하여 현재 브랜치에 브랜치를 병합하여 병합 커밋을 생성하는 것입니다.

이 챌린지를 위해 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다.

1. `https://github.com/labex-labs/git-playground.git`에서 저장소를 복제합니다.

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 디렉토리로 이동하여 ID 를 구성합니다.

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `feature-branch`라는 브랜치를 생성하고 전환합니다.

```shell
git checkout -b feature-branch
```

4. "This is a new line."을 `README.md` 파일에 추가하고, 스테이징 영역에 추가하고 커밋합니다. 커밋 메시지는 "Add new line to README.md"입니다.

```shell
echo "This is a new line." >> README.md
git add .
git commit -am "Add new line to README.md"
```

5. `master` 브랜치로 전환합니다.

```shell
git checkout master
```

6. `feature-branch`를 `master` 브랜치에 병합합니다. 그러면 "Merge feature-branch" 메시지가 있는 병합 커밋이 생성됩니다.

```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

다음은 `git log`를 실행한 결과입니다.

```shell
ADD new line to README.md
```
