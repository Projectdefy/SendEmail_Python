import smtplib

# author Andy Dao

# Create these global variables
username = ''
password = ''
subjectTitle = ''
bodyMsg = ''
recipient = ''

# Function to grab password, subject title, and body message.
def userInput():
    print('Please enter your email address.')
    global username
    username = input()

    print('Please enter your password to send the email.')
    global password
    password = input()

    print('Enter the subject title.')
    global subjectTitle
    subjectTitle = input()

    print('Enter body message.')
    global bodyMsg
    bodyMsg = input()

    print('Who do you wish to send the email to?')
    global recipient
    recipient = input()

# Setup the basic server connection
connectionObj = smtplib.SMTP('smtp.gmail.com', 587)
type(connectionObj)
connectionObj.ehlo()
connectionObj.starttls()

# Call this function to grab the user inputs.
userInput()

# Login
connectionObj.login(username, password)

# Setup the email and send the email with the user input info.
connectionObj.sendmail(username, recipient, 'Subject: ' + subjectTitle + '\n' + bodyMsg)

# Done
print('Message sent')

# Close connection
connectionObj.quit()

