# pdf-merger
PDF Merger software written in Python

Hello there! I made this software for merging PDFs a few at a time. I decided just to publish this on Github in case someone found it useful. If you want me to improve
the documentation and the code, give this repo a star so I know someones intrested!

As it is, you can use this repo by cloning this repo and installing a single dependency : PyPDF2
to install the dependency, run : 
```
pip install PyPDF2
```

## Usage
If you have a few pdfs you wanna merge, put them all in a single folder called `pdfs` (NOTE : the naming is important) and then run this python script from the parent folder.
The script will search for PDFs within the folder `pdfs` and merge them

> Note that the PDFs should be numbered as numerals, ie : 1.pdf, 2.pdf etc.. this is to make sure that the merged PDF is sorted properly

As for the .bat file this repo comes with, you can open it in notepad, in place of <python-path> put the absolute path to your python interpreter, in place of <merge.py-path>
add the path to the merge.py file
This way, if you add the merge.bat file to a folder that is in the PATH variable, you can access this program from within any folder.

If you don't get it, open an issue lol, i'll clear it then
