def is_right_angled(s1, s2, s3):
    sides = sorted([s1, s2, s3])
    return (sides[0]**2 + sides[1]**2) == sides[2]**2

try:
    side1 = int(input("Enter integer length of side 1: "))
    side2 = int(input("Enter integer length of side 2: "))
    side3 = int(input("Enter integer length of side 3: "))

    if is_right_angled(side1, side2, side3):
        print("Yes, it is a right-angled triangle. 📐")
    else:
        print("No, it is not a right-angled triangle.")
        
except ValueError:
    print("Please enter valid integers only.")
