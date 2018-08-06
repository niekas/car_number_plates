from rest_framework import exceptions
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 400:
        if 'owner_id' in response.data and response.data['owner_id'][0].code == 'does_not_exist':
            response.data['owner_id'][0] = exceptions.ErrorDetail(
                'Please choose an owner.',
                code='does_not_exist'
            )
        if 'number' in response.data and response.data['number'][0].code == 'unique':
            response.data['number'][0] = exceptions.ErrorDetail(
                'This number plate already exists, please choose a different one.',
                code='unique'
            )
    return response
