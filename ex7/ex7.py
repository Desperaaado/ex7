from os import path
import argparse
import re
import glob

def parse():
    parser = argparse.ArgumentParser(
        description='Realize sth like "grep" command.'
    )
    parser.add_argument('keyword', help='keyword for search.')
    parser.add_argument('files_name', help='file(s) name')
    parser.add_argument('addr', nargs='?', help='search range.[optional]')
    parser.add_argument(
        '-escape',
        help='disable <regular> function',
        action='store_true'
    )
    return parser.parse_args()

def search_keyword(keyword, file_name):
    find_flag = 0
    with open(file_name) as f:
        for line in f.readlines():
            if re.search(keyword, line):
                print(line)
                find_flag += 1
    return find_flag

def find_files(files_name, addr):
    if not addr:
        addr = '.'
    files_path = path.join(addr, files_name)
    return glob.glob(files_path)

def search_key_from_files(keyword, files_list):
    for file in files_list:
        print('='*15, '<<', file, '>>', '='*15)
        find_flag = search_keyword(keyword, file)
        print(f'>> {find_flag} line(s) in this file.')

def escape_regular(keyword, escape):
    if escape:
        return re.escape(keyword)
    else:
        return keyword

args = parse()
files_list = find_files(args.files_name, args.addr)
keyword = escape_regular(args.keyword, args.escape)
search_key_from_files(keyword, files_list)
