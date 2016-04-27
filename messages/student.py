import endpoints
from protorpc import message_types
from protorpc import messages

from enums.enum import Class, EduBoard, Gender


class StudentResp(messages.Message):
    """
    Student request and response format.
    """
    name = messages.StringField(1, required=True)
    mobile = messages.StringField(2, required=True)
    email = messages.StringField(3, required=False, default='')
    id = messages.StringField(4, default='')
    address = messages.StringField(5, default='')
    stu_class = messages.EnumField(Class, 6)
    board = messages.EnumField(EduBoard, 7)
    gender = messages.EnumField(Gender, 8)
    add_date = messages.StringField(9)


class StudentList(messages.Message):
    """
    Student list response format
    """
    list = messages.MessageField(StudentResp, 1, repeated=True)


CONTAINER = endpoints.ResourceContainer(message_types.VoidMessage,
                                        name=messages.StringField(1, required=True),
                                        mobile=messages.StringField(2, required=True),
                                        email=messages.StringField(3, required=False, default=None),
                                        id=messages.StringField(4, required=False, default=None),
                                        address=messages.StringField(5, required=False, default=''),
                                        stu_class=messages.EnumField(Class, 6, required=True),
                                        board=messages.EnumField(EduBoard, 7, required=True),
                                        gender=messages.EnumField(Gender, 8, required=True)
                                        )
