# 손실된 파일 찾기

`git-playground` 저장소에서 프로젝트를 진행해 왔습니다. 하지만 일부 파일이 누락되었고, 언제 삭제되었는지 또는 복구하는 방법을 알 수 없습니다. Git 을 사용하여 저장소에서 손실된 파일과 커밋을 찾는 것이 목표입니다.

1. `git-playground` 저장소를 복제합니다:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 디렉토리로 이동하여 신원을 구성합니다:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `one-branch`라는 브랜치를 생성하고 전환한 다음, `file2.txt`를 삭제하고 "Remove file2" 메시지로 커밋합니다:

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Remove file2"
```

4. 다시 `master` 브랜치로 전환하고 `one-branch` 브랜치를 삭제합니다:

```shell
git checkout master
git branch -D one-branch
```

5. `git fsck --lost-found` 명령을 실행하여 손실된 파일과 커밋을 찾습니다:

```shell
git fsck --lost-found
```

6. `.git/lost-found` 디렉토리를 확인하여 손실된 파일이 복구되었는지 확인합니다:

```shell
ls .git/lost-found
```

7. 손실된 파일이 발견된 경우, 누락된 파일인지 확인하기 위해 검토합니다.

`ls .git/lost-found` 명령 실행 결과는 다음과 같습니다:

```shell
commit
```
