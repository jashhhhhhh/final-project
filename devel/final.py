#Joshua McKnight

#Email List Collection Program 

import re
import os
#import docx

#username = ''
#useremail = ''

emailRegex = re.compile(r'''([a-zA-Z0-9._%+-] + @ [a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)




def emailtxtlist(username, useremail):

   emailList = open('emails.txt', 'w')
   emailList.write('NAME: ' + username + ', EMAIL: ' + useremail + '\n')
   emailList.close()


#def emaildoclist(username, useremail):

   #emaildoc = docx.Document()
   #emaildoc.add_paragraph('NAME: ' + username + ', EMAIL: ' + useremail)
   #emaildoc.save('emails.docx')

def userinput():
   print('~HUGS EMAIL NEWSLETTER SIGNUP~')
   print('------------------------------\n')
   print('\nPlease enter your name:')
   username = input()
   print('\nPlease enter your email:')
   useremail = input()
   if not emailRegex.match(useremail):
      print('Not a valid email address. Please restart program and try again')
   else:
      emailtxtlist(username, useremail)
      #emaildoclist(username, useremail)


userinput()

