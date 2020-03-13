import sys
import os
import subprocess as SP

import here.util as U
def run(cmd_string):
    cmd=cmd_string.split()
    return SP.Popen( cmd, stdout=SP.PIPE, stderr=SP.PIPE).stdout.read().decode('utf-8')

SPLIT=U.pad(U.str_split)
FILTER=U.fil
ASSERT=U.ASSERT


class GIT_REMOTE(BaseException): pass
class NOT_A_REPO_ROOT(GIT_REMOTE): pass
class NOT_A_REMOTE_NAME(GIT_REMOTE): pass

def is_git_root(path):
    return os.path.isdir(path+'/.git')


def remote4path4name(path, name):
    ASSERT( is_git_root(path),  NOT_A_REPO_ROOT, path  )
    os.chdir(path)
    out=run('git remote -v')
    lines=out.split('\n')
    lines=FILTER(lambda line: SPLIT(line)[0]==name, lines)
    ASSERT( lines, NOT_A_REMOTE_NAME, name )
    return lines[0].split()[1]

if __name__=='__main__':
    __main__()
