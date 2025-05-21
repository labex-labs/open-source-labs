# 특정 날짜 범위 내의 커밋 보기

이제 특정 날짜를 기준으로 커밋을 필터링하는 방법을 배우겠습니다. Git 은 이 목적을 위해 두 가지 유용한 옵션을 제공합니다.

- `--since` 또는 `--after`: 특정 날짜 이후의 커밋을 표시합니다.
- `--until` 또는 `--before`: 특정 날짜 이전의 커밋을 표시합니다.

이러한 옵션을 결합하면 특정 날짜 범위 내의 커밋을 볼 수 있습니다.

2023 년 4 월 25 일부터 2023 년 4 월 27 일 사이에 발생한 모든 커밋을 살펴보겠습니다.

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

이 명령어는 2023 년 4 월 25 일부터 4 월 27 일 사이에 만들어진 모든 커밋을 표시합니다. 출력은 다음과 같아야 합니다.

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

Git 은 다음과 같은 다양한 날짜 형식을 허용합니다.

- `"YYYY-MM-DD"` (예: `2023-04-25`)
- `"Month DD YYYY"` (예: `Apr 25 2023`)
- `"DD Month YYYY"` (예: `25 Apr 2023`)

다른 날짜 범위 내에 커밋이 있는지 확인하기 위해 다른 날짜 형식을 시도해 보십시오.

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

해당 기간 동안 커밋이 없으면 이 명령어가 결과를 반환하지 않을 수 있으며, 이는 정상입니다.
