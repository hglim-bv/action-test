import sys


def check_arguments(arguments: list) -> None:
    if len(arguments) == 1:
        raise Exception('PR title 을 입력해 주세요.')
    if len(arguments) > 2:
        raise Exception('인자값은 1개만 입력 가능합니다.')


def check_pr_title(pr_title: str) -> None:
    allow_prefix = ['SV-']

    for prefix in allow_prefix:
        if pr_title.startswith(prefix):
            return

    raise Exception(f'PR title 은 {allow_prefix} 중 하나로 시작해야 합니다.')


if __name__ == '__main__':
    arguments = sys.argv
    check_arguments(arguments)

    pr_title = arguments[1]
    check_pr_title(pr_title)
