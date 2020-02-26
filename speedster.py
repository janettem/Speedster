import pygame
import random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

win_width = 500
win_height = 500

white = (255, 255, 255)
light_gray = (192, 192, 192)
gray = (128, 128, 128)
red = (255, 0, 0)

car_width = 45
car_height = 75

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Speedster")
clock = pygame.time.Clock()

icon_img = pygame.image.load("media/icon.png")

guide_img = pygame.image.load("media/guide.png")

speedster_img = pygame.image.load("media/speedster.png")
fast_img = pygame.image.load("media/fast.png")
furious_img = pygame.image.load("media/furious.png")
crash_img = pygame.image.load("media/crash.png")
menu_img = pygame.image.load("media/menu.png")
start_img = pygame.image.load("media/start.png")
start_2_img = pygame.image.load("media/start2.png")
credits_img = pygame.image.load("media/credits.png")
credits_2_img = pygame.image.load("media/credits2.png")
quit_img = pygame.image.load("media/quit.png")
quit_2_img = pygame.image.load("media/quit2.png")
mute_img = pygame.image.load("media/mute.png")
mute_2_img = pygame.image.load("media/mute2.png")
volume_img = pygame.image.load("media/volume.png")
volume_2_img = pygame.image.load("media/volume2.png")

background_img = pygame.image.load("media/background.png")
race_car_img = pygame.image.load("media/racecar.png")
car_img = pygame.image.load("media/car.png")
car_2_img = pygame.image.load("media/car2.png")
car_3_img = pygame.image.load("media/car3.png")
crash_large_img = pygame.image.load("media/crashbig.png")
pause_img = pygame.image.load("media/pause.png")
pause_2_img = pygame.image.load("media/pause2.png")

paused_img = pygame.image.load("media/paused.png")
unpause_img = pygame.image.load("media/unpause.png")
unpause_2_img = pygame.image.load("media/unpause2.png")

credits_3_img = pygame.image.load("media/credits3.png")
menu_2_img = pygame.image.load("media/menu2.png")
menu_3_img = pygame.image.load("media/menu3.png")

pygame.display.set_icon(icon_img)

car_honk_sound = pygame.mixer.Sound("media/carhonk.wav")

pygame.mixer.music.load("media/8-Bit-Mayhem.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

pause = False
crash = False


def race_car(x, y):
    win.blit(race_car_img, (x, y))


def car(car_x, car_y):
    win.blit(car_img, (car_x, car_y))


def car_2(car_2_x, car_2_y):
    win.blit(car_img, (car_2_x, car_2_y))


def car_3(car_3_x, car_3_y):
    win.blit(car_2_img, (car_3_x, car_3_y))


def car_4(car_4_x, car_4_y):
    win.blit(car_2_img, (car_4_x, car_4_y))


def car_5(car_5_x, car_5_y):
    win.blit(car_3_img, (car_5_x, car_5_y))


def car_6(car_6_x, car_6_y):
    win.blit(car_3_img, (car_6_x, car_6_y))


def cars_dodged(count):
    message_font = pygame.font.SysFont("Agency FB", 20)
    message_surface = message_font.render("Dodged: " + str(count), True, red)
    win.blit(message_surface, (5, 475))


def message(text, font, text_size, text_color, text_width, text_height):
    message_font = pygame.font.SysFont(font, text_size)
    message_surface = message_font.render(text, True, text_color)

    if text_width != "center" and text_height != "center":
        win.blit(message_surface, (text_width, text_height))

    elif text_width == "center" and text_height != "center":
        message_width = message_surface.get_width()
        win.blit(message_surface, ((win_width - message_width) / 2, text_height))

    else:
        message_rect = message_surface.get_rect(center=(win_width / 2, win_height / 2))
        win.blit(message_surface, message_rect)


def get_high_score():
    high_score_file = open("media/speedsterhighscore.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()

    pygame.draw.rect(win, light_gray, (5, 450, 125, 25))
    message_font = pygame.font.SysFont("Agency FB", 20)
    message_surface = message_font.render("High score: " + str(high_score), True, red)
    win.blit(message_surface, (5, 450))

    return high_score


def save_high_score(new_high_score):
    high_score_file = open("media/speedsterhighscore.txt", "w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()


def crash(dodged):
    crash = True

    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_loop()
                elif event.key == pygame.K_m:
                    game_intro()

        win.blit(crash_large_img, (145, 187.5))

        pygame.draw.rect(win, light_gray, (315, 450, 180, 45))

        button(130, 450, 180, 45, start_img, start_2_img, game_loop)
        button(315, 450, 180, 45, menu_2_img, menu_3_img, game_intro)

        high_score = get_high_score()

        if dodged > high_score:
            save_high_score(dodged)

        pygame.display.update()
        clock.tick(15)


def car_honk():
    pygame.mixer.Sound.play(car_honk_sound)


def button(x, y, w, h, ii, ai, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        win.blit(ai, (x, y))
        if click[0] == 1 and action is not None and action != game_pause:
            action()
        elif click[0] == 1 and action == game_pause:
            global pause
            pause = True
            game_pause()

    else:
        win.blit(ii, (x, y))


def game_guide():
    guide = True

    while guide:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_loop()

        win.fill(gray)

        win.blit(guide_img, (145, 70))

        message("Dodge cars by pressing the arrow keys on your keyboard.", "agencyfb", 25, white, "center", 190)
        message("Also, don't drive outside the road or you'll crash.", "agencyfb", 25, white, "center", 220)

        button(160, 450, 180, 45, start_img, start_2_img, game_loop)

        pygame.display.update()
        clock.tick(15)


def game_credits():
    speedster_credits = True

    while speedster_credits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game_intro()

        win.fill(gray)

        win.blit(credits_3_img, (105, 70))

        message("Game by Janette Metelinen", "agencyfb", 25, white, "center", 190)
        message("Music by Eric Matyas, www.soundimage.org", "agencyfb", 25, white, "center", 220)
        message("Sound effect by Sound Jay, www.soundjay.com", "agencyfb", 25, white, "center", 250)

        button(160, 450, 180, 45, menu_2_img, menu_3_img, game_intro)

        pygame.display.update()
        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


def music_unmute():
    if pygame.mixer.music.set_volume(0):
        pygame.mixer.music.set_volume(1)
    else:
        pass


def music_mute():
    if pygame.mixer.music.set_volume(1):
        pygame.mixer.music.set_volume(0)
    else:
        pass


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_guide()
                elif event.key == pygame.K_c:
                    game_credits()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_m:
                    music_unmute()
                elif event.key == pygame.K_u:
                    music_mute()

        win.fill(gray)

        win.blit(speedster_img, (65, 70))
        win.blit(fast_img, (60, 145))
        win.blit(furious_img, (250, 145))
        win.blit(crash_img, (147.5, 180))
        win.blit(menu_img, (160, 250))

        button(160, 300, 180, 45, start_img, start_2_img, game_guide)
        button(160, 350, 180, 45, credits_img, credits_2_img, game_credits)
        button(160, 400, 180, 45, quit_img, quit_2_img, quit_game)
        button(425, 400, 70, 45, mute_img, mute_2_img, music_unmute)
        button(425, 450, 70, 45, volume_img, volume_2_img, music_mute)

        pygame.display.update()
        clock.tick(15)


def game_unpause():
    global pause
    pause = False


def game_pause():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    game_unpause()

        win.blit(paused_img, (125, 187.5))

        button(130, 450, 180, 45, unpause_img, unpause_2_img, game_unpause)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause

    x = 197
    y = 315

    x_change = 0

    car_x = 77
    car_y = random.randint(-2000, -500)

    car_2_x = 257
    car_2_y = random.randint(-2000, -500)

    car_3_x = 137
    car_3_y = random.randint(-2000, -500)

    car_4_x = 317
    car_4_y = random.randint(-2000, -500)

    car_5_x = 197
    car_5_y = random.randint(-2000, -500)

    car_6_x = 377
    car_6_y = random.randint(-2000, -500)

    cars_speed = 6

    dodged = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change -= 60
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change += 60
                elif event.key == pygame.K_p:
                    pause = True
                    game_pause()
                elif event.key == pygame.K_h:
                    car_honk()

                x += x_change

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 0

        win.blit(background_img, (0, 0))

        car(car_x, car_y)
        car_y += cars_speed

        car_2(car_2_x, car_2_y)
        car_2_y += cars_speed

        car_3(car_3_x, car_3_y)
        car_3_y += cars_speed

        car_4(car_4_x, car_4_y)
        car_4_y += cars_speed

        car_5(car_5_x, car_5_y)
        car_5_y += cars_speed

        car_6(car_6_x, car_6_y)
        car_6_y += cars_speed

        race_car(x, y)
        pygame.draw.rect(win, light_gray, (0, 445, 500, 55))
        cars_dodged(dodged)
        button(315, 450, 180, 45, pause_img, pause_2_img, game_pause)

        if x > 427 - car_width or x < 72:
            crash(dodged)

        if car_y > 445:
            car_y = random.randint(-1500, 0 - car_height)
            car_x = 77
            dodged += 1
            cars_speed += 0.01

        if car_2_y > 445:
            car_2_y = random.randint(-1500, 0 - car_height)
            car_2_x = 257
            dodged += 1
            cars_speed += 0.01

        if car_3_y > 445:
            car_3_y = random.randint(-1500, 0 - car_height)
            car_3_x = 137
            dodged += 1
            cars_speed += 0.01

        if car_4_y > 445:
            car_4_y = random.randint(-1500, 0 - car_height)
            car_4_x = 317
            dodged += 1
            cars_speed += 0.01

        if car_5_y > 445:
            car_5_y = random.randint(-1500, 0 - car_height)
            car_5_x = 197
            dodged += 1
            cars_speed += 0.01

        if car_6_y > 445:
            car_6_y = random.randint(-1500, 0 - car_height)
            car_6_x = 377
            dodged += 1
            cars_speed += 0.01

        if x <= car_x < x + car_width or car_x <= x < car_x + car_width:
            if y <= car_y < y + car_height or car_y <= y < car_y + car_height:
                crash(dodged)

        if x <= car_2_x < x + car_width or car_2_x <= x < car_2_x + car_width:
            if y <= car_2_y < y + car_height or car_2_y <= y < car_2_y + car_height:
                crash(dodged)

        if x <= car_3_x < x + car_width or car_3_x <= x < car_3_x + car_width:
            if y <= car_3_y < y + car_height or car_3_y <= y < car_3_y + car_height:
                crash(dodged)

        if x <= car_4_x < x + car_width or car_4_x <= x < car_4_x + car_width:
            if y <= car_4_y < y + car_height or car_4_y <= y < car_4_y + car_height:
                crash(dodged)

        if x <= car_5_x < x + car_width or car_5_x <= x < car_5_x + car_width:
            if y <= car_5_y < y + car_height or car_5_y <= y < car_5_y + car_height:
                crash(dodged)

        if x <= car_6_x < x + car_width or car_6_x <= x < car_6_x + car_width:
            if y <= car_6_y < y + car_height or car_6_y <= y < car_6_y + car_height:
                crash(dodged)

        pygame.display.update()
        clock.tick(60)


game_intro()
pygame.quit()
quit()
