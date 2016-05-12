
# hi. This is a little program

################################################################################
# calculate overtime hours.  Takes a parameter for the total number of hours worked
# and return hours above 40.
# returns 0 if worked 40 or less hours.
################################################################################
def calcOverTimeHours(hours ):
    otHours = hours - 40
    if ( otHours>0):
        return otHours
    else:
        return 0

################################################################################
# calculate regular pay rate  hours.  Takes a parameter for the total number of hours worked
# and return 40 if hours is greater than 40
# returns hours if hours is less than or equal to 40.
# 
################################################################################
def calcRegularHours(hours):
    if ( hours>=40):
        return 40
    else:
        return hours

################################################################################
#
################################################################################
def calcTotalPay(basePayHours, hourlyRate, overTimePayHours, overTimeRate):
    totalPay = (basePayHours * hourlyRate) + (overTimePayHours * hourlyRate * overTimeRate )
    return totalPay

################################################################################
#
################################################################################
def getValueUserPrompt( whichPrompt ):
    retPrompt = "nothing"

    if ( whichPrompt == "AskRate"):
        return input("Please enter you Hourly rate= ")
    elif ( whichPrompt =="AskHours"):
        return input("Please enter total number of hours= ")
        
################################################################################
#
################################################################################
def main():
    overTimeRate = 1.5                                                  # Set overtime rate to 1.5/ Time and a half.
    continueLoop = "1"                                                  # initialize loop flag to 1. continue loping.
    while continueLoop == "1" :
        hourlyRate =  getValueUserPrompt("AskRate")
        try:
            hourlyRate = float(hourlyRate)				    # convert to a number just in case.
        except:
             print("Invalid input. Use only numbers. Please try again.")
             
        hoursWorked = getValueUserPrompt("AskHours")
        try:
            hoursWorked = float(hoursWorked)				    # convert to a number just in case.
        except:
             print("Invalid input. Use only numbers. Please try again.")        
 
        print ("Total Pay = ", calcTotalPay( calcRegularHours(hoursWorked), hourlyRate, calcOverTimeHours( hoursWorked ), overTimeRate))
        continueLoop = input("Press 1 to run again")
    else :
        print("Thank you .  Bye.")
################################################################################
#
################################################################################
main()
