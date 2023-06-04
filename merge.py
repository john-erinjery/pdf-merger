from PyPDF2 import PdfMerger, PdfReader
import os
import shutil from rmtree
mergedObject = PdfMerger()
download_dir = f"{os.getcwd()}\\pdfs"
download_dir_list = os.listdir(download_dir)
d1 = []
for i in download_dir_list:
    num = i.split('.pd')[0]
    d1.append(int(num) if num.isdigit() else float(num))
d1.sort()
for i in d1:
    print('adding {}.pdf to merger'.format(i))
    mergedObject.append(PdfReader(os.path.join(download_dir, str(i) + '.pdf', 'rb'))
print('Processing...')
mergedObject.write('{}-{}.pdf'.format(max(d1), min(d1)))
print('deleting the temp folder..')
# rmtree(download_dir)
print('Done!')

