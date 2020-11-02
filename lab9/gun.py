from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
canvas.focus_set()


class Ball:
    def __init__(self, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'brown'])
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени

        Метод описывает перемещение мяча за один кадр перерисовки, обновляя значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600)
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 2
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -0.5 * self.vx
            self.vy *= 0.5
        elif self.x + self.r >= 800:
            self.x = 800 - self.r
            self.vx = -0.5 * self.vx
            self.vy *= 0.5
        if self.y + self.r >= 600:
            self.y = 600 - self.r
            self.vy = -0.5 * self.vy
            self.vx *= 0.5
            if abs(self.vy) <= 4:
                self.vy = 0
            if abs(self.vx) <= 1:
                self.vx = 0
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj

        Args:
            obj: Обьект, с которым проверяется столкновение
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        return False


class MassiveBall(Ball):
    def __init__(self, x, y):
        super(MassiveBall, self).__init__(x, y)
        self.r = 25
        self.color = choice(['orange', 'black'])
        canvas.itemconfig(self.id, fill=self.color)


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x0 = 30
        self.y0 = 550
        self.id_body = canvas.create_rectangle(self.x0, self.y0, self.x0 + 100, self.y0 + 50, fill='grey')
        self.id = canvas.create_line(self.x0, self.y0, self.x0 + 30, self.y0 - 30, width=7)

    def fire2_start(self, event):
        if event.keysym == 'space' or event.keysym == '??':
            self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом

        Происходит при отпускании кнопки мыши
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши
        """
        global balls, bullet
        if event.keysym == 'space' or event.keysym == '??':
            bullet += 1
            if not is_massive:
                new_ball = Ball(x=self.x0, y=self.y0)
            else:
                new_ball = MassiveBall(x=self.x0, y=self.y0)
                new_ball.color = 'orange'
            new_ball.r += 5
            if event.x - new_ball.x > 0:
                self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
            elif event.x - new_ball.x < 0:
                self.an = math.pi + math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
            else:
                self.an = math.pi / 2
            if not is_massive:
                new_ball.vx = self.f2_power * math.cos(self.an)
                new_ball.vy = -self.f2_power * math.sin(self.an)
            else:
                new_ball.vx = self.f2_power * math.cos(self.an) / 2
                new_ball.vy = -self.f2_power * math.sin(self.an) / 2
            balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

    def targeting(self, event):
        """
        Прицеливание
        Зависит от положения мыши
        """
        if event:
            if event.x - self.x0 > 0:
                self.an = math.atan((event.y - self.y0) / (event.x - self.x0))
            elif event.x - self.x0 < 0:
                self.an = math.pi + math.atan((event.y - self.y0) / (event.x - self.x0))
            else:
                self.an = math.pi / 2
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, self.x0, self.y0,
                      self.x0 + max(self.f2_power, 20) * math.cos(self.an),
                      self.y0 + max(self.f2_power, 20) * math.sin(self.an)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')

    def move_right(self, event):
        if event.keysym == 'Right' and self.x0 <= 698:
            self.x0 += 2
            canvas.move(self.id, 2, 0)
            canvas.move(self.id_body, 2, 0)

    def move_left(self, event):
        if event.keysym == 'Left' and self.x0 >= 2:
            self.x0 -= 2
            canvas.move(self.id, -2, 0)
            canvas.move(self.id_body, -2, 0)


class ClassicTarget:
    def __init__(self, x=0, y=0, r=0, vx=0, vy=0):
        self.color = 'red'
        self.points = 0
        self.live = 1
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r)

    def new_target(self):
        """ Инициализация новой цели"""
        x = self.x = rnd(200, 750)
        y = self.y = rnd(100, 550)
        r = self.r = rnd(5, 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        color = self.color
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель"""
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points

    def move(self):
        x, y = self.x, self.y
        if self.vx == 0:
            self.vx = rnd(1, 5)
        if self.vy == 0:
            self.vy = rnd(1, 5)
        self.x += self.vx
        self.y -= self.vy
        if self.x - self.r <= 0 or self.x + self.r >= 800:
            self.vx = -self.vx
        if self.y - self.r <= 0 or self.y + self.r >= 600:
            self.vy = -self.vy
        canvas.move(self.id, self.x - x, self.y - y)


class EllipseMovingTarget(ClassicTarget):
    def __init__(self):
        super(EllipseMovingTarget, self).__init__()
        self.color = 'yellow'
        self.center_of_ellipse_x = rnd(100, 700)
        self.center_of_ellipse_y = rnd(100, 500)

    def move(self):
        self.vx += (self.center_of_ellipse_x - self.x) / 50
        self.vy += (self.center_of_ellipse_y - self.y) / 50
        if self.x - self.r <= 0:
            self.vx = abs(self.vx)
        elif self.x + self.r >= 800:
            self.vx = -abs(self.vx)
        if self.y - self.r <= 0:
            self.vy = abs(self.vy)
        elif self.y + self.r >= 600:
            self.vy = -abs(self.vy)
        self.x += self.vx
        self.y += self.vy
        canvas.move(self.id, self.vx, self.vy)


def change_types_of_balls():
    global is_massive
    is_massive = not is_massive


t1 = ClassicTarget()
t2 = EllipseMovingTarget()
screen1 = canvas.create_text(400, 300, text='', font='28')
screen2 = canvas.create_text(720, 30, text='Ваши жизни: 3', font='28')
is_massive = False
g1 = Gun()
bullet = 0
balls = []
targets = [t1, t2]
sum_points = 0
screen_points = canvas.create_text(30, 30, text=sum_points, font='28')


def new_game(event=''):
    global t1, t2, screen1, balls, bullet, sum_points, screen_points
    for b in balls:
        canvas.delete(b.id)
    t1.new_target()
    t2.new_target()

    bullet = 0
    balls = []
    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<KeyPress>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', g1.fire2_end)
    canvas.bind('<KeyRelease>', g1.fire2_end)
    canvas.bind('<Motion>', g1.targeting)
    canvas.bind('<Left>', g1.move_left)
    canvas.bind('<Right>', g1.move_right)

    is_hit_1 = False
    is_hit_2 = False

    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        for t in targets:
            t.move()
        for b in balls:
            b.move()
            if b.vx == 0 and b.vy == 0:
                b.live -= 1
            if b.live <= 0:
                canvas.delete(b.id)
                balls.remove(b)
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                is_hit_1 = True
                sum_points += 1
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                is_hit_2 = True
                sum_points += 1
            canvas.delete(screen_points)
            screen_points = canvas.create_text(30, 30, text=sum_points, font='28')
            if is_hit_1 and is_hit_2:
                canvas.bind('<Button-1>', '')
                canvas.bind('<KeyPress>', '')
                canvas.bind('<ButtonRelease-1>', '')
                canvas.bind('<KeyRelease>', '')
                if 5 <= int(str(bullet)[-1]) <= 9 or int(str(bullet)[-1]) == 0:
                    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                elif bullet == 1:
                    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрел')
                elif 2 <= bullet <= 4:
                    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрела')
                elif str(bullet)[-2] == '1':
                    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                elif str(bullet)[-1] == '1':
                    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрел')
                else:
                    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрела')
        canvas.update()
        time.sleep(0.03)
        g1.targeting(event)
        g1.power_up()
    canvas.itemconfig(screen1, text='')
    canvas.delete(Gun)
    root.after(750, new_game)


new_game()

tk.mainloop()
