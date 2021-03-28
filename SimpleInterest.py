class SI:
    
    def __init__(self):
        while(True):#Loop to take only a valid value for Principal amount as Input 
            self.P = input("Enter the value of Principal amount(Rupees): ")
            try:
                if(float(self.P)):#Checks if the input value can be converted into floating point number
                    break
            except:
                print("\nEnter a valid input")
                continue
        while(True):#Loop to take only a valid value for Time as Input
            self.T = input("Enter the value of Time period(Years): ")
            try:
                if(float(self.T)):#Checks if the input value can be converted into floating point number
                    break
            except:
                print("\nEnter a valid input")
                continue
        while(True):#Loop to take only a valid value for Rate as Input
            self.R = input("Enter the value of Rate of Interest(% per year): ")
            try:
                if(float(self.R)):#Checks if the input value can be converted into floating point number
                    break
            except:
                print("\nEnter a valid input")
                continue
        
    def calcSI(self):#Function to calculate and return the value of Simple Interest
        self.P = float(self.P)#Typecasting to float 
        self.T = float(self.T)#Typecasting to float 
        self.R = float(self.R)#Typecasting to float 
        SimInt = (self.P*self.T*self.R)/100#Calculates the value of simple interest from P,T,R
        return(SimInt)
    
if __name__ == '__main__':#The code below runs only if the program is run directly and not if imported 
    Obj = SI()#creating an object of type SI
    SimInt = Obj.calcSI()#calling calcSI() and storing the value of Simple Interest calc in SimInt
    print("\nSimple interest for given values of P, T, R = ",SimInt)
    