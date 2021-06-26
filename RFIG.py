import pygame
import os
import sys
import random


class Board:
    def __init__(self, width, height):
        self.OldCord = None
        self.width = width
        self.height = height
        self.board = [[0] * (width) for _ in range(height)]
        self.hod = [[0] * (width) for _ in range(height)]
        # board это матрица со всеми фигурами которые отрисововаються
        # хочу заметить что board[0] это a, тоесть они вертикальны

        self.NewCord = False
        # эта переменная отвечает за смену позиции,
        # если она True то следущее нажатие меняет класс board,
        # все это происходит в reverse

        self.left = 10
        self.top = 10
        self.cell_size = 30
        # задает размеры и отступы клеток

    def boardd(self):
        # задаю начальное состояние матрицы, потом сюда зафигачим рандом
        # ps рандом доделал
        choic = [1, 2, 3, 4]
        choic2 = [2, 3, 4, 6]
        # по правилам шахмат фишера с 1\2 стороны первой строчки
        # и с 2\2 должны быть одинаковые фигуры
        for t in range(4):
            c = random.choice(choic)
            self.board[t] = [c, 0, 0, 0, 0, 0, 0, c + 6]
            # фигачу на первую клетку фигуру 1ого игрока и на зеркальную второго
            # print(f'{t}: {c} из {choic}')
            for j in range(len(choic)):
                i = choic[j]
                if i == c:
                    # print(f'{i} == {c}: {choic[j]}')
                    del choic[j]
                    break
        for t in range(4, 8):
            c = random.choice(choic2)
            self.board[t] = [c, 0, 0, 0, 0, 0, 0, c + 6]
            # print(f'{t}: {c} из {choic2}')
            c1 = []
            for j in range(len(choic2)):
                i = choic2[j]
                if i == c:
                    # print(f'{i} == {c}: {choic[j]}')
                    del choic2[j]
                    break
        for i in range(8):
            self.board[i][1] = 5
            self.board[i][len(self.board) - 2] = 5 + 6
        # self.board[5][5] = 2
        # ставлю в центр поля фигуру
        # это использовалось для калибровки фигур

    def set_view(self, left, top, cell_size):
        # отвечает за размеры поля и клетки
        self.left = left  # отступ в лево
        self.top = top  # отступ наверх
        self.cell_size = cell_size

    def render(self, screen):
        l = self.left
        t = self.top
        c = self.cell_size
        color = {0: (255, 255, 255), 1: (255, 0, 0), 2: (0, 0, 255)}
        dosca(screen)
        # доска закрашивает поле
        for x in range(self.height):
            for y in range(self.width):
                # бегу по клеткам поля
                coard = (x * c + l, y * c + t, c, c)
                # 0 - ничего 1 - король(self.korol), 2 -  ладья(self.lad), 3 - конь(self.kon),
                # 4 - слон (self.slon), 5 - пешка(self.pesh), 6 - королева(self.qween)
                if self.board[x][y] == 0:
                    pygame.draw.rect(screen, color[0], coard, 1)
                elif self.board[x][y] == 1:
                    self.all_sprites.draw(screen)
                    self.korol.rect.x = x * c
                    self.korol.rect.y = y * c
                    # рисуем все спрайты где то и при перемещении просто меняем кадры
                elif self.board[x][y] == 2:
                    self.all_sprites.draw(screen)
                    self.lad.rect.x = x * c
                    self.lad.rect.y = y * c
                elif self.board[x][y] == 3:
                    self.all_sprites.draw(screen)
                    self.kon.rect.x = x * c
                    self.kon.rect.y = y * c
                elif self.board[x][y] == 4:
                    self.all_sprites.draw(screen)
                    self.slon.rect.x = x * c
                    self.slon.rect.y = y * c
                elif self.board[x][y] == 5:
                    self.all_sprites.draw(screen)
                    self.pesh.rect.x = x * c
                    self.pesh.rect.y = y * c
                elif self.board[x][y] == 6:
                    self.all_sprites.draw(screen)
                    self.qween.rect.x = x * c
                    self.qween.rect.y = y * c
                elif self.board[x][y] == 1 + 6:
                    # хуярю спрайты второго игрока
                    self.all_sprites.draw(screen)
                    self.korol2.rect.x = x * c
                    self.korol2.rect.y = y * c
                    # рисуем все спрайты где то и при перемещении просто меняем кадры
                elif self.board[x][y] == 2 + 6:
                    self.all_sprites.draw(screen)
                    self.lad2.rect.x = x * c
                    self.lad2.rect.y = y * c
                elif self.board[x][y] == 3 + 6:
                    self.all_sprites.draw(screen)
                    self.kon2.rect.x = x * c
                    self.kon2.rect.y = y * c
                elif self.board[x][y] == 4 + 6:
                    self.all_sprites.draw(screen)
                    self.slon2.rect.x = x * c
                    self.slon2.rect.y = y * c
                elif self.board[x][y] == 5 + 6:
                    self.all_sprites.draw(screen)
                    self.pesh2.rect.x = x * c
                    self.pesh2.rect.y = y * c
                elif self.board[x][y] == 6 + 6:
                    self.all_sprites.draw(screen)
                    self.qween2.rect.x = x * c
                    self.qween2.rect.y = y * c

        # бегу по циклу возм ходов
        for x in range(self.height):
            for y in range(self.width):
                if self.hod[x][y] == 1:
                    # ресую возможные ходы для фигур
                    pygame.draw.circle(screen, pygame.Color(pygame.Color(150, 150, 150)),
                                       (x * c + l + (c // 2), y * c + t + (c // 2)), ((c // 4) - 4), 2)

    def how_kw(self, x_c, y_c):
        song = pygame.mixer.Sound('click.mp3')
        song.play()
        # определяею на какую клетку нажал игрок
        l = self.left
        t = self.top
        c = self.cell_size
        for x in range(self.height):
            for y in range(self.width):
                kx, ky = (x * c + l, y * c + t)
                if kx < x_c < kx + c and ky < y_c < ky + 100:
                    # print(f'({x + 1}, {y + 1}) = {self.board[x][y]}')
                    return (x, y)
        # если за полем то не определяет
        return None

    def figur(self, f):
        # создает классы спрайтов что бы их отрисововать
        # фигуры с "2" это фигуры другого игрока
        self.all_sprites = pygame.sprite.Group()

        self.korol = pygame.sprite.Sprite()  # король
        self.korol.image = load_image('white_figure.png', -1)
        self.korol.rect = self.korol.image.get_rect()
        self.all_sprites.add(self.korol)
        self.korol.rect.x = 1000  # отрисововаю все фигуры в одной точке
        self.korol.rect.y = 1000  # потом просто буду менять координат спрайта

        self.lad = pygame.sprite.Sprite()  # ладья
        self.lad.image = load_image('white_figure.png', -1)
        self.lad.rect = self.lad.image.get_rect()
        self.all_sprites.add(self.lad)
        self.lad.rect.x = 1000
        self.lad.rect.y = 1000

        self.kon = pygame.sprite.Sprite()  # конь
        self.kon.image = load_image('white_figure.png', -1)
        self.kon.rect = self.kon.image.get_rect()
        self.all_sprites.add(self.kon)
        self.kon.rect.x = 1000
        self.kon.rect.y = 1000

        self.slon = pygame.sprite.Sprite()  # слон
        self.slon.image = load_image('white_figure.png', -1)
        self.slon.rect = self.slon.image.get_rect()
        self.all_sprites.add(self.slon)
        self.slon.rect.x = 1000
        self.slon.rect.y = 1000

        self.pesh = pygame.sprite.Sprite()  # пешка
        self.pesh.image = load_image('white_pawn.png', -1)
        self.pesh.rect = self.pesh.image.get_rect()
        self.all_sprites.add(self.pesh)
        self.pesh.rect.x = 1000
        self.pesh.rect.y = 1000

        self.qween = pygame.sprite.Sprite()  # королева
        self.qween.image = load_image('white_figure.png', -1)
        self.qween.rect = self.qween.image.get_rect()
        self.all_sprites.add(self.qween)
        self.qween.rect.x = 1000
        self.qween.rect.y = 1000

        self.lad2 = pygame.sprite.Sprite()  # ладья
        self.lad2.image = load_image('black_figure.png', -1)
        self.lad2.rect = self.lad2.image.get_rect()
        self.all_sprites.add(self.lad2)
        self.lad2.rect.x = 1000
        self.lad2.rect.y = 1000

        self.kon2 = pygame.sprite.Sprite()  # конь
        self.kon2.image = load_image('black_figure.png', -1)
        self.kon2.rect = self.kon.image.get_rect()
        self.all_sprites.add(self.kon2)
        self.kon2.rect.x = 1000
        self.kon2.rect.y = 1000

        self.slon2 = pygame.sprite.Sprite()  # слон
        self.slon2.image = load_image('black_figure.png', -1)
        self.slon2.rect = self.slon2.image.get_rect()
        self.all_sprites.add(self.slon2)
        self.slon2.rect.x = 1000
        self.slon2.rect.y = 1000

        self.pesh2 = pygame.sprite.Sprite()  # пешка
        self.pesh2.image = load_image('black_pawn.png', -2)
        self.pesh2.rect = self.pesh2.image.get_rect()
        self.all_sprites.add(self.pesh2)
        self.pesh2.rect.x = 1000
        self.pesh2.rect.y = 1000

        self.qween2 = pygame.sprite.Sprite()  # королева
        self.qween2.image = load_image('black_figure.png', -1)
        self.qween2.rect = self.qween2.image.get_rect()
        self.all_sprites.add(self.qween2)
        self.qween2.rect.x = 1000
        self.qween2.rect.y = 1000

        self.korol2 = pygame.sprite.Sprite()  # король
        self.korol2.image = load_image('black_figure.png', -1)
        self.korol2.rect = self.korol2.image.get_rect()
        self.all_sprites.add(self.korol2)
        self.korol2.rect.x = 1000  # отрисововаю все фигуры в одной точке
        self.korol2.rect.y = 1000  # потом просто буду менять координат спрайта

    def reverse(self, cord, screen):
        self.cord = cord
        if not self.NewCord:
            # если не меняем координату то показываем куда можно ходить
            if cord != None:
                y, x = cord
                print(f'x:{x}, y:{y}')
            if self.board[cord[0]][cord[1]] == 5:  # куда может ходить пешка
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                self.hod[cord[0]][cord[1] + 1] = 1
                if cord[1] == 1:
                    self.hod[cord[0]][cord[1] + 2] = 1
            elif self.board[cord[0]][cord[1]] == 5 + 6:  # куда может ходить пешка
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                self.hod[cord[0]][cord[1] - 1] = 1
                if cord[1] == 6:
                    self.hod[cord[0]][cord[1] - 2] = 1
            elif self.board[cord[0]][cord[1]] == 3 + 6:
                # куда может ходить конь
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                print(x, y)
                if x - 2 < 8 and x - 2 >= 0 and y - 1 >= 0 and y - 1 < 8:  # 1
                    self.hod[y - 1][x - 2] = 1
                if x - 2 < 8 and x - 2 >= 0 and y + 1 >= 0 and y + 1 < 8:  # 2
                    self.hod[y + 1][x - 2] = 1
                if x - 1 < 8 and x - 1 >= 0 and y + 2 >= 0 and y + 2 < 8:  # 3
                    self.hod[y + 2][x - 1] = 1
                if x - 1 < 8 and x - 1 >= 0 and y - 2 >= 0 and y - 2 < 8:  # 8
                    self.hod[y - 2][x - 1] = 1
                if x + 1 < 8 and x + 1 >= 0 and y + 2 >= 0 and y + 2 < 8:  # 4
                    self.hod[y + 2][x + 1] = 1
                if x + 2 < 8 and x + 2 >= 0 and y + 1 >= 0 and y + 1 < 8:  # 5
                    self.hod[y + 1][x + 2] = 1
                if x + 2 < 8 and x + 2 >= 0 and y - 1 >= 0 and y - 1 < 8:  # 4
                    self.hod[y - 1][x + 2] = 1
                if x + 1 < 8 and x + 1 >= 0 and y - 2 >= 0 and y - 2 < 8:  # 4
                    self.hod[y - 2][x + 1] = 1
            elif self.board[cord[0]][cord[1]] == 3:
                # куда может ходить конь
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                print(x, y)
                if x - 2 < 8 and x - 2 >= 0 and y - 1 >= 0 and y - 1 < 8:  # 1
                    self.hod[y - 1][x - 2] = 1
                if x - 2 < 8 and x - 2 >= 0 and y + 1 >= 0 and y + 1 < 8:  # 2
                    self.hod[y + 1][x - 2] = 1
                if x - 1 < 8 and x - 1 >= 0 and y + 2 >= 0 and y + 2 < 8:  # 3
                    self.hod[y + 2][x - 1] = 1
                if x - 1 < 8 and x - 1 >= 0 and y - 2 >= 0 and y - 2 < 8:  # 8
                    self.hod[y - 2][x - 1] = 1
                if x + 1 < 8 and x + 1 >= 0 and y + 2 >= 0 and y + 2 < 8:  # 4
                    self.hod[y + 2][x + 1] = 1
                if x + 2 < 8 and x + 2 >= 0 and y + 1 >= 0 and y + 1 < 8:  # 5
                    self.hod[y + 1][x + 2] = 1
                if x + 2 < 8 and x + 2 >= 0 and y - 1 >= 0 and y - 1 < 8:  # 4
                    self.hod[y - 1][x + 2] = 1
                if x + 1 < 8 and x + 1 >= 0 and y - 2 >= 0 and y - 2 < 8:  # 4
                    self.hod[y - 2][x + 1] = 1
            elif self.board[y][x] == 1:
                # куда может ходить король
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                if x - 1 < 8 and x - 1 >= 0 and y >= 0 and y < 8:  # 1
                    self.hod[y][x - 1] = 1
                if x + 1 < 8 and x + 1 >= 0 and y >= 0 and y < 8:  # 1
                    self.hod[y][x + 1] = 1
                if x < 8 and x >= 0 and y - 1 >= 0 and y - 1 < 8:  # 1
                    self.hod[y - 1][x] = 1
                if x < 8 and x >= 0 and y + 1 >= 0 and y + 1 < 8:  # 1
                    self.hod[y + 1][x] = 1
            elif self.board[y][x] == 1 + 6:
                # куда может ходить король
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                if x - 1 < 8 and x - 1 >= 0 and y >= 0 and y < 8:  # 1
                    self.hod[y][x - 1] = 1
                if x + 1 < 8 and x + 1 >= 0 and y >= 0 and y < 8:  # 1
                    self.hod[y][x + 1] = 1
                if x < 8 and x >= 0 and y - 1 >= 0 and y - 1 < 8:  # 1
                    self.hod[y - 1][x] = 1
                if x < 8 and x >= 0 and y + 1 >= 0 and y + 1 < 8:  # 1
                    self.hod[y + 1][x] = 1
            elif self.board[y][x] == 4:
                # куда может ходить слон
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                i, j = x, y
                if i == 0:
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        i += 1
                        j += 1
                        self.hod[j][i] = 1
                        print(f'{j}, {i}')
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        i += 1
                        j -= 1
                        self.hod[j][i] = 1
                    print(self.hod)
                    return None
                while i != 0 and j != 0:
                    i -= 1
                    j -= 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i += 1
                    j += 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i -= 1
                    j += 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i += 1
                    j -= 1
                    self.hod[j][i] = 1
                self.hod[y][x] = 0
            elif self.board[y][x] == 4 + 6:
                # куда может ходить слон
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                i, j = x, y
                if i == 7:
                    i, j = x, y
                    i -= 1
                    j -= 1
                    k = True
                    self.hod[j][i] = 1
                    print(i, j)
                    while i != -1 and j != -1 and i != 7 and j != 7 and k:
                        i -= 1
                        j -= 1
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
                            k = False
                    i, j = x, y
                    i -= 1
                    j += 1
                    k = True
                    self.hod[j][i] = 1
                    print(i, j)
                    while i != -1 and j != -1 and i != 7 and j != 7 and k:
                        i -= 1
                        j += 1
                        self.hod[j][i] = 1
                    # print(self.hod)
                    return None
                while i != 0 and j != 0:
                    i -= 1
                    j -= 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i += 1
                    j += 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i -= 1
                    j += 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i += 1
                    j -= 1
                    self.hod[j][i] = 1
                self.hod[y][x] = 0
            elif self.board[cord[0]][cord[1]] == 2:  # куда может ходить ладья
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                i, j = x, y
                while i != -1 and j != -1 and i != 7 and j != 7:
                    j -= 1
                    print(i)
                    self.hod[j][i] = 1
                    if j == -1:
                        self.hod[j][i] = 0
                i, j = x, y
                while i != -1 and j != -1 and i != 7 and j != 7:
                    j += 1
                    print(i)
                    self.hod[j][i] = 1
                    if j == -1:
                        self.hod[j][i] = 0
                i, j = x, y
                while i != -1 and j != -1 and i != 7 and j != 7:
                    i += 1
                    print(i)
                    self.hod[j][i] = 1
                    if j == -1:
                        self.hod[j][i] = 0
                i, j = x, y
                if i != 0:
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        i -= 1
                        print(i)
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
            elif self.board[cord[0]][cord[1]] == 2 + 6:  # куда может ходить ладья
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                i, j = x, y
                while i != -1 and j != -1 and i != 8 and j != 8:
                    j -= 1
                    self.hod[j][i] = 1
                    if j == -1:
                        self.hod[j][i] = 0
                i, j = x, y
                while i != -1 and j != -1 and i != 8 and j != 8:
                    j += 1
                    if i == 8 or j == 8:
                        pass
                    else:
                        self.hod[j][i] = 1
                i, j = x, y
                while i != -1 and j != -1 and i != 8 and j != 8:
                    i += 1
                    if j == -1:
                        self.hod[j][i] = 0
                    elif i == 8 or j == 8:
                        pass
                    else:
                        self.hod[j][i] = 1
                i, j = x, y
                if i != 0:
                    while i != -1 and j != -1 and i != 8 and j != 8:
                        i -= 1
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
                        elif i == 8 or j == 8:
                            pass
                        else:
                            self.hod[j][i] = 1
                self.hod[y][x] = 0
            # ферзя не доделал
            elif self.board[y][x] == 6:
                # куда может ходить ферзь
                self.hod = [[0] * (self.width) for _ in range(self.height)]
                i, j = x, y

                if i == 0:
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        i += 1
                        j += 1
                        self.hod[j][i] = 1
                        print(f'{j}, {i}')
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        i += 1
                        j -= 1
                        self.hod[j][i] = 1
                    print(self.hod)

                if i == 7:
                    i, j = x, y
                    i -= 1
                    j -= 1
                    k = True
                    self.hod[j][i] = 1
                    print(i, j)
                    while i != -1 and j != -1 and i != 7 and j != 7 and k:
                        i -= 1
                        j -= 1
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
                            k = False
                    i, j = x, y
                    i -= 1
                    j += 1
                    k = True
                    self.hod[j][i] = 1
                    print(i, j)
                    while i != -1 and j != -1 and i != 7 and j != 7 and k:
                        i -= 1
                        j += 1
                        self.hod[j][i] = 1
                    # print(self.hod)
                while i != 0 and j != 0:
                    i -= 1
                    j -= 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i += 1
                    j += 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i -= 1
                    j += 1
                    self.hod[j][i] = 1
                i, j = x, y
                while i != 0 and j != 0 and i != 7 and j != 7:
                    i += 1
                    j -= 1
                    self.hod[j][i] = 1
                if self.board[cord[0]][cord[1]] == 2:  # куда может ходить ладья
                    self.hod = [[0] * (self.width) for _ in range(self.height)]
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        j -= 1
                        print(i)
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        j += 1
                        print(i)
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
                    i, j = x, y
                    while i != -1 and j != -1 and i != 7 and j != 7:
                        i += 1
                        print(i)
                        self.hod[j][i] = 1
                        if j == -1:
                            self.hod[j][i] = 0
                    i, j = x, y
                    if i != 0:
                        while i != -1 and j != -1 and i != 7 and j != 7:
                            i -= 1
                            print(i)
                            self.hod[j][i] = 1
                            if j == -1:
                                self.hod[j][i] = 0
                self.hod[y][x] = 0
            if self.board[cord[0]][cord[1]] != 0:
                self.OldCord = self.cord
                self.NewCord = True

        else:
            # тут будет код замены фигур
            print(cord)
            x = cord[0]
            y = cord[1]
            # меняю клетку куда нажал на значение старой клетки, если что то стояло то оно убираетьсяя из таблицы
            if self.hod[x][y] == 1:
                self.board[x][y] = self.board[self.OldCord[0]][self.OldCord[1]]
                self.board[self.OldCord[0]][self.OldCord[1]] = 0
                # обнуляю старую клетку
            self.hod = [[0] * (self.width) for _ in range(self.height)]
            self.NewCord = False


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        if colorkey == -2:
            colorkey = pygame.Color('blue')
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def dosca(screen):
    kaf = 0
    koard = 100
    x = 0
    y = 0
    screen.fill((30, 30, 30))
    for i in range(8):
        for j in range(8):
            kaf += 1
            if kaf % 2 == 0:
                pygame.draw.polygon(screen, pygame.Color([220, 220, 220]),
                                    [(x, y), (x, y + koard), (x + koard, y + koard), (x + koard, y)])
            x += koard
        y += koard
        if i % 2 == 0:
            x = 0 - koard
        else:
            x = 0


def main(width, height, ot_left, ot_top, gross):  # основная функция
    pygame.init()
    screen = pygame.display.set_mode(window_size)

    board = Board(width, height)
    board.set_view(ot_left, ot_top, gross)
    running = True
    board.figur('1.jpg.png')
    q = 0
    board.boardd()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                q += 1
                x, y = event.pos
                board.reverse(board.how_kw(x, y), screen)

        dosca(screen)
        screen.fill((0, 0, 0))
        dosca(screen)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


window_size = win_width, win_height = 801, 801
pygame.display.set_caption('RFIG')

if __name__ == '__main__':
    main(8, 8, 0, 0, 100)
