from PyPDF2 import PdfMerger, PdfReader
import os
mergedObject = PdfMerger()
download_dir = f"{os.getcwd()}\\pdfs"
download_dir_list = os.listdir(download_dir)
d1 = []
d2 = []
d3 = []
for i in download_dir_list:
    d3.append(int(i.split('.')[0]))
d3.sort()
for i in d3:
    d1.append(str(i))
for i in d1:
    if not i.is_integer():
        mergedObject.append(PdfReader(download_dir + d2 + ' ' + str(i) + '.pdf', 'rb'))
        print('Added' + ' ' + d2 + ' ' + str(i) + '.pdf' + ' to merger.')
    else:
        mergedObject.append(PdfReader(download_dir+ d2 + ' ' + str(int(i)) + '.pdf', 'rb'))
        print('Added' + ' ' + d2 + ' ' + str(int(i)) + '.pdf' + ' to merger.')
print('Processing...')
mergedObject.write("{}/mergedfilesoutput.pdf".format())
print('Done!')
