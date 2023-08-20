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
        file = open(self.name, 'r')
        details = file.readlines()
        return details 

    def update(self, data,dataId):
        editData = self.readDetails()
        # print(editData)
        if 0 <= dataId < len(editData):
            editData[dataId] = data
            print(editData[dataId])
            file = open(self.name, 'a+')
            file.write(data)
            file.write("\n")
            # return True
        return False   

    def delete(self, deleteID):
        rows = self.readDetails()
        print(rows)
        if 0 <= int(deleteID):
            if rows[int(deleteID)] in rows:
                rows[int(deleteID)] == ''
                file = open(self.name,'w+')
                file.write(rows[int(deleteID)])
                # for i in rows:
                #     file.write(i)
                file.close()
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
    data = input("Enter the changes you want: ")
    musicChild.update(data, dataId)
    deleteId = input("Enter the data number you want to delete: ")
    musicChild.delete(deleteId)