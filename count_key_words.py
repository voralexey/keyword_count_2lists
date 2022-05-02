import csv
import re
from tqdm import tqdm # progress bar

# keywords = ['keyword_1', 'keyword_2', 'keyword_3']
# occurrences = []

# with open("list_of_keywords.txt") as keyword_list:
#     keywords = keyword_list.readlines()

with open("key_words_plain_list_AV.txt") as keyword_list: # list_of_keywords.txt
    keywords = [keyword.rstrip() for keyword in keyword_list]
    keywords = [word.replace(" ", "_") for word in keywords]  # replace " " with "_"
    keywords = [("_" + word + "_") for word in keywords]  # add "_" before and after each keyword
    keywords = list(filter(None, keywords))

with open("all_txt_diff_v3.out") as my_file: # file with NCBI headers (my_file.txt) test_100_headers.txt
    headers = my_file.readlines()

list_dict = {keyword:0 for keyword in keywords}

# regex in keywords
for header in tqdm(headers): # shows a % progress bar
    sub_header = "_" + re.sub(r'\W+', '_', header).rstrip("\n").lower() + "_"  # substitute all NON alphanumerics with "_"
    for keyword in list_dict.keys():
        if re.search(re.compile(keyword), sub_header) is not None:
            list_dict[keyword] += 1
            with open('keyword_count_all_regex.csv', 'w') as csv_file: # 'keyword_count_all.csv'
                writer = csv.writer(csv_file)
                for key, value in list_dict.items():
                    writer.writerow([key, value])

# NO REGEX IN KEYWORDS
# for header in tqdm(headers): # shows a % progress bar
#     for keyword in list_dict.keys():
#         if header.find(keyword) != -1:
#             list_dict[keyword] += 1
#             with open('keyword_count_all.csv', 'w') as csv_file:
#                 writer = csv.writer(csv_file)
#                 for key, value in list_dict.items():
#                     writer.writerow([key, value])
    #print(list_dict)

# count = 0
# for keyword in keywords:
#     # count = headers.count(keyword)
#     # occurrences.append(count)
#
#     for header in headers:
#         header = header.strip().lower().split()
#         for word in header:
#             if word.find(keyword.lower()) != -1:
#                 print(word)
#                 count += 1
#     with open('keyword_count.txt', 'a') as keyword_count:
#         keyword_count.write(f"{keyword} - {count}")
#
# # print(f"{keyword} - {count}")
