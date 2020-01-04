import os
import glob
import collections


SearchResults= collections.namedtuple('SearchResults', ['line', 'file', 'text'])



def main():
    print_header()
    folder=get_file_path()
    if not folder:
        print("Sorry can't search that")

    criteria=what_to_search_for()
    if not criteria:
        print("Sorry can't search for nothing")


    matches=search_folder(folder, criteria)
    match_count=0
    for m in matches:
        match_count+=1

        print('--------------MATCHES----------------')
        print('file: {}'.format(m.file))
        print('line: {}'.format(m.line))
        print('match: {}'.format(m.text.strip()))


    print ("We found {} matches".format(match_count))

def print_header():
    print ('----------------------------------------')
    print ('            FILE SEARCH APP')
    print ('----------------------------------------')


def get_file_path():
    user_input=input('where would you like to search?')

    if not user_input or not user_input.strip():
        return None
    if not os.path.abspath(user_input):
        return None
    return os.path.abspath(user_input)


def what_to_search_for():
    search_criteria=input('What word or phrase do you want to search for?')
    return search_criteria

def search_folder(folder_location, criteria):
    print('Will search {} for {}'.format(folder_location, criteria))
    items=glob.glob(os.path.join(folder_location, '*'))
    for i in items:
        full_item=os.path.join(folder_location, i)
        if full_item=='/Users/Krystal/Documents/Python Files/File Searcher App/venv':
            pass
        elif os.path.isdir(full_item):
            yield from search_folder(full_item,criteria)
        else:
            yield from search_file(full_item, criteria)



def search_file(file_path, criteria):
    with open(file_path, 'r', encoding='utf-8') as fin:
        line_number=0
        for line in fin:
            line_number+=1
            if line.lower().find(criteria)>=0:
                m=SearchResults(line=line_number, file=file_path, text=line)
                yield m



if __name__=='__main__':
    main()

