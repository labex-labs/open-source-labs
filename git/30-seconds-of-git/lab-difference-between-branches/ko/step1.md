# 브랜치 간의 차이점

팀과 함께 프로젝트를 진행하면서 새로운 기능을 작업하기 위해 `feature-1`이라는 브랜치를 생성했습니다. 동료도 다른 기능을 작업하기 위해 `feature-2`라는 브랜치를 생성했습니다. 두 브랜치 간의 변경 사항을 비교하여 추가, 수정 또는 삭제된 내용을 확인하고 싶습니다. 두 브랜치 간의 차이점을 어떻게 확인할 수 있을까요?

GitHub 계정에서 `https://github.com/labex-labs/git-playground.git`에서 `git-playground`라는 리포지토리를 복제했다고 가정해 보겠습니다. 다음 단계를 따르세요.

1. `cd git-playground` 명령을 사용하여 리포지토리의 디렉토리로 이동합니다.
2. `git config --global user.name "Your Name"` 및 `git config --global user.email "your@email.com"` 명령을 사용하여 이 환경에서 GitHub 계정을 구성합니다.
3. `git checkout -b feature-1` 명령을 사용하여 `feature-1` 브랜치를 생성하고 전환한 다음, `README.md` 파일에 "hello"를 추가하고, 스테이징 영역에 추가하고 커밋합니다. 커밋 메시지는 "Add new content to README.md"입니다. `echo "hello" >> README.md `, `git add .` 및 `git commit -am "Add new content to README.md"` 명령을 사용합니다.
4. 다시 `master` 브랜치로 전환합니다.
5. `git checkout -b feature-2` 명령을 사용하여 `feature-2` 브랜치를 생성하고 전환한 다음, `index.html` 파일에 "world"를 추가하고, 스테이징 영역에 추가하고 커밋합니다. 커밋 메시지는 "Update index.html file"입니다. `echo "world" > index.htm`, `git add .` 및 `git commit -am "Update index.html file"` 명령을 사용합니다.
6. `git diff feature-1..feature-2` 명령을 사용하여 두 브랜치 간의 차이점을 확인합니다.

출력 결과는 `feature-1` 및 `feature-2` 브랜치 간의 차이점을 표시해야 합니다. 최종 결과가 다음과 같이 표시됩니다.

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
