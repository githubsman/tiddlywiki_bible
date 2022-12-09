import re

####### Patterns for TiddlyWiki doc

rgx_scriptr_tiddler = re.compile(r'''^<div\stitle=\"                    
                                    (?P<bk>([1-3])?[A-Z][a-z]{1,20})\-  ## bk   = book_abbr
                                    (?P<ch>\d{1,3})\-                   ## ch   = chap
                                    (?P<vs>\d{1,3})\"                   ## vs   = vs
                                    ''', re.VERBOSE)

rgx_comment_tiddler = re.compile(r'''^<div\stitle=\"
                                    (?P<bk>([1-3])?[A-Z][a-z]{1,20})\-  ## bk   = book_abbr
                                    (?P<ch>\d{1,3})\-                   ## ch   = chap
                                    (?P<vs>\d{1,3})\-note\"             ## vs   = vs
                                    ''', re.VERBOSE)



#rgx_twiki_hz    = re.compile(r"\-\-\-\-")


