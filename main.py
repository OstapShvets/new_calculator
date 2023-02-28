while True:
    try:
        num1 = float(input("Ведіть число:"))
        num2 = float(input("Ведіть друге число:"))
    except ValueError:
        print("Має бути лише число")
    except KeyboardInterrupt:
        print("Помилка!")
        continue

    value_operator = input("Виберіть свій варіант: \n1 '+', \n2 '-', \n3 '*', \n4 '/'")
    result = None
    if value_operator in ['1', '2', '3', '4']:
        if value_operator == '1':
            result = num1 + num2
        elif value_operator == '2':
            result = num1 - num2
        elif value_operator == '3':
            result = num1 * num2
        elif value_operator == '4':
            if num2 == 0:
                print("На нуль ділити не можна!")
                continue
            else:
                result = num1 / num2
    else:
        print("Це лише може бути число від 1 до 4")
    print(result)
    finish = input("Чи хочите ви продовжити? (Так/Ні)")
    if finish == 'Так':
        continue
    else:
        break