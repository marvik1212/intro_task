"""Генератор приветствий."""

def Greeting(name: str) -> str:
      """Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Returns:
          str: Текст приветствия
      """
      name = name.title()
      return f'Привет, {name}'
