import tkinter
from random import choice, randint
import time
#import sys


ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
colors = ('brown','red', 'green', 'blue', 'yellow', 'cyan', 'gray', 'navy', 'silver', 'black', 'olive', 'teal', 'magenta', 'maroon', 'bisque', 'lightgreen', 'lightblue', 'lightyellow', 'lightcyan', 'lightgray', 'maroon', 'darkred', 'darkgreen', 'darkblue', 'darkcyan', 'darkgray', 'darkmagenta')
#ball_available_colors = '0123456789ABCDEF'#['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
balls_coord = []#список координат шариков
balls_num = []#список номеров шариков


def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитываеть его в очки пользователя.
    """
    global points, label,  balls_coord, balls_num, rand_color
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    num = obj[0]# вытаскиваем номер объекта из кортежа
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        index = balls_num.index(num)# определяем индекс элемента списка, где храниться номер объекта
        balls_num.pop(index)# удаляем элемент списка с номером объекта
        balls_coord.pop(index)# удаляем элемент списка с координатами объекта
        if rand_color in ('bisque', 'lightgreen', 'lightblue', 'lightyellow', 'lightcyan', 'lightgray'):
            points += 2
        elif rand_color in ('darkred', 'darkgreen', 'darkcyan', 'darkgray', 'darkmagenta'):
            points -= 1
        elif rand_color in ('brown', 'black', 'darkblue', 'maroon'):
            points -= 2
        else:
            points += 1
        label['text']=points
        create_random_ball()


def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)"""
    global balls_coord
    """каждый шарик движется по своей траектории"""
    for obj in balls_coord:
        x1, y1, x2, y2 =canvas.coords(obj[0])
        # проверяем, не выйдет ли шарик за границы холста
        if x1+obj[1]+obj[3]>=400 or x1+obj[1]<=0:
            obj[1]=-obj[1] #меняем направление движения
        if y1+obj[2]+obj[3]>=400 or y1+obj[2]<=0:
            obj[2]=-obj[2]
        canvas.move(obj[0],obj[1],obj[2])

def create_random_ball():
    """
    создаёт шарик в случайном месте игрового холста canvas,
     при этом шарик не выходит за границы холста!
    """
    global balls_coord, balls_num, color, rand_color
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    #рисуем шарик и запоминаем его номер в num_oval
    rand_color= random_color()
    num_oval = canvas.create_oval(x, y, x+R, y+R, width=1, fill=rand_color)
    dx = randint(-2, 2)
    dy = randint(-2, 2)
    # запоминаем идентификатор, вектор и радиус движения нового шарика
    balls_coord.append([num_oval, dx, dy, R])
    balls_num.append(num_oval)# запоминаем номер нового шарика


def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов

    #return choice(ball_available_colors)

    color = '#'
    for c in range(6):
        color = color + choice(ball_available_colors)
    """
    n = randint(0, 26)
    color = colors[n]
    return color


def init_ball_catch_game():
    """
    Создаём необходимое для игры количество шариков, по которым нужно будет кликать.
    """
    global timeEnd

    for i in range(ball_initial_number):
        create_random_ball()
    timeEnd = int(time.time()+20)
    tick()

"""
-------- Код от ganilova (https://github.com/ganilova) -------------------
-------- Немного переработано и изменено ---------------------------------
"""

def close_win():
    root.destroy()

def close_rule():
    tex.destroy()
    close.destroy()
    win.destroy()

def new_win():
    global win, tex, close

    win = tkinter.Toplevel(root)
    win.title("Правила игры")
    rule = "За отведенное время надо набрать\n наибольшее количество очков.\nЧасть цветов приносит баллы (1 или 2),\n а другие - отнимают (1 или 2)"
    tex = tkinter.Label(win, text=rule, width=40,height= 10, font="Verdana 12")
    tex.pack()
    close = tkinter.Button(win, text="Закрыть",command=close_rule)#Срабатывает на нажатие и отпуск мышки
    close.pack()

def init_menu():
    m = tkinter.Menu(root)
    root.config(menu = m)
    fm = tkinter.Menu(m)
    m.add_cascade(label="Меню", menu=fm)
    fm.add_command(label="Правила игры", command=new_win)
    fm.add_command(label="Выход", command=close_win)


def ex_it():
    #global win
    exit('Время закончилось!')


def game_over():
    global  tex, close, win, points
    win = tkinter.Toplevel(root)
    win.title("Конец игры")
    rule = "Игра закончена!\n вы набрали:", points, " баллов."
    tex = tkinter.Label(win, text=rule, width=40,height= 10, font="Verdana 12")
    tex.pack()
    close = tkinter.Button(win, text="Закрыть")#Срабатывает на нажатие и отпуск мышки
    close.pack("<Button-1>", ex_it())


def tick():
    global timeEnd

    if timeEnd - int(time.time()) > 0:
        time_Go.config(text=(timeEnd - int(time.time())))
    elif timeEnd - int(time.time()) <= 0:
        #time.sleep(10)
        #exit('Время закончилось!')
        #raise SystemExit
        game_over()
        #ex_it()
        return
    time_Go.after(200, tick)

# ------------- End ----------------------

def init_main_window():
    global root, canvas, label, points, time_Go, frame_text

    root = tkinter.Tk()
    root.title("Игра в шарики")
    init_menu()
    frame_text = tkinter.Frame(root)
    label_text = tkinter.Label(root, text = 'Заработанные баллы:')
    label_text.pack()
    points = 0
    label = tkinter.Label(root, text=points)#привязка к переменной
    label.pack()
    time_text = tkinter.Label(frame_text, text='Оставшееся время (сек)', width=20, font='Calibri 14')
    time_Go = tkinter.Label(frame_text, font='Calibri 14')
    time_text.grid(row=2, column=0)
    time_Go.grid(row=2, column=1)
    frame_text.pack()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()
    label_text = tkinter.Label(root, text = 'За "обычные" цвета даётся по 1 баллу:')
    label_text.pack()
    canvas2 = tkinter.Canvas(root, height=50)
    canvas2.create_rectangle(10,10,30,30,fill="red", width=1)
    canvas2.create_rectangle(40,10,60,30,fill="green", width=1)
    canvas2.create_rectangle(70,10,90,30,fill="blue", width=1)
    canvas2.create_rectangle(100,10,120,30,fill="yellow", width=1)
    canvas2.create_rectangle(130,10,150,30,fill="cyan", width=1)
    canvas2.create_rectangle(160,10,180,30,fill="gray", width=1)
    canvas2.create_rectangle(190,10,210,30,fill="navy", width=1)
    canvas2.create_rectangle(220,10,240,30,fill="silver", width=1)
    canvas2.create_rectangle(250,10,270,30,fill="olive", width=1)
    canvas2.create_rectangle(280,10,300,30,fill="teal", width=1)
    canvas2.create_rectangle(310,10,330,30,fill="magenta", width=1)
    canvas2.pack()
    label_text = tkinter.Label(root, text = 'За бонусные цвета даётся по 2 балла:')
    label_text.pack()
    canvas3 = tkinter.Canvas(root, height=50)
    canvas3.create_rectangle(10,10,30,30,fill="bisque", width=1)
    canvas3.create_rectangle(40,10,60,30,fill="lightgreen", width=1)
    canvas3.create_rectangle(70,10,90,30,fill="lightblue", width=1)
    canvas3.create_rectangle(100,10,120,30,fill="lightyellow", width=1)
    canvas3.create_rectangle(130,10,150,30,fill="lightcyan", width=1)
    canvas3.create_rectangle(160,10,180,30,fill="lightgray", width=1)
    canvas3.pack()
    label_text = tkinter.Label(root, text = 'За штрафные цвета отнимается по 1 баллу:')
    label_text.pack()
    canvas4 = tkinter.Canvas(root, height=50)
    canvas4.create_rectangle(10,10,30,30,fill="darkred", width=1)
    canvas4.create_rectangle(40,10,60,30,fill="darkgreen", width=1)
    canvas4.create_rectangle(70,10,90,30,fill="darkcyan", width=1)
    canvas4.create_rectangle(100,10,120,30,fill="darkgray", width=1)
    canvas4.create_rectangle(130,10,150,30,fill="darkmagenta", width=1)
    canvas4.pack()
    label_text = tkinter.Label(root, text = 'За штрафные цвета отнимается по 1 баллу:')
    label_text.pack()
    canvas5 = tkinter.Canvas(root, height=50)
    canvas5.create_rectangle(10,10,30,30,fill="brown", width=1)
    canvas5.create_rectangle(40,10,60,30,fill="black", width=1)
    canvas5.create_rectangle(70,10,90,30,fill="darkblue", width=1)
    canvas5.create_rectangle(100,10,120,30,fill="maroon", width=1)
    canvas5.pack()

if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Ваш счет:", points)