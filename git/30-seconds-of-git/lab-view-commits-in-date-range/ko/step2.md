# 기본 Git Log 명령어 탐색

이제 리포지토리를 복제했으므로 `git log` 명령어를 사용하여 커밋 히스토리를 보는 방법을 알아보겠습니다.

`git log` 명령어는 가장 최근 커밋부터 시작하여 리포지토리의 모든 커밋 목록을 표시합니다. 각 커밋 항목에는 다음이 포함됩니다.

- 고유한 커밋 해시 (식별자)
- 작성자 정보
- 커밋 날짜 및 시간
- 커밋 메시지

기본 커밋 히스토리를 살펴보겠습니다.

```bash
git log
```

다음과 유사한 출력을 볼 수 있습니다.

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

출력이 길 경우 다음을 사용하여 탐색할 수 있습니다.

- `Space` 키를 눌러 앞으로 이동
- `b` 키를 눌러 뒤로 이동
- `q` 키를 눌러 로그 보기 종료

각 커밋에는 고유 식별자 (긴 16 진수 문자열), 작성자 정보, 커밋 날짜 및 시간, 그리고 변경 사항을 설명하는 메시지가 있습니다.
