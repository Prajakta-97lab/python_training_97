'''
Accept average score from the student of his exam and print his result as follows:
0 to 49 is fail
58 to 74 is second class
75 to 90 is first class
91 to 100 is distinction 
Also chcek for invalid score


'''

student_score = int(input('Enter the marks of student:'))
 
if 0<student_score<49 :
    print('FAIL')
elif 58<student_score<74:
    print('SECOND CLASS')
elif 75<student_score<90:
    print("FIRST CLASS")
elif 91<student_score<100:
    print("DISTINCTION")
else:
    print("invalid score")

