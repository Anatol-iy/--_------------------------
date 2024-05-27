import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.right(90)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.left(45)
    t.backward(length)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))
    
    # Налаштування turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість черепашки
    
    # Початкове положення черепашки
    t.penup()
    t.goto(0, -200)  # Зміна початкової позиції на центр екрану
    t.left(90)      # Повертаємо черепашку вгору
    t.pendown()
    
    # Малювання дерева Піфагора
    draw_pythagoras_tree(t, 100, level)
    
    # Завершення роботи turtle
    turtle.done()

if __name__ == "__main__":
    main()
