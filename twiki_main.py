import argparse
import re

from regex_patterns import *
from book_dictionary import *
from regex_patterns import *
from book_dictionary import *
from config_params import *

parser = argparse.ArgumentParser()
parser.add_argument('-s','--wiki_specimen', help='file path of source document', required=True, default='wiki_specimen/Wiki_Bible.html')
parser.add_argument('-m','--output_mode',   help='debug or other', required=True, default='my value')
parser.add_argument('-cc','--count_curtail',help='', required=True, default='120')

args = parser.parse_args()
wiki_specimen = args.wiki_specimen

print(wiki_specimen)




output_mode     = 'debug'   #debug, debug_shorties, free text, wiki
tiddler_count, count_curtail   = 0, 120
tid_body = ''
tid_type = ''
wiki = []

with open(wiki_specimen, encoding='utf8') as f:

    for line in f:
        if re.match(rgx_comment_tiddler, line):
            match = re.match(rgx_comment_tiddler, line)
            if match:
                if 'POST-SHADOW' not in tid_body and tid_body != '':
                    tiddler = {'type': tid_type, 'book_abbr': match.group('bk'), 'chap': match.group('ch'), 'vs': match.group('vs'), 'body': tid_body }
                    tiddler_title = f"{tiddler['book_abbr']}-{tiddler['chap']}-{tiddler['vs']}-note    {tiddler['body'][:60]}"
                    print(tiddler_title)
                    #print (tid_type, book_abbr, chap , vs, tid_body) 
                    pass
                tid_type = 'commentry'
                tid_body = ''
                book_abbr = match.group('bk')
                chap = match.group('ch')
                vs = match.group('vs')
                
                #tiddler = {'type': 'comment', 'book_abbr': match.group('bk'), 'chap': match.group('ch'), 'vs': match.group('vs'), 'body': tid_body }

        elif re.match(rgx_scriptr_tiddler, line):
            match = re.match(rgx_scriptr_tiddler, line)
            if match:
                if tid_body != '':
                    tiddler = {'type': tid_type, 'book_abbr': match.group('bk'), 'chap': match.group('ch'), 'vs': match.group('vs'), 'body': tid_body }
                    tiddler_title = f"{tiddler['book_abbr']}-{tiddler['chap']}-{tiddler['vs']}    {tiddler['body'][:60]}"
                    print(tiddler_title)
                    pass
                tid_type = 'scripture'
                tid_body = ''
                book_abbr = match.group('bk')
                chap = match.group('ch')
                vs = match.group('vs')

        else:
            tid_body = f'{tid_body}\n{line}'


#   for line in f:
#     if re.match(rgx_comment_tiddler, line):
#         match = re.match(rgx_comment_tiddler, line)
#         if match:
#             if 'POST-SHADOW' not in tid_body and tid_body != '':
#                 print (tid_type, book_abbr, chap , vs, tid_body) 
#             tiddler = {}
#             tid_type = 'comment'
#             tid_body = ''
#             book_abbr = match.group('bk')
#             chap = match.group('ch')
#             vs = match.group('vs')


            
#     elif re.match(rgx_scriptr_tiddler, line):
#         match = re.match(rgx_scriptr_tiddler, line)
#         if match:
#             if tid_body != '':
#                 print (tid_type, book_abbr, chap , vs, tid_body) 
#             tid_type = 'scripture'
#             tid_body = ''
#             book_abbr = match.group('bk')
#             chap = match.group('ch')
#             vs = match.group('vs')

#     else:
#         tid_body = f'{tid_body}\n{line}'

    