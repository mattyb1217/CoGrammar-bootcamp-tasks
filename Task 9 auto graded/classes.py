class email():
    def __init__(self, email_address, subject_line,email_content):
        self.email = email_address
        self.subject = subject_line
        self.content= email_content


email1= email("123@hotmail.com", "Football game", "When does the football game start tonight?")
email2= email("345@yahoo.com", "Ideas for dinner", "Do you have any ideas for tonights dinnner?")
email3= email("567@gmail.com", "Concert choices", "Who are we next seeing in concert")

print(email1.email )                # after the "." put the function with the self e.g self.email is just email
print(email2.subject)

#has_been_read= email(False)
#mark_as_read= has_been_read(True)

inbox= [email1.content, email2.content, email3.content]
print(inbox)

def populate_inbox():
    email1= email("123@hotmail.com", "Football game", "When does the football game start tonight?")
email2= email("345@yahoo.com", "Ideas for dinner", "Do you have any ideas for tonights dinnner?")
email3= email("567@gmail.com", "Concert choices", "Who are we next seeing in concert")


def list_emails():
    email1.subject
    email2.subject
    email3.subject

#print(list_emails)

def read_email(index):
    no= input("choose an email: ")
    print(no)

menu=True
while True:
    user_option= int(input(""" what would you like to do:
        1. Read emails
        2. View unread
        3. Quit application
                           enter choice: """))
    
    if user_option ==1:
        print(email1.content)
    elif user_option==2:
        print ("you have no unread")#
    elif user_option==

    else: print("wrong input")

