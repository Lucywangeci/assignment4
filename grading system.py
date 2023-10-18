def calculate_grade(maths, physics, geo, chem):

  if any(x < 0 or x > 100 for x in [maths, physics, geo, chem]):
    return "Unrecognized marks/avg"


  average = (maths + physics + geo + chem) / 4


  if 0 <= average <= 30:
    return "D"
  elif 31 <= average <= 50:
    return "C"
  elif 51 <= average <= 70:
    return "B"
  elif 71 <= average <= 100:
    return "A"



maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
geo = float(input("Enter Geography marks: "))
chem = float(input("Enter Chemistry marks: "))


grade = calculate_grade(maths, physics, geo, chem)
print(f"Average Grade: {grade}")
