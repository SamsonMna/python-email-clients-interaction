import imapclient
imapObj = imapclient.IMAPClientI('imap.gmail.com', ssl=True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_KEY')
import pprint
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(["SINCE date xyz.."])
UIDs
rawMessages = imapObj.fetch([UIDs[0], ['BODY[]', 'FLAGS']])
pprint.pprint(rawMessage) # marks the email as read
import pyzmail
message = pyzmail.pyzMessage.Factory(rawMessage[UIDs[0]['BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc') # If any
message.get_addresses('bcc') # if any
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None # If any html pages sent to you.
message.html_part.get_payload().decode(message.html_part.charset)
impaObj.logout() # Terminate session interaction

# Say we want to delete a message
imapObj.delete_messages(UIDs[1])
imapObj.expunge()


