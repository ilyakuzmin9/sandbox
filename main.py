# import re
#
# to_sec = 24*60*60
#
#
# # tf = re.search('WCL_Триколор', 'WCL_Триколор')
# # l = tf.re.groupindex
# # print(tf)
#
# print("tr"+str(50)+"dfd")

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)


for number in range(1,101):
    if number % 3 == 0:
        if number % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)






