def addSemicolons(rfile, wfile):
    rfin = open(rfile, 'r')
    wfin = open(wfile, 'w')
    for line in rfin:
        line = line.rstrip()
        if len(line) > 0:
            if line[-1] not in "{}":
                line += ";"
        line += "\n"
        wfin.write(line)
    rfin.close()
    wfin.close()

def main():
    rfile = "scratch.js"
    wfile = "updated-" + rfile
    addSemicolons(rfile, wfile)
main()

