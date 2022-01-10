from datetime import datetime
from datetime import timedelta
import time


class DigitalCounter:
    def __init__(self, current, minimum, maximum):
        self.__set_current_counter(current)
        self.max_counter = maximum
        self.min_counter = minimum

    @property
    def current_counter(self):
        return self.__current_counter

    def __set_current_counter(self, value):
        if not isinstance(value, int):
            raise TypeError('current counter must be of type int')
        self.__current_counter = value

    @property
    def max_counter(self):
        return self.__max_counter

    @max_counter.setter
    def max_counter(self, value):
        if not isinstance(value, int):
            raise TypeError('max_counter must be of type int')
        # if value < self.min_counter:
        #     self.__min_counter = value
        if value < self.current_counter:
            self.__current_counter = self.min_counter
        self.__max_counter = value

    @property
    def min_counter(self):
        return self.__min_counter

    @min_counter.setter
    def min_counter(self, value):
        if not isinstance(value, int):
            raise TypeError('min_counter must be of type int')
        # if value > self.max_counter:
        #     self.__max_counter = value
        if value > self.current_counter:
            self.__current_counter = self.min_counter
        self.__min_counter = value

    def iadd(self, other):
        if not isinstance(other, int):
            raise TypeError('increment must be of type int')
        incremented_counter = self.current_counter + other
        if incremented_counter > self.max_counter or incremented_counter < self.min_counter:
            self.__set_current_counter(self.min_counter)
        return self

    def __isub(self, other):
        if not isinstance(other, int):
            raise TypeError('decrement must be of type int')
        decremented_counter = self.current_counter + other
        if decremented_counter > self.max_counter or decremented_counter < self.min_counter:
            self.__set_current_counter(self.min_counter)
        return self


class Stopwatch(DigitalCounter):
    def __init__(self, current, minimum, maximum):
        super().__init__(current, minimum, maximum)
        self.__started = False
        self.__finished = False
        self.__start = None
        self.__stop = None

    def start(self):
        self.__finished = False
        self.__started = True
        self.__start = datetime.now()

    def stop(self):
        if not self.__started:
            return ValueError('Stopwatch is not started yet')
        self.__finished = True
        self.__started = False
        self.__stop = datetime.now()

    def elapsed_time(self):
        if not self.__finished:
            return ValueError('illegal stopwatch state')
        return self.__stop - self.__start

    def __str__(self):
        return f'Elapsed time = {self.elapsed_time()}'


class RaceResults:
    def __init__(self, *args):
        self.races = list(args)
        self.__iter = None

    @property
    def races(self):
        return self.__races

    @races.setter
    def races(self, races):
        if not isinstance(races, list):
            raise TypeError('races must be of type list')
        if not all(isinstance(race, Stopwatch) for race in races):
            raise TypeError('race must be of type Stopwatch')
        if len(races) == 0:
            raise ValueError('races must not have zero size')
        self.__races = races

    def __iter__(self):
        self.__iter = self.races.__iter__()
        return self.__iter

    def __next__(self):
        self.__iter.__next()

    def min_race_time(self):
        min_time = self.races[0].elapsed_time()
        for race in self:
            if race.elapsed_time() < min_time:
                min_time = race.elapsed_time()
        return min_time

    def max_race_time(self):
        max_time = self.races[0].elapsed_time()
        for race in self:
            if race.elapsed_time() > max_time:
                max_time = race.elapsed_time()
        return max_time

    def results_of_3_winners(self):
        results = list()
        for race in self:
            results.append(race.elapsed_time())
        results.sort(reverse=True)
        if len(results) < 4:
            return results
        else:
            return results[0:3]

    def average_race_time(self):
        results = list()
        for race in self:
            results.append(race.elapsed_time())
        timedelta(seconds=sum(
            map(lambda f: int(f[0]) * 3600 + int(f[1]) * 60 + int(f[2]), map(lambda f: f.split(':'), results))) / len(
            results))


my_stopwatch = Stopwatch(0, 0, 10)
my_stopwatch.start()
time.sleep(2)
my_stopwatch.stop()
print(my_stopwatch.elapsed_time())