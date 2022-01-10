from Student import Student
from Group import Group


def main():
    try:
        student1 = Student('Іван', 'Власюк', {'мат': 100, 'англ': 85, 'фп': 90})
        student2 = Student('Ліза', 'Гончарова', {'мат': 99, 'англ': 99, 'фп': 99})
        student3 = Student('Максим', 'Груздов', {'мат': 100, 'англ': 90, 'фп': 80})
        student4 = Student('Олексій', 'Дудкін', {'мат': 100, 'англ': 100, 'фп': 80})
        student5 = Student('Олексій', 'Занченко', {'мат': 85, 'англ': 90, 'фп': 100})
        student6 = Student('Євгеній', 'Захарчук', {'мат': 100, 'англ': 85, 'фп': 100})
        student7 = Student('Анна', 'Котова', {'мат': 90, 'англ': 100, 'фп': 90})
        student8 = Student('Дарія', 'Кравченко', {'мат': 70, 'англ': 90, 'фп': 90})
        student9 = Student('Сергій', 'Кубрак', {'мат': 100, 'англ': 70, 'фп': 70})
        student10 = Student('Тетяна', 'Кушнірук', {'мат': 100, 'англ': 100, 'фп': 100})
        student11 = Student('Михайло', 'Лагойда', {'мат': 100, 'англ': 100, 'фп': 100})
        student12 = Student('Святослав', 'Луговий', {'мат': 100, 'англ': 60, 'фп': 70})
        # student13 = Student('Юля', 'Мангуплі', {'мат': 80, 'англ': 80, 'фп': 70})
        # student14 = Student('Кіріл', 'Марченко', {'мат': 70, 'англ': 90, 'фп': 90})
        # student15 = Student('Іван', 'Міньков', {'мат': 70, 'англ': 90, 'фп': 100})
        # student16 = Student('Влад', 'Мітлицький', {'мат': 100, 'англ': 80, 'фп': 100})
        # student17 = Student('Олег', 'Моругий', {'мат': 100, 'англ': 80, 'фп': 100})
        # student18 = Student('Максим', 'Мосолов', {'мат': 70, 'англ': 70, 'фп': 70})
        # student19 = Student('Артур', 'Сарахман', {'мат': 100, 'англ': 100, 'фп': 100})
        # student20 = Student('Анна', 'Сідорська', {'мат': 80, 'англ': 100, 'фп': 100})
        # student21 = Student('Кирило', 'Сокирка', {'мат': 95, 'англ': 100, 'фп': 95})
        # student22 = Student('Єгор', 'Согулов', {'мат': 95, 'англ': 95, 'фп': 95})
        # student23 = Student('Дмитро', 'Філюк', {'мат': 80, 'англ': 100, 'фп': 90})
        # student24 = Student('Сергій', 'Чукін', {'мат': 100, 'англ': 80, 'фп': 90})
        # student25 = Student('Богдан', 'Чуй', {'мат': 95, 'англ': 95, 'фп': 100})

        ti_02 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                      student10, student11, student12)
        print('Group after creating', ti_02, sep='\n')
        ti_02.add(student8)
        ti_02.add(student9)
        print('Group after addition new two students', ti_02, sep='\n')
        print('Highest average score for 5 students', ti_02.top_five_students(), sep='\n')
        ti_02.delete(student8)
        print('Group after removal of the Oleg', ti_02, sep='\n')
        ti_02.add(student1)
    except Exception as e:
        print(e)


def get_list_ti02():
    try:
        student1 = Student('Іван', 'Власюк', {'мат': 100, 'англ': 85, 'фп': 90})
        student2 = Student('Ліза', 'Гончарова', {'мат': 99, 'англ': 99, 'фп': 99})
        student3 = Student('Максим', 'Груздов', {'мат': 100, 'англ': 90, 'фп': 80})
        student4 = Student('Олексій', 'Дудкін', {'мат': 100, 'англ': 100, 'фп': 80})
        student5 = Student('Олексій', 'Занченко', {'мат': 85, 'англ': 90, 'фп': 100})
        student6 = Student('Євгеній', 'Захарчук', {'мат': 100, 'англ': 85, 'фп': 100})
        student7 = Student('Анна', 'Котова', {'мат': 90, 'англ': 100, 'фп': 90})
        student8 = Student('Дарія', 'Кравченко', {'мат': 70, 'англ': 90, 'фп': 90})
        student9 = Student('Сергій', 'Кубрак', {'мат': 100, 'англ': 70, 'фп': 70})
        student10 = Student('Тетяна', 'Кушнірук', {'мат': 100, 'англ': 100, 'фп': 100})
        student11 = Student('Михайло', 'Лагойда', {'мат': 100, 'англ': 100, 'фп': 100})
        student12 = Student('Святослав', 'Луговий', {'мат': 100, 'англ': 60, 'фп': 70})
        # student13 = Student('Юля', 'Мангуплі', {'мат': 80, 'англ': 80, 'фп': 70})
        # student14 = Student('Кіріл', 'Марченко', {'мат': 70, 'англ': 90, 'фп': 90})
        # student15 = Student('Іван', 'Міньков', {'мат': 70, 'англ': 90, 'фп': 100})
        # student16 = Student('Влад', 'Мітлицький', {'мат': 100, 'англ': 80, 'фп': 100})
        # student17 = Student('Олег', 'Моругий', {'мат': 100, 'англ': 80, 'фп': 100})
        # student18 = Student('Максим', 'Мосолов', {'мат': 70, 'англ': 70, 'фп': 70})
        # student19 = Student('Артур', 'Сарахман', {'мат': 100, 'англ': 100, 'фп': 100})
        # student20 = Student('Анна', 'Сідорська', {'мат': 80, 'англ': 100, 'фп': 100})
        # student21 = Student('Кирило', 'Сокирка', {'мат': 95, 'англ': 100, 'фп': 95})
        # student22 = Student('Єгор', 'Согулов', {'мат': 95, 'англ': 95, 'фп': 95})
        # student23 = Student('Дмитро', 'Філюк', {'мат': 80, 'англ': 100, 'фп': 90})
        # student24 = Student('Сергій', 'Чукін', {'мат': 100, 'англ': 80, 'фп': 90})
        # student25 = Student('Богдан', 'Чуй', {'мат': 95, 'англ': 95, 'фп': 100})

        ti_02 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                      student10, student11, student12)
        return ti_02
    except Exception as e:
        print(e)


def get_list_ti01():
    try:
        student1 = Student('Саня', 'Ткаченко', {'мат': 100, 'англ': 85, 'фп': 90})
        student2 = Student('Даня', 'Петраченко', {'мат': 99, 'англ': 99, 'фп': 99})
        student3 = Student('Максим', 'Гарманенко', {'мат': 100, 'англ': 90, 'фп': 80})
        student4 = Student('Олекса', 'Гарбаж', {'мат': 100, 'англ': 100, 'фп': 80})
        student5 = Student('Степан', 'Зінченко', {'мат': 85, 'англ': 90, 'фп': 100})
        student6 = Student('Саня', 'Санович', {'мат': 100, 'англ': 85, 'фп': 100})
        student7 = Student('Тіна', 'Костаренко', {'мат': 90, 'англ': 100, 'фп': 90})
        student8 = Student('Катерина', 'Свербигова', {'мат': 70, 'англ': 90, 'фп': 90})
        student9 = Student('Сергій', 'Рвихвіст', {'мат': 100, 'англ': 70, 'фп': 70})
        student10 = Student('Стьопа', 'Костел', {'мат': 100, 'англ': 100, 'фп': 100})
        student11 = Student('Михайло', 'Лагідний', {'мат': 100, 'англ': 100, 'фп': 100})
        student12 = Student('Ілля', 'Саймоненко', {'мат': 100, 'англ': 60, 'фп': 70})
        # student13 = Student('Агата', 'Степаненко', {'мат': 80, 'англ': 80, 'фп': 70})
        # student14 = Student('Кіріл', 'Береговський', {'мат': 70, 'англ': 90, 'фп': 90})
        # student15 = Student('Іван', 'Спільний', {'мат': 70, 'англ': 90, 'фп': 100})
        # student16 = Student('Сніжана', 'Габенко', {'мат': 100, 'англ': 80, 'фп': 100})
        # student17 = Student('Остап', 'Трусенко', {'мат': 100, 'англ': 80, 'фп': 100})
        # student18 = Student('Максим', 'Остапенко', {'мат': 70, 'англ': 70, 'фп': 70})
        # student19 = Student('Павло', 'Саранченко', {'мат': 100, 'англ': 100, 'фп': 100})
        # student20 = Student('Денчик', 'Мовчанюк', {'мат': 80, 'англ': 100, 'фп': 100})
        # student21 = Student('Кирило', 'Мовчаненко', {'мат': 95, 'англ': 100, 'фп': 95})
        # student22 = Student('Женик', 'Каленик', {'мат': 95, 'англ': 95, 'фп': 95})
        # student23 = Student('Роман', 'Ліфвантій', {'мат': 80, 'англ': 100, 'фп': 90})
        # student24 = Student('Євген', 'Галич', {'мат': 100, 'англ': 80, 'фп': 90})
        # student25 = Student('Жека', 'Бурбело', {'мат': 95, 'англ': 95, 'фп': 100})

        ti_01 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                      student10, student11, student12)
        return ti_01
    except Exception as e:
        print(e)


def get_list_tv_01():
    try:
        student1 = Student('Орест', 'Тойвович', {'мат': 100, 'англ': 85, 'фп': 90})
        student2 = Student('Ксюша', 'Бездоганна', {'мат': 99, 'англ': 99, 'фп': 99})
        student3 = Student('Санчоус', 'Спільний', {'мат': 100, 'англ': 90, 'фп': 80})
        student4 = Student('Остап', 'Ковальський', {'мат': 100, 'англ': 100, 'фп': 80})
        student5 = Student('Ілля', 'Рудий', {'мат': 85, 'англ': 90, 'фп': 100})
        student6 = Student('Євгенія', 'Бороденко', {'мат': 100, 'англ': 85, 'фп': 100})
        student7 = Student('Анна', 'Марієнко', {'мат': 90, 'англ': 100, 'фп': 90})
        student8 = Student('Данил', 'Креніда', {'мат': 70, 'англ': 90, 'фп': 90})
        student9 = Student('Серж', 'Свійвович', {'мат': 100, 'англ': 70, 'фп': 70})
        student10 = Student('Сніжана', 'Кук', {'мат': 100, 'англ': 100, 'фп': 100})
        student11 = Student('Михайло', 'Дагойда', {'мат': 100, 'англ': 100, 'фп': 100})
        student12 = Student('Аміна', 'Шимко', {'мат': 100, 'англ': 60, 'фп': 70})
        # student13 = Student('Оксана', 'Брай', {'мат': 80, 'англ': 80, 'фп': 70})
        # student14 = Student('Костя', 'Дзю', {'мат': 70, 'англ': 90, 'фп': 90})
        # student15 = Student('Василій', 'Ломаченко', {'мат': 70, 'англ': 90, 'фп': 100})
        # student16 = Student('Олександр', 'Усик', {'мат': 100, 'англ': 80, 'фп': 100})
        # student17 = Student('Тарас', 'Смішний', {'мат': 100, 'англ': 80, 'фп': 100})
        # student18 = Student('Андрій', 'Лузан', {'мат': 70, 'англ': 70, 'фп': 70})
        # student19 = Student('Сніжана', 'Махмет', {'мат': 100, 'англ': 100, 'фп': 100})
        # student20 = Student('Анна', 'Прекрасна', {'мат': 80, 'англ': 100, 'фп': 100})
        # student21 = Student('Денчик', 'Найкращенко', {'мат': 95, 'англ': 100, 'фп': 95})
        # student22 = Student('Єгор', 'Мемченко', {'мат': 95, 'англ': 95, 'фп': 95})
        # student23 = Student('Анастасія', 'Симоні', {'мат': 80, 'англ': 100, 'фп': 90})
        # student24 = Student('Сергій', 'Мольфаренко', {'мат': 100, 'англ': 80, 'фп': 90})
        # student25 = Student('Джеймс', 'Патінсенко', {'мат': 95, 'англ': 95, 'фп': 100})

        tv_01 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                      student10, student11, student12)
        return tv_01
    except Exception as e:
        print(e)


# def set_ti_01():
#


if __name__ == '__main__':
    main()