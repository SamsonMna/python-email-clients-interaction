from twilio.rest import TwilioRestClient
accountSID = 'AcXXXXXXXXXXXXXXXXXX'
authToken = 'XXXXXXXXXXXXXXXXXXXXX'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = 'the disgnated twilio number'
myCellPhone = input("Enter your number provided by twilio ")
message = twilioCli.messages.create(body='Write your message here.', from_=myTwilioNumber, to=myCellPhone)

# Checking for different message instances
message.to # Checks the number the message was sent to
message.from # checks the number the message was sent from
message.body # confirms the message sent
message.status # checks the status of the message on whether it has been sent, waiting to be sent or it has been delivered.
message.date_created # Checks the date the message was created
message.date_sent == None #

