studentCount = int(input("Enter No.of Students: "))  # Asking the User to provide count of students
studentHeightsInFeet = []
studentHeightsInCM = []
for i in range(studentCount):
    height = float(input("Enter the Student-{} height in Feet ".format(i)))  # Accepting Height of the each student
    # from user and converting into Float
    studentHeightsInFeet.append(float("{:.1f}".format(height)))  # adding height of student to list and converting to
    # 1 decimal float format
    studentHeightsInCM.append(float("{:.1f}".format(height * 30.48)))  # adding height of student to list after
    # converting it to Centimeter and converting to 1 decimal float format

print("Student's Height in Feet", studentHeightsInFeet)  # printing student height in feet metric
print("Student's Height in centimeter", studentHeightsInCM)  # printing student height in Centimeter metric
