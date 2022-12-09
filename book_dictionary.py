'''
def __main__():
    import re
    #global booklist
    global book_title
'''
import re
rgx_book_specs = \
    re.compile(r"^\s*(?P<order>\d\d\d),\s*(?P<book_key>([1-3]\s)?.*),\s*(?P<chunk_size>.*)\s*,\s*(?P<name_wiki>.*)\s*,\s*(?P<name_pretty>.*)\s*,\s*(?P<name_awkward>.*)\s*$")
    # order = match.group("order")
    # chunk_size = match.group("chunk_size")
    # name_wiki = match.group("name_wiki")
    # name_pretty = match.group("name_pretty")
    
def book_spec(which_key, file_booklist, which_spec):
    # This is a fake dictionary.  I like it.
    
    file_r = open( file_booklist, "r", encoding="utf8" )

    for line in file_r:
      if not line.startswith("#"):
        match = re.match(rgx_book_specs, line)
        
        book_key = match.group("book_key")
        if which_key == book_key:
            my_spec = match.group(which_spec)
            break
        # print (order, book_key, chunk_size, name_wiki, name_pretty)

    file_r.close()
    return my_spec
    
#test above function... press f6 with this doc in focus.
#book_list('C:/Users/Boswell/Documents/Bible_Wiki_Project/LEB-to-TW/Lists/bible_book_list w whitespace.csv')
#ook_list()


def get_book_pretty(book_key, file_booklist, booklist):
    book_title = book_spec(book_key, file_booklist, "name_pretty")
    #book_title.strip
    book_title = book_title.strip(r" ")
    return book_title

def get_chunk_size(book_key, file_booklist, chunk_me_char_fudge):

    chunk_size = 501
    chunk_size = book_spec(book_key, file_booklist, "chunk_size")
    chunk_size = int(chunk_size)
    chunk_size = ( chunk_size * chunk_me_char_fudge )
    
    return chunk_size

def get_tiddler_title(book_key, chap, vs, file_booklist):
    book_stub = book_spec(book_key, file_booklist, "name_pretty")
    if "Ps" in book_stub:
        fill = 3
    else:
        fill = 2
    
    if vs == 0: 
        vs = 1      #deal with Psalm intro "verse zero"
    
    f_chap = str(chap)
    f_vs = str(vs)
    f_chap = "-" + f_chap.zfill(fill)
    f_vs = "-" + f_vs.zfill(fill)
    
    return book_stub+f_chap+f_vs