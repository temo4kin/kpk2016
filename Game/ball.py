import tkinter

ball_initial_number = 10

def click_ball(event):
    """ Обработчик событий для холста
    :param event: событие
    :return: ничего
    """
    print(event.x, event.y)
    if event.widget != canvas:
        print('Странно, ведь paint() привязыывали только к canvas')
        return
    #canvas.coords(line, 0, 0, event.x, event.y)


def create_ramndom_ball():
    """
    Создает шарик в случайном месте игрового холста canvas, при этом шарик не выходит за границы холста
    :return:
    """
    x = ???
    y = ???
    R = ???

    oval = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())


def random_color():



def init_ball_catch_game():
    """
    Создает необходимое количество шариков, по которым нужно будет кликать
    :return:
    """
    for i in range(ball_initial_number):

def init_main_window():
    global root, canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root,bg="lightblue", width="400", height="400")
    canvas.bind("<Motion>", click_ball)
    canvas.pack()




if __name__=="__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()

