# fruits = ["Apple", "Peach", "Pineapple", "Orange", "Pear"]
# for f in fruits:
#     print (f)
#     print(f + "salad")


# height = input("Please list student heights \n")
# student_heights = height.split(",")
# print(student_heights)
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
# total_height = 0
# for h in student_heights:
#     total_height += h
# print(f"The total height is {total_height}")

# # number_of_students = 0
# # for s in student_heights:
# #     number_of_students += 1
# number_of_students = len(student_heights)
# print(f"The number of students is: {number_of_students}")

# average_height = round(total_height/ number_of_students)

# print(f"The average height of the students is {average_height}")
    
    
# student = input("Please input student scores, separating them using a comma. \n")
# student_scores = student.split(",")
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])


# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
            
# print(f"The highest test score is {highest_score}.")

# test_scores = input("Please input student test scores, separating them with a comma. \n")
# student_scores = test_scores.split(",")
# for num in range(0, len(student_scores)):
#     student_scores[num]= int(student_scores[num])
    
# highest_test_score = 0
# for score in student_scores:
#     if score > highest_test_score:
#         highest_test_score = score
# print(f"The highest test score is {highest_test_score}")
        
#For loop w Range
# for number in range(1,10):
#     print(number)

# total = 0
# for number in range(1,101):
#     total += number
# print(total)

# target = int(input()) 
# even_sum = 0
# for n in range(0,target + 1, 2):
#   even_sum += n
# print(even_sum)

# write a program to recreate the fizzbuzz game
# target = 100
# for n in range(0, target +1):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else: 
#         print(n)

#While loops - while something is true, do something repeatedly

number = 6
while number > 0:
    print(number)
    number -= 1
