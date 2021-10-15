# Create a class with 3 fields
class Attendance:
    Present = 0
    Absent = 0
    Released = 0

# creating list of students where we will put data later on
students = []

# Import data 
f = open("attendance.txt")
records = f.read().split("\n")
f.close()

# read data into list 
for rec in records:
    cols = rec.split(" ")
    s = Attendance()
    s.Present = int(cols[0])
    s.Absent = int(cols[1])
    s.Released = int(cols[2])
    
    students.append(s)

# Function for Attendance Alert Days 
def Rule(students):
    countmin = 0
    minRate = float(input("Min. Attendance Rule: "))
    
    for s in students:
        if s.Present / (s.Present + s.Absent + s.Released) < minRate:
            countmin += 1
    return countmin

# Function to calculate average enrollment (choice 2)
def Tavg(students):
    count = 0
    for s in students:
        count += (s.Present + s.Absent + s.Released) / len(students)
    return count

# Function to calculate average released students (choice 3)
def ReleasedAvg(students):
    amount = 0
    count = 0
    
    for s in students:
        if s.Released > 0:
            amount += s.Released
            count += 1
    avgg = amount / count
    
    return avgg


while True:
    print("Attendance Analysis")
    print("===================")
    print("1- Attendance Alert Days")
    print("2- Avg. Engrollment")
    print("3- Release Days")
    print("0- Exit ")
    choice = int(input("? "))
    if choice == 0:
        break
    
    if choice == 1:
        miin = Rule(students)
        print("The rule has been violated for ", miin, " days.")
        
    
    if choice == 2:
        c = Tavg(students)
        print("Avg. Enrollment is ", c)
    
    if choice == 3:
        ra = ReleasedAvg(students)
        print("On avg. ", ra, "students were released for 3 days.")
        
