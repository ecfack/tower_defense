from tower.attack_strategy import *
import os
import pygame

# obelisk image
OBELISK_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image0.png")), (150, 150))
OBELISK_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image1.png")), (150, 150))
OBELISK_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image2.png")), (150, 150))
OBELISK_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image3.png")), (150, 150))
OBELISK_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image4.png")), (150, 150))
OBELISK_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image5.png")), (150, 150))
OBELISK_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image6.png")), (150, 150))
OBELISK_IMAGE_7 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image7.png")), (150, 150))
OBELISK_IMAGE_8 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image8.png")), (150, 150))
OBELISK_IMAGE_9 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image9.png")), (150, 150))
OBELISK_IMAGE_10 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image10.png")), (150, 150))
OBELISK_IMAGE_11 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image11.png")), (150, 150))
OBELISK_IMAGE_12 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image12.png")), (150, 150))
OBELISK_IMAGE_13 = pygame.transform.scale(pygame.image.load(os.path.join("images", "obelisk_image13.png")), (150, 150))

# moon tower image
MOON_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image0.png")), (200, 200))
MOON_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image1.png")), (200, 200))
MOON_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image2.png")), (200, 200))
MOON_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image3.png")), (200, 200))
MOON_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image4.png")), (200, 200))
MOON_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image5.png")), (200, 200))
MOON_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image6.png")), (200, 200))
MOON_IMAGE_7 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image7.png")), (200, 200))
MOON_IMAGE_8 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image8.png")), (200, 200))
MOON_IMAGE_9 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image9.png")), (200, 200))
MOON_IMAGE_10 = pygame.transform.scale(pygame.image.load(os.path.join("images", "moon_image10.png")), (200, 200))

# red fire tower image
RED_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image29.png")), (300, 300))
RED_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image30.png")), (300, 300))
RED_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image31.png")), (300, 300))
RED_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image32.png")), (300, 300))
RED_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image33.png")), (300, 300))
RED_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image34.png")), (300, 300))
RED_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "red_image35.png")), (300, 300))

# blue fire tower image
BLUE_IMAGE_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image0.png")), (400, 400))
BLUE_IMAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image1.png")), (400, 400))
BLUE_IMAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image2.png")), (400, 400))
BLUE_IMAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image3.png")), (400, 400))
BLUE_IMAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image4.png")), (400, 400))
BLUE_IMAGE_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image5.png")), (400, 400))
BLUE_IMAGE_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "blue_image6.png")), (400, 400))

# vacancy image
PLOT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vacant_lot.png")), (40, 40))


class Vacancy:
    def __init__(self, x, y):
        self.image = PLOT_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int) -> bool:
        """
        :param x: mouse pos x
        :param y: mouse pos y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False


# tower (product)
class Tower:
    """ super class of towers """
    def __init__(self, x: int, y: int, attack_strategy):
        """
        self.sprites: list for animation
        self.current_sprites: counter for each image
        self.max_current_sprites: total image
        self.update_speed: count speed
        self.sprites.append(OBELISK_IMAGE_0): append first image
        """
        self.sprites = []
        self.current_sprites = 0
        self.max_current_sprites = 10
        self.update_speed = 1
        self.sprites.append(OBELISK_IMAGE_0)
        self.image = self.sprites[self.current_sprites]  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.name = ""
        self.intro = ""

        self.level = 0  # level of the tower
        self._range = [100, 110, 120, 130, 140, 150]  # tower attack range
        self._damage = [10, 20, 30, 40, 50, 60]   # tower damage
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.attack_strategy = attack_strategy  # chose an attack strategy (AOE, single attack ....)
        self.attack_strategy_name = ""
        self.value = [100, 140, 200, 300, 380, 460]
        self.price = self.value[self.level]


    @classmethod
    # moon_tower attacks all the enemies
    def moon_tower(cls, x, y):
        moon_tower = cls(x, y, SingleSlowAttack())
        moon_tower.name = "Moon Tower"
        moon_tower.intro = "Moon Tower attacks all enemies."
        moon_tower.attack_strategy_name = "Single Slow Attack"
        moon_tower.sprites = []
        moon_tower.update_speed = 0.2
        moon_tower.max_current_sprites = 10
        moon_tower.sprites.append(MOON_IMAGE_0)
        moon_tower.sprites.append(MOON_IMAGE_1)
        moon_tower.sprites.append(MOON_IMAGE_2)
        moon_tower.sprites.append(MOON_IMAGE_3)
        moon_tower.sprites.append(MOON_IMAGE_4)
        moon_tower.sprites.append(MOON_IMAGE_5)
        moon_tower.sprites.append(MOON_IMAGE_6)
        moon_tower.sprites.append(MOON_IMAGE_7)
        moon_tower.sprites.append(MOON_IMAGE_8)
        moon_tower.sprites.append(MOON_IMAGE_9)
        moon_tower.sprites.append(MOON_IMAGE_10)
        moon_tower._range = [130, 140, 150, 160, 170, 180]
        moon_tower._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
        moon_tower.value = [100, 140, 200, 280, 360, 450]
        return moon_tower

    @classmethod
    # red_fire_tower attacks and inflicts continuous damages on an enemy
    def red_fire_tower(cls, x, y):
        red_fire_tower = cls(x, y, AOE())
        red_fire_tower.name = "Fire Totem"
        red_fire_tower.intro = "Fire Totem attacks multiple enemies."
        red_fire_tower.attack_strategy_name = "AOE"
        red_fire_tower.sprites = []
        red_fire_tower.update_speed = 0.2
        red_fire_tower.max_current_sprites = 6
        red_fire_tower.sprites.append(RED_IMAGE_0)
        red_fire_tower.sprites.append(RED_IMAGE_1)
        red_fire_tower.sprites.append(RED_IMAGE_2)
        red_fire_tower.sprites.append(RED_IMAGE_3)
        red_fire_tower.sprites.append(RED_IMAGE_4)
        red_fire_tower.sprites.append(RED_IMAGE_5)
        red_fire_tower.sprites.append(RED_IMAGE_6)

        red_fire_tower._range = [120, 125, 130, 135, 140, 145]
        red_fire_tower._damage = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
        red_fire_tower.value = [120, 160, 220, 320, 400, 500]
        return red_fire_tower

    @classmethod
    # blue_fire_tower attacks and slows down enemies
    def blue_fire_tower(cls, x, y):
        blue_fire_tower = cls(x, y, AOE())
        blue_fire_tower.name = "Ice Totem"
        blue_fire_tower.intro = "Ice Totem attacks multiple enemies."
        blue_fire_tower.attack_strategy_name = "AOE"
        blue_fire_tower.sprites = []
        blue_fire_tower.update_speed = 0.2
        blue_fire_tower.max_current_sprites = 6
        blue_fire_tower.sprites.append(BLUE_IMAGE_0)
        blue_fire_tower.sprites.append(BLUE_IMAGE_1)
        blue_fire_tower.sprites.append(BLUE_IMAGE_2)
        blue_fire_tower.sprites.append(BLUE_IMAGE_3)
        blue_fire_tower.sprites.append(BLUE_IMAGE_4)
        blue_fire_tower.sprites.append(BLUE_IMAGE_5)
        blue_fire_tower.sprites.append(BLUE_IMAGE_6)

        blue_fire_tower._range = [120, 125, 130, 135, 140, 145]
        blue_fire_tower._damage = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
        blue_fire_tower.value = [120, 160, 220, 320, 400, 500]
        return blue_fire_tower

    @classmethod
    # obelisk_tower attacks an enemy far away
    def obelisk_tower(cls, x, y):
        obelisk_tower = cls(x, y, SnipeAll())
        obelisk_tower.name = "Obelisk Tower"
        obelisk_tower.intro = "Obelisk Tower attacks far."
        obelisk_tower.attack_strategy_name = "Snipe All"
        obelisk_tower.sprites = []
        obelisk_tower.max_current_sprites = 13
        obelisk_tower.update_speed = 0.25
        obelisk_tower.sprites.append(OBELISK_IMAGE_0)
        obelisk_tower.sprites.append(OBELISK_IMAGE_1)
        obelisk_tower.sprites.append(OBELISK_IMAGE_2)
        obelisk_tower.sprites.append(OBELISK_IMAGE_3)
        obelisk_tower.sprites.append(OBELISK_IMAGE_4)
        obelisk_tower.sprites.append(OBELISK_IMAGE_5)
        obelisk_tower.sprites.append(OBELISK_IMAGE_6)
        obelisk_tower.sprites.append(OBELISK_IMAGE_7)
        obelisk_tower.sprites.append(OBELISK_IMAGE_8)
        obelisk_tower.sprites.append(OBELISK_IMAGE_9)
        obelisk_tower.sprites.append(OBELISK_IMAGE_10)
        obelisk_tower.sprites.append(OBELISK_IMAGE_11)
        obelisk_tower.sprites.append(OBELISK_IMAGE_12)
        obelisk_tower.sprites.append(OBELISK_IMAGE_13)

        obelisk_tower._range = [100, 105, 110, 115, 120, 125]  # tower attack range
        obelisk_tower.cd_max_count = 120  # tower damage
        obelisk_tower.value = [120, 140, 200, 280, 360, 400]
        return obelisk_tower

    def update(self):
        self.current_sprites += self.update_speed
        if self.current_sprites >= self.max_current_sprites:
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]

    def attack(self, enemy_group: list):
        # cd
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return
        # syntax: attack_strategy().attack(tower, enemy_group, cd_count)
        # It's something like you hire a "Strategist" to decide how to attack the enemy
        # You can add other ways of attack just by expanding the "attack_strategy.py"
        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

    def get_upgrade_cost(self):
        return self.value[self.level+1] - self.value[self.level]

    def get_cost(self):
        return self.value[self.level]

    @property
    def range(self):
        return self._range[self.level]

    @property
    def damage(self):
        return self._damage[self.level]

    def clicked(self, x: int, y: int) -> bool:
        """
        :param x: mouse pos x
        :param y: mouse pos y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False




