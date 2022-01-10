class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if not isinstance(value, int):
            raise TypeError('hours must be of type int')
        if 0 > value > 23:
            raise ValueError('hours must be between 0 and 23')
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if not isinstance(value, int):
            raise TypeError('minutes must be of type int')
        if 0 > value > 59:
            raise ValueError('minutes must be between 0 and 59')
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if not isinstance(value, int):
            raise TypeError('seconds must be of type int')
        if 0 > value > 59:
            raise ValueError('seconds must be between 0 and 59')
        self.__seconds = value

    def get_full_time(self):
        return f'{self.__get_full_hours_str()} {self.__get_minutes_str()} {self.__get_seconds_str()}'

    def get_part_time(self):
        return f'{self.__get_part_hours_str()} {self.__get_minutes_str()} {self.__get_seconds_str()}'

    def __get_minutes_str(self):
        time_str = str()
        residue = self.minutes % 10
        if 10 < self.minutes < 20 or residue not in (1, 2, 3, 4):
            time_str += str(self.minutes) + ' хвилин'
        elif residue == 1:
            time_str += str(self.minutes) + ' хвилина'
        else:
            time_str += str(self.minutes) + ' хвилини'
        return time_str

    def __get_seconds_str(self):
        time_str = str()
        residue = self.seconds % 10
        if 10 < self.seconds < 20 or residue not in (1, 2, 3, 4):
            time_str += str(self.seconds) + ' секунд'
        elif residue == 1:
            time_str += str(self.seconds) + ' секунда'
        else:
            time_str += str(self.seconds) + ' секунди'
        return time_str

    def __get_full_hours_str(self):
        time_str = str()
        residue = self.hours % 10
        if 10 < self.hours < 20 or residue not in (1, 2, 3, 4):
            time_str += str(self.hours) + ' годин'
        elif residue == 1:
            time_str += str(self.hours) + ' година'
        else:
            time_str += str(self.hours) + ' години'
        return time_str

    def __get_part_hours_str(self):
        time_str = str()
        period = self.hours // 12
        if period == 0:
            time_str += str(self.hours) + ' a.m.'
        else:
            time_str += str(self.hours) + ' p.m.'
        return time_str


def main():
    try:
        time = Time(3, 13, 44)
        print(time.get_full_time())
        print(time.get_part_time())

    except Exception as e:
        print(e)


main()
