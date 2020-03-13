import sys
import os
import argparse
import here.magic as MM
import here.block as BB
import here.git as GG

MAGIC="# 834765q784q3"
target_profile_name = 'profile'
target_bashrc_name  = 'bashrc'

HOME=os.environ["HOME"]
fqpath_bashrc  = HOME + os.path.sep + '.bashrc'
fqpath_profile = HOME + os.path.sep + '.profile'

parser=argparse.ArgumentParser()
parser.add_argument( "--source" , help="Tell system to Clone from PATH" , metavar="PATH" , action="store")
parser.add_argument( "--remote" , help="With --source, tell system to clone from PATH's remote." , metavar="NAME" , action="store" , default=None)
parser.add_argument( "--dest" , help="Install to PATH" , metavar="PATH" , action="store" , default=None)
parser.add_argument( "--dryrun" , help="dry run" , action="store_true")
OPT=parser.parse_args()
if not OPT.source: exit( '--source required' )
if not OPT.dest: exit( '--dest required' )
if OPT.remote: OPT.source = GG.remote4path4name( OPT.source, OPT.remote )
OPT.dest    = '~' + os.path.sep + os.path.relpath( OPT.dest, HOME )
OPT.profile = OPT.dest + os.path.sep + target_profile_name
OPT.bashrc  = OPT.dest + os.path.sep + target_bashrc_name

magic=MM.Magic(MAGIC)
magic.inject_4fname4block(fqpath_profile, BB.profile_block(OPT) )
magic.inject_4fname4block(fqpath_bashrc, BB.bashrc_block(OPT) )

