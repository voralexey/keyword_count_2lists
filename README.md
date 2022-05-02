# keyword_count_2lists


The script takes a list of keywords for environmental sources (one keyword per line) and a list of NCBI headers (that includes an environmental source 
from which this sequence has been isolated) and counts occurrences of each keyword across all headers.

## AV / 26-4-2022

#### Python version.

3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)]

### Input files
1. A txt file with a list of keywords (e.g. blood, .*leaf.* (i.e. including regex)), one keyword per line. (e.g. list_of_keywords.txt)
2. A txt file with a list of headers (e.g. Homo sapiens|DSM:22607|type strain of Christensenella minuta|Japan|**feces**|2012) from NCBI 
that includes environmental source (e.g. all_origin_col1-.txt), one header per line

The file with headers is the output of the bash command grep "^>" myfile.fasta OR 
python script (https://github.com/voralexey/filter_NCBI_header_by_keywords):


### Output files
- A csv file with a keyword in the 1st column and a number of its occurrences in the NCBI headers in the 2nd column (e.g. "keyword_count_all.csv")
