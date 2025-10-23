#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days
CP = input("Please input the current population")
R = input ("Please input the rate in a decimal")
D = input ("Please input the number of days")
Y = input ("Please input the number of days in a year")
Y = int(Y)
Y = 365
D = int(D)
D = D/Y
R = float(R)
CP = int(CP)
FP = (CP) * (1+R) ** (D)
FP = int(FP)
answer = FP
print (answer)