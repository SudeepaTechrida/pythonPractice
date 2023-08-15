class CSV_Saver:
    def __init__(self):
        self.name = "Parent CSV"
    def csv_file(self):
        self.csv_file = self.name + ".csv"
    def createCSV(self):
        self.file = open(self.csv_file, 'w',newline='')
        self.file.write('Hello \nWelcome \nto Python')
        self.file.close()
class ChildCSV_Saver(CSV_Saver):
    def __init__(self):
        self.name = "Child CSV"
    def csv_file(self):
        self.csv_file = self.name + ".csv"

objParent = CSV_Saver()
objChild = ChildCSV_Saver()

objChild.csv_file()
objChild.createCSV()