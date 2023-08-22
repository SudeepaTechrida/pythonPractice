class CSVSaver:
    def __init__(self):
        self.name = "CSV.csv"
    
    def addDetails(self, data):
        file = open(self.name, 'a')
        file.write(",".join(data)+"\n")
        file.close()
        print("Object added.")
    def readDetails(self):
        file = open(self.name, 'r')
        details = file.readlines()
        return details 
    
    def update(self, dataId, data):
       readdata = self.readDetails()
       if 0 <= dataId < len(readdata):
           readdata[dataId] = ','.join(data) + '\n'
           updateFile = open(self.name, 'w')
           updateFile.writelines(readdata)
           print("Row updated")
       else:
           print("Row index out of range.")
           
    @staticmethod
    def delete(name,deleteID):
        readData = open(name,'r')
        detail = readData.readlines()
        if 0 <= deleteID < len(detail):
            detail[deleteID] = ''
            deleteFile = open(name, 'w')
            deleteFile.writelines(detail)
            print("Row Deleted")
        else:
            print("Row index out of bound")
class Music(CSVSaver):
    def __init__(self, name):
        self.name = name
class Car(CSVSaver):
    def __init__(self, name):
        self.name = name
    
music_inst = Music("Music.csv")
music_inst.addDetails(['1','SEVENTEEN', 'SARA SARA'])
print(music_inst.readDetails())
music_inst.update(0,['1','Sara Sara', 'SEVENTEEN'])
Music.delete("Music.csv",0)

car_obj = Car("Car.csv")
# print(car_obj.name)
car_obj.addDetails(['1','Boleno','Suziki'])
print(car_obj.readDetails())
car_obj.update(0,['1','A-Star','Suzuki'])
Car.delete("Car.csv", 0)