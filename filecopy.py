import shutil, os,csv
path = os.path.join('..','MTSD','MTSD.part1','MTSD')
files = os.listdir(os.path.join(path,'Detection'))

pictures = []
with open(os.path.join(path,'file_names.csv')) as csv_file:
    line_count=1
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if (line_count>1):
            pictures.append(row[0])
        line_count+=1

file_count = 0
for pic in pictures:
    shutil.copy(os.path.join(path,'Detection',pic),os.path.join(path,'export'))
