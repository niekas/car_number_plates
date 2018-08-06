from rest_framework import exceptions
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 400:
        if 'owner' in response.data and response.data['owner'][0].code == 'does_not_exist':
            response.data['owner'][0] = exceptions.ErrorDetail(
                'Please choose an owner.',
                code='does_not_exist'
            )
    return response
