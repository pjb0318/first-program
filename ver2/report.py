import pygame
import random
import sys

pygame.init()

# 초기좌표
to_x = 0
to_y = 0

# 프레임
clock = pygame.time.Clock()

bomb_speed = 13

# 화면 크기 설정
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("직업윤리 보고서")

# 이미지
background = pygame.image.load("./image/background.png")
character_main = pygame.image.load("./image/character_main.png")
startim = pygame.image.load("./image/start.png")
stage1 = pygame.image.load("./image/stage1.png")
stage2 = pygame.image.load("./image/stage2.png")

bomb = pygame.image.load("./image/drop.png")
bomb2 = pygame.image.load("./image/drop2.png")

minigame_background = pygame.image.load("./image/minigame_background.png")

character_main_size = character_main.get_rect().size
character_main_width = character_main_size[0]
character_main_height = character_main_size[1]
character_main_x_pos = (WIDTH / 2) - character_main_width
character_main_y_pos = HEIGHT - character_main_height + 100

player_speed = 10

test_image = pygame.image.load("./image/test.png")

door_im1 = pygame.image.load("./image/door1.png")
door_im2 = pygame.image.load("./image/door2.png")
door_im3 = pygame.image.load("./image/door3.png")
door_im4 = pygame.image.load("./image/door4.png")

door_clear1 = pygame.image.load("./image/clear1.png")
door_clear2 = pygame.image.load("./image/clear2.png")
door_clear3 = pygame.image.load("./image/clear3.png")
door_clear4 = pygame.image.load("./image/clear4.png")

button = pygame.image.load("./image/button.png")

donggi = pygame.image.load("./image/donggi.png")
donggi1 = pygame.image.load("./image/donggi1.png")
donggi2 = pygame.image.load("./image/donggi2.png")
donggi3 = pygame.image.load("./image/donggi3.png")
donggi4 = pygame.image.load("./image/donggi4.png")

text_job = pygame.image.load("./image/text_job.png")
feature = pygame.image.load("./image/feature.png")
feature2 = pygame.image.load("./image/feature2.png")

ethics = pygame.image.load("./image/ethics.png")
what_ethics = pygame.image.load("./image/what_ethics.png")

# 사운드
start_sound = pygame.mixer.Sound("./music/start_sound.wav")
door_open = pygame.mixer.Sound("./music/door_open.wav")
button_sound = pygame.mixer.Sound("./music/button_sound.mp3")
pass_not = pygame.mixer.Sound("./music/youcantpass.mp3")

avoid_bomb = 0

long = pygame.image.load("./image/long.png")
long_size = long.get_rect().size
long_width = long_size[0]
long_height = long_size[1]
long_x_pos = (WIDTH / 2) - long_width
long_y_pos = 150

to_x_l = 0
to_y_1 = 0

# 문 유무
door1 = 1
door2 = 1
door3 = 1
door4 = 1

# 출입 자격
door1_enter = 1
door2_enter = 0
door3_enter = 0
door4_enter = 0

stage = 0

job = 0

dong = 0

bomb_size = bomb.get_rect().size
bomb_width = bomb_size[0]
bomb_height = bomb_size[1]

bomb2_size = bomb2.get_rect().size
bomb2_width = bomb2_size[0]
bomb2_height = bomb2_size[1]

bomb_x_pos = random.randint(0, (WIDTH - character_main_width))
bomb_y_pos = 0

bomb2_x_pos = random.randint(0, (WIDTH - character_main_width))
bomb2_y_pos = 0

MENUCLEAR = 0
RUN = True

game = 0

while RUN:
    dt = clock.tick(60)

    # 프레임 체크용
    #  data = str(clock.get_fps())
    #  print("FPS : " + data)

    if stage == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= 10
                elif event.key == pygame.K_RIGHT:
                    to_x += 10
                elif event.key == pygame.K_UP:
                    to_y -= 10
                elif event.key == pygame.K_DOWN:
                    to_y += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

        character_main_x_pos += to_x
        character_main_y_pos += to_y

        # 나가지마렴
        if character_main_x_pos < 0:
            character_main_x_pos = 0
        elif character_main_x_pos > WIDTH - character_main_width:
            character_main_x_pos = WIDTH - character_main_width

        if character_main_y_pos < 0:
            character_main_y_pos = 0
        elif character_main_y_pos > HEIGHT - character_main_height:
            character_main_y_pos = HEIGHT - character_main_height

        screen.blit(background, (0, 0))
        screen.blit(startim, (400, 400))
        screen.blit(character_main, (character_main_x_pos, character_main_y_pos))

        # 충돌 감지
        if (750 > character_main_x_pos > 300) and (525 > character_main_y_pos > 400):
            MENUCLEAR = 1
            stage = 1
            character_main_x_pos = (WIDTH / 2) - character_main_width
            character_main_y_pos = HEIGHT - character_main_height + 200
            start_sound.play()

    if stage == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= 10
                elif event.key == pygame.K_RIGHT:
                    to_x += 10
                elif event.key == pygame.K_UP:
                    to_y -= 10
                elif event.key == pygame.K_DOWN:
                    to_y += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0
        # 나가지마렴
        if character_main_x_pos < 0:
            character_main_x_pos = 0
        elif character_main_x_pos > WIDTH - character_main_width:
            character_main_x_pos = WIDTH - character_main_width

        if character_main_y_pos < 0:
            character_main_y_pos = 0
        elif character_main_y_pos > HEIGHT - character_main_height:
            character_main_y_pos = HEIGHT - character_main_height

        character_main_x_pos += to_x
        character_main_y_pos += to_y

        if MENUCLEAR == 1:
            screen.blit(stage1, (0, 0))
            # 문1
            if door1 == 1:
                screen.blit(door_im1, (250, 150))
            elif door1 == 0:
                screen.blit(door_clear1, (250, 150))
            # 문2
            if door2 == 1:
                screen.blit(door_im2, (450, 150))
            elif door2 == 0:
                screen.blit(door_clear2, (450, 150))
            # 문3
            if door3 == 1:
                screen.blit(door_im3, (650, 150))
            elif door3 == 0:
                screen.blit(door_clear3, (650, 150))
            # 문4
            if door4 == 1:
                screen.blit(door_im4, (850, 150))
            elif door4 == 0:
                screen.blit(door_clear4, (850, 150))

            # 문 출입
            if (400 > character_main_x_pos > 250) and (
                    400 > character_main_y_pos > 100) and door1_enter == 1 and door1 == 1:
                MENUCLEAR = 0
                stage = 2
                character_main_x_pos = (WIDTH / 2) - character_main_width
                character_main_y_pos = HEIGHT - character_main_height
                door_open.play()
                door1 = 0
                door2_enter = 1

            if (500 > character_main_x_pos > 350) and (
                    400 > character_main_y_pos > 100) and door2_enter == 1 and door2 == 1:
                MENUCLEAR = 0
                stage = 3
                character_main_x_pos = (WIDTH / 2) - character_main_width
                character_main_y_pos = HEIGHT - character_main_height
                door_open.play()
                door2 = 0
                door3_enter = 1
                to_y = 0

            if (700 > character_main_x_pos > 650) and (
                    400 > character_main_y_pos > 100) and door3_enter == 1 and door3 == 1:
                MENUCLEAR = 0
                stage = 4
                character_main_x_pos = (WIDTH / 2) - character_main_width
                character_main_y_pos = HEIGHT - character_main_height
                door_open.play()
                game = 1

            if (950 > character_main_x_pos > 800) and (
                    400 > character_main_y_pos > 100) and door4_enter == 1 and door4 == 1:
                MENUCLEAR = 0
                stage = 5
                character_main_x_pos = (WIDTH / 2) - character_main_width
                character_main_y_pos = HEIGHT - character_main_height
                door_open.play()

            screen.blit(character_main, (character_main_x_pos, character_main_y_pos))

    if stage == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= 10
                elif event.key == pygame.K_RIGHT:
                    to_x += 10
                elif event.key == pygame.K_UP:
                    to_y -= 10
                elif event.key == pygame.K_DOWN:
                    to_y += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

        # 나가지마렴
        if character_main_x_pos < 0:
            character_main_x_pos = 0
        elif character_main_x_pos > WIDTH - character_main_width:
            character_main_x_pos = WIDTH - character_main_width

        if character_main_y_pos < 0:
            character_main_y_pos = 0
        elif character_main_y_pos > HEIGHT - character_main_height:
            character_main_y_pos = HEIGHT - character_main_height

        character_main_x_pos += to_x
        character_main_y_pos += to_y

        screen.blit(stage2, (0, 0))

        if dong == 0:
            screen.blit(donggi, (((WIDTH / 2) - 400), 40))
        elif dong == 1:
            screen.blit(donggi1, (((WIDTH / 2) - 400), 40))
        elif dong == 2:
            screen.blit(donggi2, (((WIDTH / 2) - 400), 40))
        elif dong == 3:
            screen.blit(donggi3, (((WIDTH / 2) - 400), 40))
        elif dong == 4:
            screen.blit(donggi4, (((WIDTH / 2) - 400), 40))

        screen.blit(button, (900, 580))
        screen.blit(character_main, (character_main_x_pos, character_main_y_pos))

        if (940 > character_main_x_pos > 850) and (
                630 > character_main_y_pos > 500):
            button_sound.play()
            character_main_x_pos = (WIDTH / 2) - character_main_width
            character_main_y_pos = (HEIGHT - character_main_height)
            dong += 1

        if dong > 5:
            MENUCLEAR = 1
            stage = 1
            character_main_x_pos = (WIDTH / 2) - character_main_width
            character_main_y_pos = HEIGHT - character_main_height
            to_x = 0

    if stage == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    job -= 1
                elif event.key == pygame.K_RIGHT:
                    job += 1

        if job < 0:
            job = 0
        screen.blit(stage2, (0, 0))
        screen.blit(text_job, (20, 10))

        if 3 > job >= 1:
            screen.blit(feature, (420, 10))

        if job == 2:
            screen.blit(feature2, (130, 130))

        if job >= 3:
            screen.blit(ethics, (420, 10))

        if job == 4:
            screen.blit(what_ethics, (130, 140))

        if job == 5:
            screen.blit(long, ((100, 100)))

        # 임시로 해놓음
        if job == 7:
            MENUCLEAR = 1
            stage = 1

    if stage == 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= player_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += player_speed
                elif event.key == pygame.K_UP:
                    to_y -= 10
                elif event.key == pygame.K_DOWN:
                    to_y += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0
        # 나가지마렴
        if character_main_x_pos < 0:
            character_main_x_pos = 0
        elif character_main_x_pos > WIDTH - character_main_width:
            character_main_x_pos = WIDTH - character_main_width

        character_main_x_pos += to_x
        character_main_y_pos += to_y

        if game == 1:
            bomb_y_pos += bomb_speed
            bomb2_y_pos += bomb_speed

            if character_main_y_pos < 620:
                character_main_y_pos = 520
            elif character_main_y_pos > 520:
                character_main_y_pos = 520

            character_main_rect = character_main.get_rect()
            character_main_rect.left = character_main_x_pos
            character_main_rect.top = character_main_y_pos

            bomb_rect = bomb.get_rect()
            bomb_rect.left = bomb_x_pos
            bomb_rect.top = bomb_y_pos

            bomb2_rect = bomb2.get_rect()
            bomb2_rect.left = bomb2_x_pos
            bomb2_rect.top = bomb2_y_pos

            if bomb_y_pos > HEIGHT:
                bomb_x_pos = random.randint(0, (WIDTH - character_main_width))
                bomb_y_pos = 0
                avoid_bomb += 1
                player_speed += 0.5
                bomb_speed += 0.2

            if bomb2_y_pos > HEIGHT:
                bomb2_x_pos = random.randint(0, (WIDTH - character_main_width))
                bomb2_y_pos = 0

            if character_main_rect.colliderect(bomb_rect):
                if avoid_bomb > 0:
                    MENUCLEAR = 1
                    stage = 1
                    character_main_x_pos = (WIDTH / 2) - character_main_width
                    character_main_y_pos = HEIGHT - character_main_height
                    pass_not.play()
                    bomb_x_pos = random.randint(0, (WIDTH - character_main_width))
                    avoid_bomb = 0
                    bomb_speed = 13
                    player_speed = 10

            if character_main_rect.colliderect(bomb2_rect):
                if avoid_bomb > 0:
                    MENUCLEAR = 1
                    stage = 1
                    character_main_x_pos = (WIDTH / 2) - character_main_width
                    character_main_y_pos = HEIGHT - character_main_height
                    pass_not.play()
                    bomb_x_pos = random.randint(0, (WIDTH - character_main_width))
                    avoid_bomb = 0
                    bomb_speed = 13
                    player_speed = 10

                #   door3 = 0
                #   door4_enter = 1
            if avoid_bomb == 21:
                game = 2
                player_speed = 10

            screen.blit(minigame_background, (0, 0))
            screen.blit(character_main, (character_main_x_pos, character_main_y_pos))
            screen.blit(bomb, (bomb_x_pos, bomb_y_pos))
            screen.blit(bomb2, (bomb2_x_pos, bomb2_y_pos))
            print(avoid_bomb)

        if game == 2:
            if character_main_y_pos < 0:
                character_main_y_pos = 0
            elif character_main_y_pos > HEIGHT - character_main_height:
                character_main_y_pos = HEIGHT - character_main_height
            screen.blit(test_image, (0, 0))
            screen.blit(character_main, (character_main_x_pos, character_main_y_pos))

    ##그 어디까지 했냐면요, 엄청 긴 윤리내용 사진까지 넣었고 그 다음에 뭐지 또 x,y 좌표 설정햇고... 그 다음에 이제 뭐해야하면
    ##그 이동하는거 넣어야댐 키보드 조작해서 to_x_l이랑 y 해가지고 하면 될듯 ㅎㅇㅌ

    pygame.display.update()

pygame.quit()
