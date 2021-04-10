import csv
import argparse
parser= argparse.ArgumentParser(description='A program that reads from / writes to a file')
parser.add_argument('path', help='path to csv file')
parser.add_argument("--file",  help="file to write to")

args = parser.parse_args()
given_csv=args.path
given_file=args.file


def print_file_content(file):
    with open(file) as file1:
        content = file1.read()
    print(content)
    
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file2:
        for tu in lst:
            for e in tu:
                file2.write(str(e)+'\n')
                
def read_csv(input_file):
    rows=[]
    with open(input_file) as file3:
        reader = csv.reader(file3)
        for row in reader:
            rows.append(row)   
    return rows

       
def read_given_csv(input_file, output_file):
    rows=[]
    with open(input_file) as file3:
        reader = csv.reader(file3)
        for row in reader:
            rows.append(row)   
        if(output_file==None):
            print(rows)
        else:
            write_list_to_file(output_file,rows)

read_given_csv(given_csv,given_file)