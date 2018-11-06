# Shinya Aoi
# CSS 340
# 10/12/2018

# This class is to make a time span including all the comparison operators
# and the string method(overloading).
class TimeSpan:

    def __init__(self, seconds = 0.0, minutes = 0.0, hours = 0.0):
        self.setTime(seconds, minutes, hours)

    def getHours(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    def setTime(self, seconds, minutes, hours):
        allSeconds = seconds + minutes * 60 + hours * 3600
        self.__hours = int(allSeconds / 3600)
        allSeconds = allSeconds - (self.__hours * 3600)
        self.__minutes = int(allSeconds / 60)
        allSeconds = allSeconds - (self.__minutes * 60)
        self.__seconds = allSeconds


    def __add__(self, other):
        temp = TimeSpan()
        temp.setTime(self.__seconds + other.getSeconds(),
                     self.__minutes + other.getMinutes(), self.__hours + other.getHours())
        return temp

    def __sub__(self, other):
        temp = TimeSpan()
        temp.setTime(self.__seconds - other.getSeconds(),
                     self.__minutes - other.getMinutes(), self.__hours - other.getHours())
        return temp

    def __neg__(self):
        return TimeSpan(-self.__seconds, -self.__minutes, -self.__hours)

    def __eq__(self, other):
        if self.__seconds != other.getSeconds():
            return False
        elif self.__minutes != other.getMinutes():
            return False
        elif self.__hours != other.getHours():
            return False
        else:
            return True

    def __ne__(self, other):
        if self.__seconds != other.getSeconds():
            return True
        elif self.__minutes != other.getMinutes():
            return True
        elif self.__hours != other.getHours():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__hours < other.getHours():
            return True
        if self.__minutes < other.getMinutes():
            return True
        if self.__seconds < other.getSeconds():
            return True
        else:
            return False

    def __le__(self, other):
        if self.__hours <= other.getHours():
            return True
        if self.__minutes <= other.getMinutes():
            return True
        if self.__seconds <= other.getSeconds():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__hours > other.getHours():
            return True
        if self.__minutes > other.getMinutes():
            return True
        if self.__seconds > other.getSeconds():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__hours >= other.getHours():
            return True
        if self.__minutes >= other.getMinutes():
            return True
        if self.__seconds >= other.getSeconds():
            return True
        else:
            return False

    def __str__(self):
        return str("Hours:" + str(self.__hours) + ", Minutes:" +
                   str(self.__minutes) + ", Seconds:" + str(self.__seconds))
