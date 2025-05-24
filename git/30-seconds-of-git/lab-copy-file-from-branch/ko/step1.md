# 다른 브랜치에서 파일 복사하기

`https://github.com/labex-labs/git-playground.git`라는 Git 저장소에서 프로젝트 작업을 하고 있습니다. `feature-1`과 `feature-2`라는 두 개의 브랜치가 있습니다. `feature-1` 브랜치에서 `feature-2` 브랜치로 `hello.txt` 파일을 복사해야 합니다.

1. 저장소 복제 (Clone):

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 디렉토리로 이동하고 ID 를 구성합니다:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `feature-1` 브랜치를 생성하고 전환한 다음, `hello.txt`라는 텍스트 파일을 생성하고 문자열 "hello,world"를 작성한 후 "add hello.txt" 메시지로 파일을 커밋합니다:

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
```

4. `master` 브랜치로 전환한 후 `feature-2` 브랜치를 생성하고 전환합니다:

```shell
git checkout master
git checkout -b feature-2
```

5. `feature-1` 브랜치에서 `feature-2` 브랜치로 `hello.txt` 파일을 복사하고 "copy hello.txt" 커밋 메시지로 커밋합니다:

```shell
git checkout feature-1 hello.txt
git commit -am "copy hello.txt"
```

6. `hello.txt` 파일이 `feature-2` 브랜치로 복사되었는지 확인합니다:

```shell
ll
```

`feature-2` 브랜치의 파일 목록에서 `hello.txt` 파일을 볼 수 있습니다:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
