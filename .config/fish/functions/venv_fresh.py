import os
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Optional, Tuple


def update_ruff(venv_path):
    #  call subprocess: pip install -U ruff
    with source_venv(venv_path):
        pass

@contextmanager
def source_venv(venv_path):
    # call subprocess: source .venv
    try:
        yield
    finally:
        # subprocess call to deactivate .venv
        pass


def find_path(search_path, search_text) -> Optional[str]:
    '''Brute force recursive directory search'''

    # get our current path and immediate parent path
    current_path = Path(search_path)
    parent_path = current_path.parent

    print('current path', current_path)
    print('parent path', parent_path)

    def gen_paths(path: Path):
        return [str(p) for p in path.iterdir()]

    # TODO itertools
    paths = gen_paths(current_path)
    paths.extend(gen_paths(parent_path))

    for p in paths:
        if search_text in p:
            return p
    else:
        home = str(current_path.home())
        # check if current parent's parent path is home or higher.
        # if it is, bail out recurssion. don't go higher than HOME dir.
        str_cur_p = str(parent_path.parent)
        if str_cur_p == home or home not in str_cur_p:
            return None

        return find_path(str(parent_path.parent), search_text)



def main():
    cwd = os.getcwd()

    venv_path = find_path(cwd, '.nope')

    if venv_path:
        print('found .venv at :', venv_path)
        update_ruff(venv_path)
    else:
        print('.venv not found')

if __name__ == '__main__':
    raise SystemExit(main())
