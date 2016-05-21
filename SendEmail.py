import smtplib

# author Andy Dao

# Create these global variables
password = ''
subjectTitle = ''
bodyMsg = ''

# Function to grab password, subject title, and body message.
def userInput():
    print('Please enter your password to send the email.')
    global password
    password = input()  # Remember, when using pycharm, add the single quotes for the password.

    print('Enter the subject title.')
    global subjectTitle
    subjectTitle = input()

    print('Enter body message.')
    global bodyMsg
    bodyMsg = input()

# Setup the basic server connection
connectionObj = smtplib.SMTP('smtp.gmail.com', 587)
type(connectionObj)
connectionObj.ehlo()
connectionObj.starttls()

# Call this function to grab the user inputs.
userInput()

# Login
connectionObj.login('andydao10@gmail.com', password)

# Setup the email and send the email with the user input info.
connectionObj.sendmail('andydao10@gmail.com', 'andydao10@gmail.com', 'Subject: ' + subjectTitle + '\n' + bodyMsg)

# Done
print('Message sent')

# Close connection
connectionObj.quit()

