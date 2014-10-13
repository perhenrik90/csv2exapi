# Converts csv file to a list of ex api statements
# @author Per-Henrik Kvalnes
import sys
import json

class Csv2ExApi:

    inpath = "test.csv"
    header = {}
    first = 0

    # set column names in csv file
    email = "email"
    name = "name"

    objectID = "code"
    objectIDprefix = "act:campus:"
    timestamp = "completed"
    verbID = "www.nob-ordbok.uio.no/perl/ordbok.cgi?OPP=fullføre&bokmaal=+&ordbok=bokmaal"

    splitValue = ";"
    jsonList = []

    def __init__(self, splitValue=";"):
        self.splitValue = splitValue


    def setObjectPrefix(newidPrefix):
        # set a new prefix for object id's
        self.objectIDprefix = newidPrefix



    def execute(self):        
        # create json list as string
        infile = open(self.inpath)

        first = self.first
        header = self.header
        objectID = self.objectID
        objectIDprefix = self.objectIDprefix
        verbID = self.verbID
        email = self.email
        splitValue = self.splitValue
        jsonList = self.jsonList
        timestamp = self.timestamp

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

                    
            else:
            # if noe, make an json object
                line = line.strip("\n")
                values = line.split(splitValue)


                actorObj = {"mbox":values[header[email]]}
                verbObj = {"id":verbID}
                objectObj = {"id":objectIDprefix+values[header[objectID]]}
                timestampObj = values[header[timestamp]]
        
                obj = {"actor":actorObj, "verb":verbObj, 
                       "object":objectObj,
                       "timestamp":timestampObj}
                jsonList.append(obj)
                
        jsonString = json.dumps(jsonList, indent=4)
        return jsonString

cv = Csv2ExApi()
str = cv.execute()
print(str)
#print(jsonString)
#outfile.write(jsonString)
#outfile.close()
