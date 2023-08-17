class Music:
    def __init__(self, name):
        self.name = name 

    @staticmethod 
    def createCSV(name):
        file = open(name, 'a')

    def addDetails(self, data):
        file = open(self.name, 'a')
        file.write(",".join(data)+"\n")
        file.close()
        print("Music added.")
    def readDetails(self):
        detail = []
        file = open(self.name, 'r')
        details = file.read()
        for line in details:
            split1 = line.strip().split(",")
            detail.append(split1)
        return detail
    
    def editDetails(self, dataId):
        data =  self.readDetails()
        value = data[dataId]
        return value
    def update(self, data,dataId):
        editData = self.editDetails(dataId)
        if 0 <= dataId < len(editData):
            editData[dataId] = data
            file = open(self.name, 'a+')
            file.write(','.join(data)+'/n')
            return True
        return False
    def delete(self, deleteID):
        deleteData = self.editDetails(int(deleteID))
        rows = self.readDetails()
        if 0 <= int(deleteID) <len(deleteData):
            deleteData[dataId]= ''
            file = open(self.name, 'w')
            for row in rows:
                file.write(','.join(row)+'\n')
            file.close()
            return True
        return False

        
class Korean(Music):
     def __init__(self, filename):
        super().__init__(filename)

csvName = input("Enter the name to save the csv file with .csv extension: ")


musicChild = Korean.createCSV(csvName)
musicChild = Korean(csvName)

musicId = int(input("Id: "))
musicName = str(input("Name of the song: "))
musicBand = str(input("Name of the artist: "))

if musicId and musicBand and musicName is not None:
    musicChild.addDetails([str(musicId), musicName, musicBand])
    print(musicChild.readDetails())
    dataId = int(input("Enter the id you want to edit: "))
    musicChild.editDetails(dataId)
    data = input("Enter the changes you want: ")
    musicChild.update(data, dataId)
    deleteId = input("Enter the data number you want to delete: ")
    musicChild.delete(deleteId)