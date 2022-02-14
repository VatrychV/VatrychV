import random
import sys

name= (input("Привет, как тебя зовут?: "))
print(f"Привет, {name}"),"\nСейчас сыграем в игру Угадай Число\nЯ загадаю число от 0 до 10, а ты пробуешь угадать." 
print("Сейчас сыграем в игру Угадай Число\nЯ загадаю число от 0 до 10, а ты пробуешь угадать.\nДля выхода нажмите Ctrl + C ")
 
arguments = sys.argv[1:]
a,b = 0 ,10
if len(arguments)>0:
  a = int(arguments[0])
if len(arguments)>1:
  b = int(arguments[1])
r = random.randint(a,b)

def game():
  counter = 0 
  while True:
    counter += 1
    print ("Попытка номер: ",counter)
    try:
     i = int(input("Какое число я загадал? :"))
    except ValueError: 
     print ("Вы ввели не число!")
    else :
     if i < 0 :
      print ("Значения меньше 0")
     elif  0 <= i >= 11: 
      print ("Число больше 10, выбери число от 0 до 10 ")
     elif i < r: 
      print ("Твоё число меньше!\nПопробуй снова!")
     elif i > r:
      print("Твоё число больше!\nПопробуй снова!")
     elif i == r: 
      print ((r), "Ты угадал!\nКонец игры!",)
      break
game()