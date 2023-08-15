import csv 
icecream_menu = {
    'Chocolate': 175,
    'Vanila': 150,
   '21 Love': 200,
   'Cookies and Cream': 250,
   'Blueberry': 220
}
cone_menu = {
    'Regular': 100,
    'Waffle': 200
}
class Icecream:
    def __init__(self, name, price,coneName,cone, scoops):
        self.name = name
        self.price = price
        self.coneName = coneName
        self.cone = cone
        self.scoops = scoops
    def icecream_Name(self):
        print(self.name, self.price, self.coneName,self.cone, self.scoops)
    def calculate(self):
        self.total = (self.price * self.scoops) + self.cone
        print("Grand Total: ", self.total)

def main():
    print("-----ICECREAM MENU------")
    for ice,price in icecream_menu.items():
        print(ice , ": ", price)

    print("------CONE TYPE------")
    for cone,conePrice in cone_menu.items():
        print(cone," : ", conePrice)
    try:
        icecream = str(input("Enter the icecream of your choose: "))

        cone = str(input("Enter the cone you want: "))

        scoops = int(input("How many scoops do you want? "))
    
    
        if icecream in icecream_menu or cone in cone_menu or scoops is not None:
            obj_icecream = Icecream(icecream, icecream_menu[icecream], cone ,cone_menu[cone], scoops)
            obj_icecream.icecream_Name()
            obj_icecream.calculate()
            csvFile = input("Do you want to download the menu? \nYes or No ")
            if csvFile.lower() == 'yes':
                csv_file = "Menu.csv"
                file = open(csv_file, 'w+', newline='')
                for row,price in icecream_menu.items():
                    file.write(row)
                    file.write(" ")
                    file.write(str(price))
                    file.write("\n")
                file.close()
                
            else:
                print("Thank you!!")
        else:
            print("Please enter the flavor of icecream you want and your choice of cone again")

            print("-----ICECREAM MENU------")
            for ice,price in icecream_menu.items():
                print(ice , ": ", price)

            print("------CONE TYPE------")
            for cone,conePrice in cone_menu.items():
                print(cone," : ", conePrice)
            
            icecream = str(input("Enter the icecream of your choose: "))

            cone = str(input("Enter the cone you want: "))

            scoops = int(input("How many scoops do you want? "))

    except:
        print("Error")

if __name__=="__main__":
    main()