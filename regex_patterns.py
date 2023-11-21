import re

####### Patterns to identify special-template tiddlers in my 
#######     Bible TiddlyWiki document

## MARK re.VERBOSE for legible comparison string.  
##  Block comment allows easy read + explanations per line.
##  VERBOSE says whitespace will be ignored (though :-[ it still shows in Code debug panel)

rgx_scriptr_tiddler = re.compile(r'''
    ^<div\stitle=\"                    
    (?P<bk>([1-3])?[A-Z][a-z]{1,20})\-  ## bk   = book_abbr
    (?P<ch>\d{1,3})\-                   ## ch   = chap
    (?P<vs>\d{1,3})\"                   ## vs   = vs
    ''', re.VERBOSE)

## the COMMENTARY tiddler has the same syntax for title but with '-note' suffix. 
rgx_comment_tiddler = re.compile(r'''
    ^<div\stitle=\"
    (?P<bk>([1-3])?[A-Z][a-z]{1,20})\-  ## bk   = book_abbr
    (?P<ch>\d{1,3})\-                   ## ch   = chap
    (?P<vs>\d{1,3})\-note\"             ## vs   = vs
    ''', re.VERBOSE)


## for dealing with markdown '----' (horiz line)
#rgx_twiki_hz    = re.compile(r"\-\-\-\-")


