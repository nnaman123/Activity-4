#take marks input from user
print("Enter the marks obtained in 4 subjects: ")
math = int(input("Enter the marks obtained in Math: "))
science = int(input("Enter the marks obtained in Science: "))
english = int(input("Enter the marks obtained in English: "))
social_studies = int(input("Enter the marks obtained in Social Studies: "))

#Calculating total marks and percentage

total_marks = math + science + english + social_studies
percentage = (total_marks / 400) * 100

print("Total Marks:", total_marks)
print("Percentage:", percentage)