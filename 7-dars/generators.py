# def square_nums(nums):
#     for i in nums:
#         yield i*i
    

# my_list = square_nums([2,4,5,7,9])

# my_list2 = range(0,7)

# for i in my_list2:
#     print(i)


# my_list = (x*x for x in [2,4,6,7,8,9])
# print(my_list)

# import random
# import time


# names = ['Murodjon', 'Boburjon', 'Ikromjon', 'Abdulbosid', 'Javohir']
# majors = ['Math', 'IT', 'History', 'Geography', 'English', 'Russian']

# def person_list(people_num):
#     result = []
#     for i in range(people_num):
#         person = {
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)
#         }
#         result.append(person)
    
#     return result

# def person_generator(people_num):
#     for i in range(people_num):
#         person = {
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)
#         }
#         yield person
    


# time1 = time.time()
# people_list = person_list(1000000)
# time2 = time.time()

# time1 = time.time()
# people_list = person_generator(1000000)
# time2 = time.time()

# for i in person_generator(10):
#     print(i)

# print(people_list)

# print("Funksiya ishlash tezligi {} seconds ".format(time2-time1))


# def square(num):
#     return num%2==0


# result = filter(square, [4,5,6,8])

# for i in result:
#     print(i)






































