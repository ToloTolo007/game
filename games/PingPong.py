import pygame
import random

# Initiate pygame
pygame.init()

# Screen width & height
WIDTH = 800
HEIGHT = 600
# Players width & height
playerWidth = 25
playerHeight = 110

# Left player starting position & rect
player1_posX = 30
player1_posY = 225
player1Rect = pygame.Rect(player1_posX, player1_posY, playerWidth, playerHeight)

# Right player starting position & rect
player2_posX = 740
player2_posY = 225
player2Rect = pygame.Rect(player2_posX, player2_posY, playerWidth, playerHeight)

# ball size, starting pos & speed
RADIUS = 12
ballPos = [390, 290]
ballSpeed = 4

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PingPong by Lee")

# Randomize ball starting movement
ops = ["+", "-"]
choice1 = random.choice(ops)
choice2 = random.choice(ops)


class Player:
    def __init__(self, color, rect):
        self.rect = rect
        self.color = color
        self.collideUp = False
        self.collideDown = False

    def move_up(self):
        """Move up"""
        if not self.collideUp:
            self.rect.y -= 35

    def move_down(self):
        """Move down"""
        if not self.collideDown:
            self.rect.y += 35

    def collision(self):
        """Collision detection when hit screen border"""
        # Hit bottom
        if self.rect.bottom >= HEIGHT:
            self.collideDown = True
        else:
            self.collideDown = False
        # Hit top
        if self.rect.top <= 0:
            self.collideUp = True
        else:
            self.collideUp = False

    def draw_player(self, surface):
        """Draw players"""
        pygame.draw.rect(surface, self.color, self.rect)


class Ball:
    def __init__(self, pos, color, radius):
        self.pos = pos
        self.color = color
        self.radius = radius
        self.collideTop = False
        self.collideLeft = False
        self.collideBottom = False
        self.collideRight = False
        self.collisionList = []
        self.lupdownList = []
        self.rupdownList = []
        self.out = False
        self.chosen = []

    def draw_ball(self, surface):
        """Draw ball"""
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def move(self):
        """Ball movement"""
        # Hit top of the screen
        if self.collideTop:
            # Check to see which direction to move
            if not self.collisionList:
                self.pos[0] -= ballSpeed
                self.pos[1] += ballSpeed
            elif self.collisionList[-1] == "left":
                self.pos[0] += ballSpeed
                self.pos[1] += ballSpeed
            else:
                self.pos[0] -= ballSpeed
                self.pos[1] += ballSpeed

        # Hit bottom of the screen
        elif self.collideBottom:
            # Check to see which direction to move
            if not self.collisionList:
                self.pos[0] += ballSpeed
                self.pos[1] -= ballSpeed
            elif self.collisionList[-1] == "left":
                self.pos[0] += ballSpeed
                self.pos[1] -= ballSpeed
            else:
                self.pos[0] -= ballSpeed
                self.pos[1] -= ballSpeed

        # Hit left player
        elif self.collideLeft:
            upper = (player1.rect.y + playerHeight) // 2
            lower = player1.rect.y + playerHeight
            # Hit upper right player ball move up
            if player1.rect.y <= self.pos[1] <= upper:
                self.pos[0] += ballSpeed
                self.pos[1] -= ballSpeed
                self.lupdownList.append("up")
            # Hit lower right player ball move down
            elif upper < self.pos[1] <= lower:
                self.pos[0] += ballSpeed
                self.pos[1] += ballSpeed
                self.lupdownList.append("low")
            # Continue the movement after hitting
            else:
                if self.lupdownList[-1] == "up":
                    self.pos[0] += ballSpeed
                    self.pos[1] -= ballSpeed
                else:
                    self.pos[0] += ballSpeed
                    self.pos[1] += ballSpeed

        # Hit right player
        elif self.collideRight:
            upper = (player2.rect.y + playerHeight) // 2
            lower = player2.rect.y + playerHeight
            # Hit upper right player ball move up
            if player2.rect.y <= self.pos[1] <= upper:
                self.pos[0] -= ballSpeed
                self.pos[1] -= ballSpeed
                self.rupdownList.append("up")
            # Hit lower right player ball move down
            elif upper < self.pos[1] <= lower:
                self.pos[0] -= ballSpeed
                self.pos[1] += ballSpeed
                self.rupdownList.append("low")
            # Continue the movement after hitting
            else:
                if self.rupdownList[-1] == "up":
                    self.pos[0] -= ballSpeed
                    self.pos[1] -= ballSpeed
                else:
                    self.pos[0] -= ballSpeed
                    self.pos[1] += ballSpeed

        # Start movement
        else:
            # Choose movement from randomizer
            if choice1 == "+":
                self.pos[0] += ballSpeed
            else:
                self.pos[0] -= ballSpeed

            if choice2 == "+":
                self.pos[1] += ballSpeed
            else:
                self.pos[1] -= ballSpeed
            self.chosen.append(choice1)
            self.chosen.append(choice2)

            # After choosing keep moving or else it stops
            if self.chosen[0] == "+":
                self.pos[0] += ballSpeed
            else:
                self.pos[0] -= ballSpeed

            if self.chosen[1] == "+":
                self.pos[1] += ballSpeed
            else:
                self.pos[1] -= ballSpeed

            # Track ball movement to make ball move in one direction
            if "+" not in self.chosen:
                self.collisionList.append("right")
            elif "-" not in self.chosen:
                self.collisionList.append("left")
            elif self.chosen[0] == "+" and self.chosen[1] == "-":
                self.collisionList.append("left")
            elif self.chosen[0] == "-" and self.chosen[1] == "+":
                self.collisionList.append("right")

    def collision(self):
        """Collision detection"""
        # Hit top screen
        if self.pos[1] - RADIUS <= 0:
            self.collideTop = True
            self.collideLeft = False
            self.collideBottom = False
            self.collideRight = False

        # Hit left player
        if self.pos[0] - RADIUS <= player1_posX + playerWidth and \
                (player1.rect.y <= self.pos[1] <= player1.rect.y + playerHeight):
            self.collideTop = False
            self.collideLeft = True
            self.collideBottom = False
            self.collideRight = False
            self.collisionList.append("left")

        # Hit bottom screen
        if self.pos[1] + RADIUS >= HEIGHT:
            self.collideTop = False
            self.collideLeft = False
            self.collideBottom = True
            self.collideRight = False

        # Hit right player
        if self.pos[0] + RADIUS >= player2_posX and (player2.rect.y <= self.pos[1] <= player2.rect.y + playerHeight):
            self.collideTop = False
            self.collideLeft = False
            self.collideBottom = False
            self.collideRight = True
            self.collisionList.append("right")

    def lose(self):
        """Game lose detection"""
        if self.pos[0] + RADIUS >= WIDTH or self.pos[0] - RADIUS <= 0:
            self.out = True
        else:
            self.out = False


# Initialize players & ball
player1 = Player(RED, player1Rect)
player2 = Player(BLUE, player2Rect)
ball = Ball(ballPos, GREEN, RADIUS)


def reDrawWin(surface):
    """Update screen everytime players & ball move"""
    surface.fill(BLACK)
    player1.draw_player(surface)
    player2.draw_player(surface)
    ball.draw_ball(surface)
    pygame.display.update()


# Main loop
clock = pygame.time.Clock()
FPS = 70
run = True
while run:

    # Detect if lose game
    ball.lose()
    if ball.out:
        run = False
        # Detect who won
        try:
            if ball.collisionList[-1] == "left":
                print("Player One Win!!!")
            elif ball.collisionList[-1] == "right":
                print("Player Two Win!!!")
        except IndexError:
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # Detect players collision first
            player1.collision()
            player2.collision()
            if event.key == pygame.K_w:
                player1.move_up()
            if event.key == pygame.K_s:
                player1.move_down()
            if event.key == pygame.K_UP:
                player2.move_up()
            if event.key == pygame.K_DOWN:
                player2.move_down()

    reDrawWin(WIN)      # Update screen
    ball.collision()    # Detect ball collision
    ball.move()         # Ball movement
    pygame.display.update()
    clock.tick(FPS)
