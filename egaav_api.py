"""
e-gaav application endpoint apis.
"""
import endpoints
import logging
from protorpc import messages
from protorpc import message_types
from protorpc import remote

WEB_CLIENT_ID = '18828650114-l608lhf4u73vom61osuegkof9sgkt4uf.apps.googleusercontent.com'
ANDROID_CLIENT_ID = 'replace this with your Android client ID'
IOS_CLIENT_ID = 'replace this with your iOS client ID'
ANDROID_AUDIENCE = WEB_CLIENT_ID

package = 'Egaav'


class Greeting(messages.Message):
    """Greeting that stores a message."""
    message = messages.StringField(1)


class GreetingCollection(messages.Message):
    """Collection of Greetings."""
    items = messages.MessageField(Greeting, 1, repeated=True)


STORED_GREETINGS = GreetingCollection(items=[
    Greeting(message='hello world!'),
    Greeting(message='goodbye world!'),
])


# E-Gaav api
@endpoints.api(name='egaav', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID],
               audiences=[ANDROID_AUDIENCE],
               scopes=[endpoints.EMAIL_SCOPE])
class Egaav(remote.Service):
    @endpoints.method(message_types.VoidMessage, GreetingCollection, name='admin.student_list', path='students',
                      http_method='GET')
    def student_list(self, request):
        current_user = endpoints.get_current_user()
        logging.info('Email=' + current_user.email())
        """
        Api return all list of students.

        Access: only for admin.

        :param request: htttp request
        :return:
        """
        return STORED_GREETINGS


api = endpoints.api_server([Egaav])
