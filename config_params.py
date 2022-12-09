#global output_mode
chunk_me_char_limit = 1000
#chunk_me_freeze     = -1
#chunk_me_nudge, chunk_me_prompt = 1.2, 1.3

#folder_path_root = "C:/Users/Boswell/Documents/Bible_Wiki_Project/"
folder_path_root = "C:/Users/Scott/Documents/Bible_Wiki_Project/"
folder_path_mid = "LEB-to-TW/"
folder_path_lists = "LEB-to-TW/Lists/"

folder_path_src_wiki = "doc_wiki_shell/"
folder_path_src_bible = "doc_source/Lexham/"
folder_path_src_bible = "doc_source/WEB/"
folder_path_target_file = "LEB-to-TW/doc_target/"
wiki_specimen = "wiki_specimen/Wiki_Bible.html"

source_document = "LEB_Galatians.txt"
source_document = "Test/LEB_test1_short.txt"
source_document = "Test/LEB_test1.txt"
source_document = "LEB.txt"
source_document = "Web0d.txt"

scriptr_file_source = folder_path_root+folder_path_src_bible+source_document
file_booklist       = folder_path_root+folder_path_lists+"bible_book_list.csv"

tiddler_count, char_count = 0, 0
str_passage, prose, v_passage, v_prose = "", "", "", ""
book_key, chap_title, vs_title, book_title = None, None, None, None
dead_zone, wrap_it = True, False 

def get_scriptr_file_source():
    return folder_path_root+folder_path_src_bible+source_document

# def get_file_booklist():
    # #C:\Users\Boswell\Documents\Bible_Wiki_Project\LEB-to-TW\doc_source
    # doc_name = "bible_book_list.csv"
    # return folder_path_root+folder_path_lists+doc_name

def get_file_target(output_mode):
    #TODO get a time-stamp onto the titles
    import time
    if "wiki" in output_mode:
        doc_name = "bible_wiki_FILL.htm"
    
    else:
        doc_name = "bible_passage.txt"
    return folder_path_root+folder_path_target_file+doc_name

#wiki_file_target    = get_file_target(output_mode)

def get_wiki_file_source():
    doc_name = "bible_wiki.htm"
    return folder_path_root+folder_path_mid+folder_path_src_wiki+doc_name

    
def get_wiki_specimen():
    return folder_path_root+wiki_specimen
    
def curtail(tiddler_count, debug_limit, char_count):
    if tiddler_count > debug_limit:
        avg = 0
        if tiddler_count > 0:
            avg = int(char_count/tiddler_count)
        print (tiddler_count, "Limit="+str(debug_limit), "Avg length is " + str(avg))
        quit()