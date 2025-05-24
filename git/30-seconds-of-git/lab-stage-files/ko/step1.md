# 스테이징 영역에 파일 추가하기

`https://github.com/labex-labs/git-playground`라는 이름의 Git 저장소에 저장된 프로젝트 작업을 하고 있습니다. 코드베이스에 몇 가지 변경 사항을 적용했으며 이러한 변경 사항을 저장소에 커밋하려고 합니다. 그러나 모든 변경 사항이 아닌 특정 변경 사항만 커밋하려는 경우, 파일을 스테이징 영역에 추가해야 합니다.

1. `git-playground` 디렉토리에서 몇 가지 변경 사항을 적용합니다.

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. 이러한 파일을 스테이징 영역에 추가합니다.

```shell
git add index.html style.css
```

3. 현재 작업 디렉토리 및 스테이징 영역의 상태를 확인합니다. 수정된 파일, 스테이징 영역에 추가된 파일 등에 대한 정보를 포함합니다.

```shell
git status
```

4. 또는 `.js` 확장자를 가진 모든 파일을 추가합니다.

```shell
git add *.js
```

5. 현재 작업 디렉토리 및 스테이징 영역의 상태를 다시 확인합니다.

```shell
git status
```

6. 모든 변경 사항을 스테이징 영역에 추가할 수도 있습니다.

```shell
git add .
```

7. 현재 작업 디렉토리 및 스테이징 영역의 상태를 다시 확인합니다.

```shell
git status
```

다음은 최종 결과입니다.

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
