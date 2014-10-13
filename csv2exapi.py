# Converts csv file to a list of ex api statements
# @author Per-Henrik Kvalnes
import sys
import json

infile = open("allecampus13oktober2014.csv")
outfile = open("out.json", "w")

first = 0
header = {}

# static headers
email = "email"
name = "name"
code = "code"
timestamp = "completed"
codeprefix = "act:campus:"
verbID = "www.nob-ordbok.uio.no/perl/ordbok.cgi?OPP=fullføre&bokmaal=+&ordbok=bokmaal"

splitValue = ";"
jsonList = []

for line in infile:

    # if first time, prepare the header 
    if not first:
        line = line.strip("\n")
        keys = line.split(";")

        i = 0
        for key in keys:
            if key != "":
                header[key] = i
                i += 1

        print ("Headers")
        print ("-------")
        print (header)
        first = 1

    # if noe, make an json object
    else:

        line = line.strip("\n")
        values = line.split(splitValue)


        actorObj = {"mbox":values[header[email]]}
        verbObj = {"id":verbID}
        objectObj = {"id":codeprefix+values[header[code]]}
        paramsObj = {}
        timestampObj = values[header[timestamp]]

        obj = {"actor":actorObj, "verb":verbObj, 
               "params":paramsObj, "object":objectObj,
               "timestamp":timestampObj}
        jsonList.append(obj)

jsonString = json.dumps(jsonList, indent=4)
print(jsonString)
#outfile.write(jsonString)
#outfile.close()
