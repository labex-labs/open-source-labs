# 수동으로 버그를 발생시킨 커밋 찾기

`git-playground` 저장소에서 버그를 발생시킨 커밋을 수동으로 찾는 것이 과제입니다. 저장소는 `https://github.com/labex-labs/git-playground`에서 찾을 수 있습니다. 버그는 `file2.txt` 파일이 "This is file2.txt." 대신 "This is file2."를 출력해야 한다는 것입니다.

이 랩을 완료하려면 `git bisect` 명령을 사용하여 저장소의 커밋 기록을 이진 검색해야 합니다. 버그를 발생시킨 커밋을 좁힐 때까지 커밋을 "good" (버그 없음) 또는 "bad" (버그 있음) 로 표시해야 합니다.

1. 저장소 디렉토리로 이동합니다:

```
cd git-playground
```

2. `git bisect` 프로세스를 시작합니다:

```
git bisect start
```

3. 현재 커밋을 "bad"로 표시합니다:

```
git bisect bad HEAD
```

4. "Initial commit" 메시지가 있는 커밋을 "good"으로 표시합니다. Git 은 자동으로 테스트할 새 커밋을 체크아웃합니다:

```
git bisect good 3050fc0de
```

Git 은 자동으로 테스트할 새 커밋을 체크아웃합니다. 5. 체크아웃된 `file2.txt` 파일의 내용이 버그와 일치하지 않으면 "good"으로 표시합니다:

```
cat file2.txt
git bisect good
```

6. 체크아웃된 `file2.txt` 파일의 내용이 버그와 일치하면 "bad"로 표시합니다:

```
git bisect bad
```

7. 버그가 있는 커밋을 찾았으면 `git bisect` 프로세스를 재설정합니다:

```
git bisect reset
```

이제 버그가 있는 커밋의 코드 변경 사항을 검사하여 버그의 원인을 찾을 수 있습니다.

다음은 테스트 결과입니다:

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 is the first bad commit
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
