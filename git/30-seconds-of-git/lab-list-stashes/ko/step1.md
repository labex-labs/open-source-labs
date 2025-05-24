# 모든 스태시 나열하기

Git 저장소에서 프로젝트 작업을 하고 있으며 아직 커밋할 준비가 되지 않은 변경 사항이 있습니다. 다른 작업을 하기 위해 이러한 변경 사항을 스태시 (stash) 하기로 결정했습니다. 나중에 적용할 스태시를 결정하기 위해 생성한 모든 스태시 목록을 보고 싶습니다. Git 저장소의 모든 스태시를 어떻게 나열할 수 있을까요?

1. `git-playground` 디렉토리로 이동합니다:

```
cd git-playground
```

2. `test.txt`라는 새 파일을 만들고 내용을 추가합니다:

```
echo "hello,world" > test.txt
git add .
```

3. 다음 명령을 사용하여 변경 사항을 스태시합니다:

```
git stash save "Added test.txt"
```

4. `test2.txt`라는 다른 새 파일을 만들고 내용을 추가합니다:

```
echo "hello,labex" > test2.txt
git add .
```

5. 다음 명령을 사용하여 변경 사항을 스태시합니다:

```
git stash save "Added test2.txt"
```

6. 다음 명령을 사용하여 모든 스태시를 나열합니다:

```
git stash list
```

다음과 유사한 출력을 볼 수 있습니다:

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
