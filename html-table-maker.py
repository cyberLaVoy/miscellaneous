"""This code will create a table in HTML format.
First it will ask how many table rows, and columns;
based on that input, it will ask for cell values;
finally, it will print out the html code to use"""

def rows():
    rows = int(input("How many rows for table?: "))
    return rows
    
def columns():
    columns = int(input("How many columns for table?: "))
    return columns
    

def dataentry(x,y):
    datalist = []
    htmldata = []
    htmlrow = []
    for imain in range(x+1):
        
        if len(datalist) > 0:
            for i in range(len(datalist)):
                htmldata.append("<td> " + str(datalist[i]) + " </td>")
                
        if len(htmldata) > 0:
                htmlrow.append("<tr>")
                for i in range(len(htmldata)):
                    htmlrow.append(str(htmldata[i]))
                htmlrow.append("</tr>")
                
        htmldata = []
        datalist = []
        
        if imain < x:
            
            print("For row #" + str(imain+1) + "...")
            iprime = 0
            while len(datalist) < y:
                datalist.append(input("Enter data for cell " + str(iprime+1) + ": "))
                iprime += 1
                
    return htmlrow
                   
def main():
    x = rows()
    y = columns()
    z = dataentry(x,y)
    print("<table>")
    for i in range(len(z)):
        print(str(z[i]), end="\n")
    print("</table>")
main()
