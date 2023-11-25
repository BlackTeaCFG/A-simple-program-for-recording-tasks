
def main():
    file = open('1.txt', 'a')
    file.write(f'У пользователя {name} есть {count} задач\n')
    chet = 1
    for line in range(count):
        print('Введите задачу')
        file.write(f'{chet} Задача: {input()}\n')
        primeta = input('Вы хотите сделать примечание? Да или Нет?\n')
        if primeta == 'Да' or primeta == 'да':
            print("Напишите своё примечание:")
            file.write(f'Пользователь с именем {name} оставил примечание\n\t{input()}\n\t')
            print('Ваши данных сохранены')
        else:
            print('Ваши данных сохранены')
        chet +=1


name = input('Введите своё имя\n')
count = int(input('Введите количество ваших задач\n'))

if __name__ == '__main__':
    main()
