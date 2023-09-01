import csv

class csvReader:

    def Reader(cFile):
        with open(cFile,"r") as f:
           reader = csv.reader(f)
           output = []
           for row in reader:
              output.append(row)
           return output

    def FileFormatCertification(arg):
        key = arg[0][0]
        if key == "ThisIsAKey.":
           return True
        else:
           return False
    
    def ReadOriginal(arg):
        shape = []
        for ii in range(3):
           shape.append(arg[0][ii])
        return shape

      
