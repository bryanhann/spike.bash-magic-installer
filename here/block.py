
PROFILE_BLOCK_TEMPLATE="""
[  -d %s ] || git clone %s %s
source %s %s
""".strip()

BASHRC_BLOCK_TEMPLATE="""
source %s %s
""".strip()

def profile_block(OPT):
    return PROFILE_BLOCK_TEMPLATE % ( OPT.dest, OPT.source, OPT.dest, OPT.profile, OPT.dest)

def bashrc_block(OPT):
    return BASHRC_BLOCK_TEMPLATE % (OPT.bashrc, OPT.dest)

