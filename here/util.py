from subprocess import *
import time
NIL=''
EOL='\n'
SPACE=' '

if 'FUNC':
    listify = lambda fn : lambda *x,**y : list(fn(*x,**y))
    fil=listify(filter)
    def str_split(_str,*a,**b):
        return _str.split(*a,**b)

if 'MISC':
    def ASSERT( pred, exc, msg ):
        if not pred:
            raise exc(msg)

    def listget(_list,_index,_default=None):
        try:
            return _list[_index]
        except IndexError:
            return _default
    def __run(cmd_string):
        cmd=cmd_string.split()
        return Popen( cmd, stdout=PIPE, stderr=PIPE).stdout.read().decode('utf-8')

if 'PAD':
    pad_list = lambda it,val=None,n=10 : it + [val] * n
    pad_function = lambda fn,*x,**y : lambda *a,**b : pad_list(fn(*a,**b),*x,**y)
    def pad(f,*a,**b):
        try: return pad_list(list(f),*a,**b)
        except TypeError: return pad_function(f,*a,**b)



if 'MAGIC':
    def magic__magic_block_4block(magic, block, *x, **y):
        lines=block.split(EOL)
        return magic__magic_block_4lineS(magic, lines, *x, **y)

    def magic__magic_block_4lineS(magic, lineS, header=True, footer=True, indent=True):
        header = (header and ['######## BEGIN']) or []
        footer = (footer and ['######## END']) or []
        indent = (indent and SPACE*4) or NIL
        suffix = ' #magic--%s at %s ' % (magic, str(time.time()))
        lines = list(lineS[:])
        lines = header + [ indent + xx for xx in lines ] + footer
        lines = [ xx + suffix for xx in lines ]
        join = EOL.join(lines)
        return join

    def magic__cleanfile_4fname(magic,fname):
        def keep(line): return not magic in line
        with open(fname, 'r') as fd: new = NIL.join(filter(keep,fd.readlines()))
        with open(fname, 'w') as fd: fd.write(new)

    def  magic__inject_4fname_4block( magic, fname, block ):
        magic__cleanfile_4fname(magic,fname)
        with open(fname,'a') as fd:
            fd.write( magic__magic_block_4block( magic, block ) )

    def  magic__inject_4fname_4lineS( magic, fname, lines ):
        magic__cleanfile_4fname(magic,fname)
        with open(fname,'a') as fd:
            fd.write( magic__magic_block_4lineS( magic, lines ) )


    #def magic_joiner_4_magic(magic):
    #    import time
    #    magic = magic + ' ' + str(time.time())
    #    def inner(lines):
    #        return join4lines4magic(lines,magic)
    #    return inner

    #def filecleaner4magic(magic):
    #    def inner(fname):
    #        def keep(line): return not magic in line
    #        with open(fname, 'r') as fd: new = NIL.join(filter(keep,fd.readlines()))
    #        with open(fname, 'w') as fd: fd.write(new)
    #    return inner
