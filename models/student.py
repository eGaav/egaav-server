from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from enums.enum import Class, EduBoard, Gender


class Student(ndb.Model):
    name = ndb.StringProperty()
    mobile = ndb.StringProperty()
    email = ndb.StringProperty()
    id = ndb.StringProperty()
    address = ndb.StringProperty()
    stu_class = msgprop.EnumProperty(Class)
    board = msgprop.EnumProperty(EduBoard)
    gender = msgprop.EnumProperty(Gender)
    add_date = ndb.DateTimeProperty(auto_now_add=True)
