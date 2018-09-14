#!/usr/bin/env python3

# hook to automate pytest. Called by "git commit" with no arguments.
# The hook should exit with non-zero status after issuing appropriate messages
#
# 1. create the file pre-commit in /.git/hooks/ (sample file may already exist)
# 2. specify environment (as indicated in line 1 here)
# 3. make the pre-hook file executable (chmod a+x ~/.git/hooks/pre-commit)
# 4. re-initialize git (git init)
#
# pytest exit codes ::
# ====================
# Exit code 0:	All tests were collected and passed successfully
# Exit code 1:	Tests were collected and run but some of the tests failed
# Exit code 2:	Test execution was interrupted by the user
# Exit code 3:	Internal error happened while executing tests
# Exit code 4:	pytest command line usage error
# Exit code 5:	No tests were collected

import sys
import subprocess


class m:  # terminal colors
    bf = '\033[1m'
    ul = '\033[4m'

    # colors
    r = '\033[91m'
    b = '\033[94m'
    bl = '\033[96m'
    g = '\033[92m'
    y = '\033[93m'
    e = '\033[0m'
    gy = '\033[1m\033[30m'

    # highlight
    r_ = '\x1b[0;37;41m'
    b_ = '\x1b[1;37;44m'
    g_ = '\x1b[1;37;42m'
    e_ = '\x1b[0m'


def check_status_code(code):
    exit_code_2 = m.bl + m.bf + "commit rejected: Tests were collected and run but some of the tests failed.\n" + m.e
    exit_code_3 = m.bl + m.bf + "commit rejected: Internal error happened while executing tests.\n" + m.e
    exit_code_4 = m.bl + m.bf + "commit rejected: pytest command line usage error.\n" + m.e
    exit_code_5 = m.bl + m.bf + "commit rejected: No tests were collected. \n" + m.e
    exit_code_6 = m.bl + m.bf + "commit rejected: Undefined exit code. \n" + m.e

    if code != 2:
        return exit_code_2, False

    elif code != 3:
        return exit_code_3, False

    elif code != 4:
        return exit_code_4, False

    elif code != 5:
        return exit_code_5, False

    else:
        return exit_code_6, False


def start_automated_testing():
    try:
        subprocess.check_call(["python3", "-m", "pytest", "-rxXs"])
        exit_state = m.bl + m.bf + "commit accepted: All tests were collected and passed successfully. \n" + m.e, True
    except subprocess.CalledProcessError as error:
        exit_state = check_status_code(error.returncode)

    if exit_state is not None:
        return exit_state
    else:
        return None


def main():
    commit_on_exit = True
    print(m.bl + m.bf + "\n\n ... starting tio test" + m.e)
    automated_test_results = start_automated_testing()

    if automated_test_results is not None:
        pytest_exit_report, is_committable = automated_test_results
        print(pytest_exit_report)
        commit_on_exit = is_committable

    return commit_on_exit


if __name__ == '__main__':
    commit = main()
    if not commit:
        sys.exit(1)
