
#Задание №7
# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.



# number = int(input('Введите число: '))
# base = 16
# original_number = number
# result_number = ''
# while number:
# 	result_number = str(number % base) + result_number
# 	number //= base
# print(f'Число {original_number} в {base} системе счисления будет: {result_number}')
# print(hex(original_number))

#==================================================================================================
import fractions
# Преобразуем дроби из строк в числа
num1, denom1 = map(int, input("Введите первую дробь в формате a/b: ").split("/"))
num2, denom2 = map(int, input("Введите вторую дробь в формате c/d: ").split("/"))

# Вычисляем сумму дробей
sum_frac_num = num1 * denom2 + num2 * denom1
sum_frac_denom = denom1 * denom2
sum_frac = (sum_frac_num, sum_frac_denom)

print(f"Сумма дробей {sum_frac_num} и {sum_frac_denom} - {sum_frac[0]}/{sum_frac[1]}")
print(fractions.Fraction(num1, denom1)+fractions.Fraction(num2, denom2))

# Вычисляем произведение дробей
prod_frac_num = num1 * num2
prod_frac_denom = denom1 * denom2
prod_frac = (prod_frac_num, prod_frac_denom)

print(f"Произведение дробей {prod_frac_num} и {prod_frac_denom} - {prod_frac_num}/{prod_frac_denom}")
print("#сокращенная дробь",fractions.Fraction(num1, denom1) * fractions.Fraction(num2, denom2)) #сокращенная дробь
