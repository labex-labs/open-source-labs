# 삭제된 파일 복원하기

Git 을 사용하여 프로젝트를 진행하던 중 실수로 필요한 `file2.txt` 파일을 삭제했습니다. 다행히 파일이 삭제된 커밋을 알고 있습니다. 이 랩의 목표는 Git 을 사용하여 삭제된 파일을 복원하는 것입니다.

이 랩을 완료하려면 `https://github.com/labex-labs/git-playground.git`에서 제공되는 Git 저장소 `git-playground`를 사용합니다. 다음 단계를 따르세요.

1. `cd git-playground` 명령을 사용하여 저장소 디렉토리로 이동합니다.
2. `git log --oneline` 명령을 실행하여 커밋 기록을 확인합니다.
3. "Added file2.txt" 메시지와 함께 파일이 삭제된 커밋을 식별합니다.
4. `git checkout <commit> -- <file>` 명령을 실행하여 지정된 `<commit>`에서 삭제된 지정된 `<file>`을 복원합니다. `<commit>`을 커밋 해시로, `<file>`을 삭제된 파일의 이름으로 바꿉니다.

예를 들어, `file2.txt` 파일이 `d22f46b` 커밋에서 삭제되었다면 다음 명령을 실행합니다.

```shell
git checkout d22f46b -- file2.txt
```

이렇게 하면 `file2.txt` 파일이 로컬 저장소로 복원됩니다.

다음은 `ll` 명령 실행 결과입니다.

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
