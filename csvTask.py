class CSVSaver:
    def __init__(self, name):
        self.name = name
    
    def addDetails(self, data,):
        file = open(self.name + '.csv', 'a')
        file.write(",".join(data)+"\n")
        file.close()
        print("Object added.")
    def readDetails(self):
        file = open(self.name + '.csv', 'r')
        details = file.readlines()
        return details 

    def update(self, data,dataId):
        editData = self.readDetails()
        oneData = editData[dataId]
        if dataId >=0:
            file = open(self.name+'.csv', 'w')
            if oneData in editData:
                file.writelines(','.join(data)+'\n')
            else:
                file.write(','.join(editData)+'\n')
            file.close()
            print("Object Edited.")


    def delete(self, deleteID):
        rows = self.readDetails()
        deletedata = rows[deleteID]
        file = open(self.name+'.csv', 'w')
        if deletedata:
            deletedata = ''
            file.write(deletedata)
        else:
            file.write(','.join(rows)+'\n')
        file.close()
        print("Object Deleted")
        
class Music(CSVSaver):
    def __init__(self, id, name, artist):
        self.name = name
        self.id = id
        self.artist = artist
class Car(CSVSaver):
    def __init__(self,id,name,model):
        self.name = name
        self.id = id
        self.model = model
    
# music_inst = Music('1', 'SARA SARA', 'Seventeen')
# music_inst.addDetails(['1','SEVENTEEN', 'SARA SARA'])
# print(music_inst.readDetails())
# music_inst.update(['1','Sara Sara', 'SEVENTEEN'],0)
# music_inst.delete(0)

car_obj = Car(1,'Boleno','Suziki')
car_obj.addDetails(['1','Boleno','Suziki'])
car_obj.readDetails()
car_obj.update(['1','A-Star','Suzuki'],0)
car_obj.delete(0)