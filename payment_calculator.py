print("Welcome to the bill payment calculator.\n\n")
total = float(input("What is the total bill? :"))
tip = int(input("How much percent tip would you like to give? :"))
people = int(input("How many people to split the bill? :"))

def calculator():
    billWithTip = total * (1 + (tip / 100))
    forEachPerson = billWithTip / people
    print("Each person will pay " + str(forEachPerson) + " dollars.")
    
calculator()