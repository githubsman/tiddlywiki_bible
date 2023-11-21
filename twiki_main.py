import argparse
import re

from regex_patterns import *
from book_dictionary import *
from regex_patterns import *
from book_dictionary import *
#from config_params import *

parser = argparse.ArgumentParser()
parser.add_argument('-s','--wiki_specimen', help='file path of source document', required=True, default='wiki_specimen/Wiki_Bible.html')
parser.add_argument('-m','--output_mode',   help='debug or other', required=True, default='my value')
parser.add_argument('-cc','--count_curtail',help='', required=True, default='120')

args = parser.parse_args()
wiki_specimen = args.wiki_specimen


print(wiki_specimen)

def consummate_tiddler():
    print(tiddler_count, tid_type.upper(), tiddler_title)
    print(tiddler['body'][:tiddler_truncate])



output_mode     = 'debug'   #debug, debug_shorties, free text, wiki
tiddler_count, count_curtail, tiddler_truncate   = 0, 120, 100
tid_body = ''
tid_type = ''
content = False
wiki = []

with open(wiki_specimen, encoding='utf8') as f:

    for line in f:
        if content == True:

            if re.match(rgx_comment_tiddler, line):

                consummate_tiddler(tiddler_count, tid_type, tiddler_title, tid_body)

                match = re.match(rgx_comment_tiddler, line)

                tid_type = 'commentry'
                book_abbr = match.group('bk')
                chap = match.group('ch')
                vs = match.group('vs')
                tiddler = {'type': tid_type, 'book_abbr': match.group('bk'), 'chap': match.group('ch'), 'vs': match.group('vs')}
                tiddler_title = f"{tiddler['book_abbr']}-{tiddler['chap']}-{tiddler['vs']}"

                tid_body = ''
                tiddler_count +=1
                
                #tiddler = {'type': 'comment', 'book_abbr': match.group('bk'), 'chap': match.group('ch'), 'vs': match.group('vs')}

            elif re.match(rgx_scriptr_tiddler, line):
                
                consummate_tiddler
                
                match = re.match(rgx_scriptr_tiddler, line)

                tid_type = 'scripture'
                tid_body = ''
                tiddler = {'type': tid_type, 'book_abbr': match.group('bk'), 'chap': match.group('ch'), 'vs': match.group('vs'), 'body': tid_body }
                tiddler_title = f"{tiddler['book_abbr']}-{tiddler['chap']}-{tiddler['vs']}"

                book_abbr = match.group('bk')
                chap = match.group('ch')
                vs = match.group('vs')
                tiddler_count +=1

            else:
                #if tid_type != '':
                tiddler['book_abbr'] = f'{tiddler["book_abbr"]}~{line.rstrip()}'
                #pass
        
        if content == False:
            content = 'storeArea' in line

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

    