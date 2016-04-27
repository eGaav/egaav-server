from protorpc import messages


class Class(messages.Enum):
    """
    Class of student
    """
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12
    GRADUATE = 15
    POST_GRADUATE = 18
    PHD = 23


class EduBoard(messages.Enum):
    ALLABHAD = 1
    CBSE = 2
    ICSE = 3
    OTHER = 4


class Gender(messages.Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
