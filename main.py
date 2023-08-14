from mimesis import Person, Address, Finance, Transport, Payment
from mimesis.locales import Locale
from mimesis.enums import Gender
from mimesis.builtins import RussiaSpecProvider
from datetime import date
from random import choice


def create_fake_person():
    address = Address(Locale.RU)
    fin = Finance(Locale.RU)
    person = Person(Locale.RU)
    pay = Payment()
    transport = Transport()
    ru_spec = RussiaSpecProvider()
    mail_dict = ['mail.ru', 'gmail.com', 'yandex.ru', 'outlook.com', 'rambler.ru']

    age_pers = person.age(minimum=14, maximum=66)
    dict_person = {'ФИО': f'{person.first_name(gender=Gender.MALE)} {ru_spec.patronymic(gender=Gender.MALE)}'
                          f' {person.last_name(gender=Gender.MALE)}', 'Год рождения': date.today().year - age_pers,
                   'Возраст': age_pers, 'Адрес': f'{address.postal_code()}, {address.city()}, {address.address()}',
                   'Номер телефона': person.telephone(mask='+7-9##-###-####'),
                   'E-mail': person.email(domains=[choice(mail_dict)]),
                   'Паспорт': ru_spec.series_and_number(),
                   'ИНН': ru_spec.inn(),
                   'СНИЛС': ru_spec.snils(),
                   'Бансковская карта': f'{pay.credit_card_number(card_type=None)},'
                                        f'{pay.credit_card_expiration_date(minimum=23, maximum=27)}, {pay.cvv()}',
                   'Автомобиль': transport.car(),
                   'Образование': person.university(),
                   'Место работы': f'{fin.company_type(abbr=True)} {fin.company()}',
                   'Должность': person.occupation().lower(),
                   'Политические взгляды': person.political_views().lower(),
                   'Мировозрение': person.worldview().lower(),
                   'Вес': person.weight(minimum=55, maximum=120),
                   'Группа крови': person.blood_type()
                   }
    return dict_person

def print_person(dict_person, i):
    with open('person.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
    for item in dict_person:
        print(f'{item}: {dict_person[item]}')
        with open('person.txt', 'a', encoding='utf-8') as file:
            file.write(f'{item}: {dict_person[item]}\n')

def main():
    pers_count = int(input('Сколько личностей?'))
    for i in range(pers_count):
        print(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
        dict_pers = create_fake_person()
        print_person(dict_pers, i)

if __name__ == '__main__':
    main()
