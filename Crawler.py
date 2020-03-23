import os

# Lets start to be a Spider Woman!
# each website I craw is a seperate proj(folder)

def create_proj_dir(dir):
    if not os.path.exists(dir):
        print('create proj' + dir)
        os.makedirs(dir)

# create queue & crawl files (if not created)
# https://www.vogue.in/horoscope/collection/monthly-love-relationships-horoscope-09-september-2019-zodiac-signs/
def create_data_files(proj_name, base_url):
    queue = proj_name + '/queue.txt'
    crawled = proj_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create file now
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data, '\n')

# delete file content
def delete_file_content(path):
    with open(path, 'w'):
        pass

# read file & convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rtf') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate thru a set, each line will be a new line in the file
def set_to_file(links, file):
    delete_file_content(file) # clean old data.
    for link in sorted(links):
        append_to_file(file, link)


