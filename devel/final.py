#Joshua McKnight

#Email List Collection Program 


import os
#import docx

#username = ''
#useremail = ''


def emailtxtlist(username, useremail):

   emailList = open('emails.txt', 'w')
   emailList.write('NAME: ' + username + ', EMAIL: ' + useremail + '\n')
   emailList.close()


#def emaildoclist(username, useremail):

   #emaildoc = docx.Document()
   #emaildoc.add_paragraph('NAME: ' + username + ', EMAIL: ' + useremail)
   #emaildoc.save('emails.docx')


print('~HUGS EMAIL NEWSLETTER SIGNUP~\n')
print('\nPlease enter your name: \n')
username = input()
print('Please enter your email: \n')
useremail = input()

emailtxtlist(username, useremail)
#emaildoclist(username, useremail)
