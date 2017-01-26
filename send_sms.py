#Udacity - Programming Foundations with Python
#
#Text message are often used in wide variety of applications. Taxi often send their
#customer text message informing passenger the driver's location. Gmail use
#security code via text messages. Shopping sites use text message for daily deals.
# 
# Use Python code to send sms text messages. Set up Twilio and use the sample code
# Twilio offered.


from twilio.rest import TwilioRestClient
# twilio installtion note:
#1. Check that there is a path to python.exe
#2. command prompt: easy_install twilio or pip install twilio

account_sid = "ACcc8e21854a9b51eb001d02f586380edf" # Your Account SID from www.twilio.com/console
auth_token  = "f974cd1213416b758993e8b4278xxxxx"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+16785592333",    # Replace with your phone number
    from_="+14708655743") # Replace with your Twilio number

print(message.sid)
