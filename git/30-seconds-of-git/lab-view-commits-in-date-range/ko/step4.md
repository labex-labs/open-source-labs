# 상대 날짜 및 형식 옵션 사용

Git 은 또한 최근 활동을 빠르게 볼 수 있도록 매우 편리한 상대 날짜를 지원합니다.

지난 12 주 동안의 모든 커밋을 살펴보겠습니다.

```bash
git log --since='12 weeks ago'
```

이 명령을 실행하는 시점에 따라 해당 기간 내에 있는 모든 커밋 또는 일부 커밋만 볼 수 있습니다.

기타 유용한 상대 날짜 형식은 다음과 같습니다.

- `"X days ago"`
- `"X months ago"`
- `"yesterday"`
- `"last week"`

지난 1 년 동안의 커밋을 살펴보겠습니다.

```bash
git log --since='1 year ago'
```

이 명령어는 지난 1 년 동안 이루어진 모든 커밋을 표시합니다.

## 추가 형식 옵션

Git log 는 출력을 사용자 정의하기 위한 다양한 형식 옵션을 제공합니다. 몇 가지 유용한 옵션은 다음과 같습니다.

1. 각 커밋을 한 줄로 표시하는 보다 간결한 로그를 표시하려면:

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

출력은 다음과 같습니다.

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. 각 커밋에서 변경된 파일을 보려면:

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

이 명령어는 각 커밋에서 수정된 파일의 상태를 표시하며, 변경된 내용을 이해하는 데 도움이 될 수 있습니다.

이러한 형식 옵션은 날짜 필터와 결합하여 프로젝트의 히스토리를 보다 효과적으로 이해하는 데 도움이 되는 강력한 쿼리를 만들 수 있습니다.
