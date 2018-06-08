
class Romanos(object):
    roman_numbers = {
        'M': 1000,
        'IM': 999,
        'CM':900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL':40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV':4,
        'I': 1,
    }
    decimal = {v: k for k, v in roman_numbers.items()}

    def to_roman(self, num):
        result = ''
        if num > 1000 or num <= 0:
            raise ValueError('El numero debe estar dentro del rango 1-1000')

        for i, k in self.decimal.items():
            while num % i < num:
                result += self.decimal[i]
                num -= self.roman_numbers[k]

        return result






cancel = 'n'
print('Para cancelar ingrese "y"')
while cancel == 'n':

    number = input('Ingrese el numero entero a convertir: ')
    if number == 'y':
        cancel = 'y'
        break

    try:
        romanos = Romanos()
        result = romanos.to_roman(int(number))
        print(result)

    except ValueError as error:
        print(error.args[0])

print('Ejecucion interrumpida por el usuario')