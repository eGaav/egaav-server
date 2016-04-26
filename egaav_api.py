"""
e-gaav application endpoint apis.
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

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
@endpoints.api(name='egaav', version='v1')
class Egaav(remote.Service):
    @endpoints.method(message_types.VoidMessage, GreetingCollection, name='admin.student_list', path='students',
                      http_method='GET')
    def student_list(self, request):
        """
        Api return all list of students.

        Access: only for admin.

        :param request: htttp request
        :return:
        """
        return STORED_GREETINGS


api = endpoints.api_server([Egaav])
