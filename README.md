# Генератор безопасных паролей на Python

Простой и эффективный генератор паролей с настраиваемыми параметрами.

## Возможности

- Генерация паролей настраиваемой длины
- Опциональное использование цифр
- Опциональное использование специальных символов
- Опциональное использование заглавных букв
- Гарантированное включение как минимум одного символа каждого выбранного типа
- Проверка минимальной длины пароля

## Установка

```bash
git clone https://github.com/looapz/py-password-generator.git
cd py-password-generator
```

## Использование

Запустите скрипт с помощью Python:

```bash
python password_generator.py
```

Следуйте инструкциям в консоли для настройки параметров генерации пароля:
1. Введите желаемую длину пароля (минимум 4 символа)
2. Укажите, нужно ли использовать цифры (y/n)
3. Укажите, нужно ли использовать специальные символы (y/n)
4. Укажите, нужно ли использовать заглавные буквы (y/n)

## Пример использования в коде

```python
from password_generator import generate_password

# Генерация пароля с настраиваемыми параметрами
password = generate_password(
    length=16,
    use_digits=True,
    use_special=True,
    use_uppercase=True
)
print(f"Сгенерированный пароль: {password}")
```

## Безопасность

Генератор использует криптографически безопасный генератор случайных чисел Python для создания паролей. Каждый пароль гарантированно содержит как минимум один символ каждого выбранного типа для обеспечения сложности.

## Лицензия

MIT