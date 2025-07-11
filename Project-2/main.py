#taking total amount as input from the user
total_amount = int(input("Enter the total amount to Withraw: "))

#Calculating the number of notes of different denominations
notes_500 = total_amount // 500
notes_200 = (total_amount % 500) // 200
notes_100 = (total_amount % 200) // 100
notes_50 = (total_amount % 100) // 50
notes_20 = (total_amount % 50) // 20
notes_10 = (total_amount % 20) // 10
notes_5 = (total_amount % 10) // 5
notes_1 = total_amount % 5

\


print("Number of 500 notes:", notes_500)
print("Number of 200 notes:", notes_200)
print("Number of 100 notes:", notes_100)
print("Number of 50 notes:", notes_50)
print("Number of 20 notes:", notes_20)
print("Number of 10 notes:", notes_10)
print("Number of 5 notes:", notes_5)
print("Number of 1 notes:", notes_1)