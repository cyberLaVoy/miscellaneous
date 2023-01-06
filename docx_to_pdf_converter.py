import comtypes.client
import os

msword = comtypes.client.CreateObject("Word.Application")
for filename in os.listdir(os.getcwd()):
    if ".doc" in filename:
        print("Processing", filename)
        fin = os.path.abspath(filename)
        fout = os.path.abspath(filename.split('.')[0]+".pdf")
        try:
            print("Opening file with Word.")
            document = msword.Documents.Open(fin)
            print("Saving file as PDF.")
            document.SaveAs(fout, FileFormat=17)
            print("Closing file.")
            document.close()
        except:
            print("Problem in processing.")
msword.quit()
    
