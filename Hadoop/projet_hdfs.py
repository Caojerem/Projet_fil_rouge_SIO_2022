from hdfs.ext.kerberos import KerberosClient
import arxiv
import csv
import re
import datetime

search = arxiv.Search(
  query = "computer science &  ai",
    max_results = 10,
  sort_by = arxiv.SortCriterion.SubmittedDate
)
id = 0
rows = [['ID', 'Title', 'Author', 'Date','Year','Categorie'] ]
for result in search.results():
    author = result.authors
    author_list = [re.sub("[^A-Za-z0-9]","_",str(i)) for i in author]
    for i in range(len(author_list)):
        rows.append(list([str(id), str(result.title), str(author_list[i]), str(result.published),str(result.published.year),str(result.categories)]))
        id += 1

with open('Hadoop/dataset.csv', 'w',newline ='') as f:
    write = csv.writer(f)
    write.writerows(rows)


client = KerberosClient('http://hdfs-nn-1.au.adaltas.cloud:50070')

hdfs_path = '/education/cs_2022_spring_1/j.cao-cs/fil_rouge/'
client.upload(hdfs_path,
            'Hadoop/dataset.csv', 
            n_threads=1, 
            temp_dir=None, 
            overwrite = True,
            chunk_size=65536, 
            progress=None, 
            cleanup=True)
