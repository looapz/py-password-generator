import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_uppercase=True):
    """
    Генерирует случайный пароль с заданными параметрами
    """
    # Определяем набор символов
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    # Генерируем пароль
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")
    
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # Проверяем, что пароль содержит хотя бы один символ каждого типа
    if use_uppercase and not any(c.isupper() for c in password):
        password = random.choice(string.ascii_uppercase) + password[1:]
    if use_digits and not any(c.isdigit() for c in password):
        password = password[:-1] + random.choice(string.digits)
    if use_special and not any(c in string.punctuation for c in password):
        pos = random.randint(1, len(password)-2)
        password = password[:pos] + random.choice(string.punctuation) + password[pos+1:]
    
    return password

def main():
    print("Генератор безопасных паролей")
    print("-" * 30)
    
    try:
        length = int(input("Введите длину пароля (минимум 4): "))
        use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
        use_special = input("Использовать специальные символы? (y/n): ").lower() == 'y'
        use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
        
        password = generate_password(
            length=length,
            use_digits=use_digits,
            use_special=use_special,
            use_uppercase=use_uppercase
        )
        
        print("\nСгенерированный пароль:")
        print("-" * 30)
        print(password)
        print("-" * 30)
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")

if __name__ == '__main__':
    main()