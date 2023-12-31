import pandas as pd
from services.filter import filter_dataset
from services.get_group import age_grouping

groups = {
    "Юристы": ['Юрисконсульт', 'Юрист'],
    "Финансы, бухгалтерия": ['Экономист', 'Финансовый менеджер', 'Кредитный специалист', 'Бухгалтер'],
    "Управление персоналом": ['Менеджер по персоналу', 'Специалист по кадрам', 'Специалист по отбору персонала',
                              'Специалист по подбору персонала'],
    "Туризм, гостиницы, рестораны": ['Менеджер по туризму', 'Менеджер ресторана', 'Менеджер АХО',
                                     'Официант, бармен, бариста', 'Повар, пекарь, кондитер', 'Уборщица, уборщик'],
    "Транспорт, логистика, перевозки": ['Упаковщик, комплектовщик', 'Руководитель отдела логистики', 'Начальник склада',
                                        'Машинист', 'Менеджер по логистике, менеджер по ВЭД', 'Водитель', 'Диспетчер',
                                        'Кладовщик', 'Курьер'],
    'Строительство, недвижимость': ['Разнорабочий', 'Руководитель проектов',
                                    'Монтажник', 'Инженер-конструктор, инженер-проектировщик',
                                    'Инженер по охране труда и технике безопасности, инженер-эколог'],
    'Спортивные клубы, фитнес, салоны красоты': ['Фитнес-тренер, инструктор тренажерного зала',
                                                 'Менеджер по продажам, менеджер по работе с клиентами'],
    'Розничная торговля': ['Администратор магазина, администратор торгового зала', 'Мерчандайзер',
                           'Продавец-консультант, продавец-кассир', 'Супервайзер', 'Товаровед'],
    'Производство, сервисное обслуживание': ['Инженер по охране труда и технике безопасности, инженер-эколог',
                                             'Инженер-конструктор, инженер-проектировщик', 'Механик',
                                             'Начальник производства', 'Начальник смены, мастер участка',
                                             'Оператор производственной линии', 'Сварщик',
                                             'Сервисный инженер, инженер-механик', 'Слесарь, сантехник', 'Технолог'],
    'Продажи, обслуживание клиентов': ['Кассир-операционист', 'Координатор отдела продаж',
                                       'Менеджер по продажам, менеджер по работе с клиентами',
                                       'Оператор call-центра, специалист контактного центра',
                                       'Продавец-консультант, продавец-кассир', 'Руководитель отдела продаж',
                                       'Специалист технической поддержки', 'Торговый представитель'],
    'Наука, Образование': ['Психолог', 'Учитель, преподаватель, педагог'],
    'Медицина, фармацевтика': ["Врач"],
    'Маркетинг, реклама, PR': ['SMM-менеджер, контент-менеджер', 'Дизайнер, художник',
                               'Менеджер по маркетингу, интернет-маркетолог',
                               'Менеджер по продажам, менеджер по работе с клиентами'],
    'Информационные технологии': ['Аналитик', 'Программист, разработчик', 'Руководитель проектов',
                                  'Системный администратор', 'Тестировщик'],
    'Домашний, обслуживающий персонал': ['Воспитатель, няня', 'Охранник', 'Уборщица, уборщик'],
    'Высший и средний менеджмент': ['Генеральный директор, исполнительный директор (CEO)', 'Начальник производства',
                                    'Директор магазина, директор сети магазинов'],
    'Административный персонал': ['Администратор', 'Делопроизводитель, архивариус', 'Менеджер/руководитель АХО',
                                  'Оператор ПК, оператор базы данных', 'Офис-менеджер',
                                  'Секретарь, помощник руководителя, ассистент']
}
specialties = groups.keys()
df = pd.read_csv('../hh_ru_dataset.csv', sep=',')
df = filter_dataset(df, salary_upper_limit=500000, only_final_invitation=True, only_initial_response=True)
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
df = age_grouping(df)
professions = list(set(list(df["profession"].values)))
for i in professions:
    count = 0
    for j in specialties:
        if i in groups[j]:
            count += 1
    if count >= 2:
        print(i, count)
