from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    birthdate_dirty = request.GET.get('s')
    if birthdate_dirty:
        birthdate = birthdate_dirty[-2:] + birthdate_dirty[5:7] + birthdate_dirty[:4]
        bd = f'{birthdate_dirty[-2:]}.{birthdate_dirty[5:7]}.{birthdate_dirty[:4]}'
        first_dop_num = 0
        for i in birthdate:
            first_dop_num += int(i)
        second_dop_num = sum(int(i) for i in str(first_dop_num))
        if second_dop_num == 10:
            second_dop_num = 1
        elif second_dop_num > 11:
            second_dop_num = sum(int(i) for i in str(second_dop_num))
        third_dop_num = (first_dop_num - 2 * int(birthdate[0])) if int(birthdate[0]) != 0 else (
                first_dop_num - 2 * int(birthdate[1]))
        fourth_dop_num = third_dop_num if int(third_dop_num) < 0 else sum(int(i) for i in str(third_dop_num))
        birthdate_dop_num = birthdate + str(first_dop_num) + str(second_dop_num) + str(third_dop_num) + str(
            fourth_dop_num)
        character = birthdate_dop_num.count('1') * '1' if birthdate_dop_num.count('1') else 'нет'
        energy = birthdate_dop_num.count('2') * '2'
        interest = birthdate_dop_num.count('3') * '3'
        health = birthdate_dop_num.count('4') * '4'
        logic = birthdate_dop_num.count('5') * '5'
        work = birthdate_dop_num.count('6') * '6'
        luck = birthdate_dop_num.count('7') * '7'
        debt = birthdate_dop_num.count('8') * '8'
        memory = birthdate_dop_num.count('9') * '9'
        life = len(health + logic + work)
        print('Быт =', life if life else 'нет')
        goal = len(character + health + luck)
        print('Цель =', goal if goal else 'нет')
        family = len(energy + logic + debt)
        print('Семья =', family if family else 'нет')
        habit = len(interest + work + memory)
        print('Привычки =', habit if habit else 'нет')
        temperament = len(interest + logic + luck)
        print('Темперамент =', temperament if temperament else 'нет')
    else:
        bd = '--.--.----'
        first_dop_num = '-'
        second_dop_num = '-'
        third_dop_num = '-'
        fourth_dop_num = '-'
        character = '-'
        energy = '-'
        interest = '-'
        health = '-'
        logic = '-'
        work = '-'
        luck = '-'
        debt = '-'
        memory = '-'
        life = '-'
        goal = '-'
        family = '-'
        habit = '-'
        temperament = '-'

    return render(request, 'matrix/home.html', {
        'bd': bd,
        'first_dop_num': first_dop_num,
        'second_dop_num': second_dop_num,
        'third_dop_num': third_dop_num,
        'fourth_dop_num': fourth_dop_num,
        'character': character if character else 'нет',
        'energy': energy if energy else 'нет',
        'interest': interest if interest else 'нет',
        'health': health if health else 'нет',
        'logic': logic if logic else 'нет',
        'work': work if work else 'нет',
        'luck': luck if luck else 'нет',
        'debt': debt if debt else 'нет',
        'memory': memory if memory else 'нет',
        'life': life if life else 'нет',
        'goal': goal if goal else 'нет',
        'family': family if family else 'нет',
        'habit': habit if habit else 'нет',
        'temperament': temperament if temperament else 'нет',
        'dop_nums': f'{first_dop_num}, {second_dop_num}, {third_dop_num}, {fourth_dop_num}',
    }
                  )
