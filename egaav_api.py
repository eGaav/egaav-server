"""
e-gaav application endpoint apis.
"""
import endpoints
import logging
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from messages import student
from models.student import Student as m_student

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
               scopes=[endpoints.EMAIL_SCOPE],
               description='egaav google end point apis',
               auth_level=endpoints.AUTH_LEVEL.REQUIRED,
               title="egaav api")
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

    @endpoints.method(student.CONTAINER, student.StudentResp, name='public.student_add', path='students',
                      http_method='POST')
    def student_add(self, request):
        stu = student.StudentResp()
        stu.name = request.name
        stu.mobile = request.mobile
        stu.email = request.email
        stu.address = request.address
        stu.board = request.board
        stu.id = request.id
        stu.stu_class = request.stu_class
        stu.gender = request.gender
        db_stu = m_student()
        db_stu.name = stu.name
        db_stu.mobile = stu.mobile
        db_stu.email = stu.email
        db_stu.address = stu.address
        db_stu.board = stu.board
        db_stu.id = stu.id
        db_stu.stu_class = stu.stu_class
        db_stu.gender = stu.gender
        db_stu.put()
        return stu


api = endpoints.api_server([Egaav])
