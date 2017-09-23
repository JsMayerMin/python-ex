#send text msg from python
#twilio external python package


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1e6f923caf5131dc734b677607dac32e"
# Your Auth Token from twilio.com/console
auth_token  = "0d5703ca534e20dbb3298519893da885"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+821096295855",
    from_="+19715448223",
    body="Hello from Python!")

print(message.sid)