# 마지막 커밋에서 파일 제거하기

의도하지 않게 마지막 커밋에 파일을 추가했습니다. 메시지를 변경하지 않고 마지막 커밋에서 해당 파일을 제거하려고 합니다.

이 실습을 위해 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. `git-playground`라는 이름의 Git 저장소가 있고, 실수로 마지막 커밋에 추가한 `file2.txt`라는 파일이 있다고 가정해 보겠습니다. 마지막 커밋에서 파일을 제거하는 단계는 다음과 같습니다.

1. 저장소를 복제하고, 디렉토리로 이동하여 신원을 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `git rm --cached <file>`을 사용하여 지정된 `<file>`을 인덱스에서 제거합니다.

```shell
git rm --cached file2.txt
```

3. `git commit --amend`를 사용하여 메시지를 변경하지 않고 마지막 커밋의 내용을 업데이트합니다.

```shell
git commit --amend --allow-empty
```

파일을 삭제한 후 커밋이 빈 커밋인 경우 `--allow-empty`를 사용하고, 그렇지 않은 경우 생략할 수 있습니다.

이러한 명령을 실행하면 `file2.txt` 파일이 메시지를 변경하지 않고 마지막 커밋에서 제거됩니다.

Git 버전 관리에서 `file2.txt`를 제거하면 다음과 같은 결과가 나타납니다.

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
