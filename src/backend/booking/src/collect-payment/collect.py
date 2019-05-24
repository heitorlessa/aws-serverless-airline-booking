from botocore.vendored import requests
import os

def lambda_handler(event, context):
    paymentApiResponse = requests.post(os.environ['PAYMENT_API_URL'], json = { "chargeId":event["chargeId"]})
    print(paymentApiResponse.content)

    if paymentApiResponse.status_code == 200:
        return { 
            'status' : 'success'
        }
    raise PaymentException('Payment failed', paymentApiResponse.status_code)

class PaymentException(Exception):
    def __init__(self, message, status_code):

        # Call the base class constructor with the parameters it needs
        super(PaymentException, self).__init__(message)

        # Now for your custom code...
        self.status_code = status_code