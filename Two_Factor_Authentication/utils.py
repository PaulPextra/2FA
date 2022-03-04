from twilio.rest import Client
from environ import Env

env = Env()
env.read_env()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_sms(user_code, phone_number):
    account_sid = env.str('TWILIO_ACCOUNT_SID')
    auth_token = env.str('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body= f'Hi! Your user and verification code is {user_code}',
                                from_=env.str('TWILIO_NUMBER'),
                                to= f'{phone_number}'
                            )
    print(message.sid)