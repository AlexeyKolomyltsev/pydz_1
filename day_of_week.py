def day_of_week(day):
    if day > 7:
        print('Нет такого дня недели')
    else:
        for key, num_days in week.items():
            if day in num_days:
                print(f'{day} день недели - {key}')
                break

week  = {'нет, будний' : list(range(1,6)), 'да, выходной' : [6, 7] }

day_of_week(int(input('Введите день недели: ')))
