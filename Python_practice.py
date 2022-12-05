print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[2] != "Denver":
    print("Nope!")

temperature = int(input("What's the current temperature? "))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows")

#What is the score?
score = int(input("What's your score? "))

#Determine the grade 
if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")

counties2 = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list")
else:
    print("Not in the list")







