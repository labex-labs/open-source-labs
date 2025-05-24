# 변경 사항의 차이점 보기

개발자로서, 스테이징 (staged) 또는 언스테이징 (unstaged) 된 변경 사항과 마지막 커밋 간의 차이점을 확인하고 싶을 수 있습니다. 이는 커밋하기 전에 변경 사항을 검토하거나 마지막 커밋 이후에 어떤 변경 사항을 적용했는지 확인하려는 경우에 유용합니다.

변경 사항의 차이점을 보는 방법을 보여주기 위해 `git-playground` 저장소를 사용하겠습니다. `README.md` 파일에 몇 가지 변경 사항을 적용했고, 변경 사항과 마지막 커밋 간의 차이점을 확인하려는 경우를 가정해 보겠습니다.

1. 터미널을 열고 `git-playground` 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. `git diff` 명령을 사용하여 언스테이징된 변경 사항과 마지막 커밋 간의 차이점을 확인합니다.

```shell
git diff
```

3. 또는 `--staged` 옵션을 사용하여 스테이징된 변경 사항과 마지막 커밋 간의 차이점을 확인할 수 있습니다.

```shell
git diff --staged
```

다음은 2 단계를 완료한 결과입니다.

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

다음은 3 단계를 완료한 결과입니다.

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
