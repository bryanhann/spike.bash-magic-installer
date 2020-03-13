#from here.constants import EOL, NIL
#from subprocess import *
import time
EOL='\n'
NIL=''
SPACE=' '
class Magic:
    def __init__(self,magic):
        self._magic = magic

    def block4block(self, block, *x, **y):
        return self.block4lines(block.split(EOL), *x, **y)

    def block4lines(self, lines, header=True, footer=True, indent=True):
        header = (header and ['######## BEGIN']) or []
        footer = (footer and ['######## END']) or []
        indent = (indent and SPACE*4) or NIL
        suffix = ' #magic--%s at %s ' % (self._magic, str(time.time()))
        aa =  header + [ indent + xx for xx in lines ] + footer
        bb = [ xx + suffix for xx in aa ]
        return EOL.join(bb)

    def clean_4fname(self,fname):
        def keep(line): return not self._magic in line
        with open(fname, 'r') as fd: new = NIL.join(filter(keep,fd.readlines()))
        with open(fname, 'w') as fd: fd.write(new)

    def inject_4fname4block( self, fname, block ):
        self.clean_4fname(fname)
        with open(fname,'a') as fd:
            fd.write( self.block4block( block ) )

    #def  inject_4fname_4lineS( self, fname, lines ):
    #    self.clean(fname)
    #    with open(fname,'a') as fd:
    #        fd.write( self.mblock_4lineS(lines) )


