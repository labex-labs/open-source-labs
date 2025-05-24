# Git 텍스트 편집기 구성

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용합니다. Git 에서 사용하는 텍스트 편집기를 선호하는 편집기로 구성하려고 합니다.

1. `git-playground` 저장소를 복제합니다:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. 복제된 저장소로 이동하여 신원을 구성합니다:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Git 이 선호하는 텍스트 편집기를 사용하도록 구성합니다 (이 예에서는 vim 을 사용합니다):

```shell
git config --global core.editor "vim"
```

4. 파일에 변경 사항을 적용하고 커밋을 위해 스테이징합니다:

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. 변경 사항을 커밋합니다:

```shell
git commit
```

6. 선호하는 텍스트 편집기 (이 예에서는 vim) 가 커밋 메시지와 함께 열립니다. 커밋 메시지 "Update hello.txt"를 작성하고 파일을 저장합니다.
7. 텍스트 편집기를 닫습니다. 작성한 메시지로 커밋이 생성됩니다.

완료된 결과는 다음과 같습니다:

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
