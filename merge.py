from PyPDF2 import PdfMerger, PdfReader
import os
mergedObject = PdfMerger()
download_dir = "C:\\Users\\Public\\Documents\\manga\\test"
download_dir_list = os.listdir(download_dir)
d1 = []
d2 = []
for i in download_dir_list:
    d2 = i.split()[0]
    d1.append(float(i.split()[1][:-4]))
d1.sort()
for i in d1:
    if not i.is_integer():
        mergedObject.append(PdfReader('C:\\Users\\Public\\Documents\\manga\\test\\'+ d2 + ' ' + str(i) + '.pdf', 'rb'))
        print('Added' + ' ' + d2 + ' ' + str(i) + '.pdf' + ' to merger.')
    else:
        mergedObject.append(PdfReader('C:\\Users\\Public\\Documents\\manga\\test\\'+ d2 + ' ' + str(int(i)) + '.pdf', 'rb'))
        print('Added' + ' ' + d2 + ' ' + str(int(i)) + '.pdf' + ' to merger.')
print('Processing...')
mergedObject.write("mergedfilesoutput.pdf")
print('Done!')