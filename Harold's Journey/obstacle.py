"""Obstacle Class"""
from random import randint, choice

from global_vars import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, time_at_spawn):
        super().__init__()
        
        self.ROUND_DIFFICULTY_INCREASE_INCREMENT = 20 # frequency in seconds the difficulty increases
        self.time_scalar = int(time_at_spawn / self.ROUND_DIFFICULTY_INCREASE_INCREMENT) + 1 # Should mean every 20 seconds goes up by 1 
        
        self.enemy_looking_right = False

        self.skeleton_walk_animation_speed =  0.32 # Changed, won't work in current implementation but will in new ones 
        self.bird_fly_animation_speed = 0.2
        
        # Skeleton Base Stats
        self.skeleton_value = 2
        self.skeleton_health = 1
        self.skeleton_speed = 2
        self.skeleton_damage = 1
        
        # Flying Enemy Base Stats
        self.bird_value = 5
        self.bird_health = 1
        self.bird_speed = 2
        self.bird_damage = 1
        
        self.immunity = False
        self.IMMUNITY_LIMIT = 50
        self.immunity_timer = 0 # will need to eventually track what fireball id hit it 

        if randint(0,1) == 1:
            self.x_pos = randint(WINDOW_WIDTH + 100,WINDOW_WIDTH + 300)
            self.enemy_looking_right = False
        else:
            self.x_pos = randint(-300,-100)
            self.enemy_looking_right = True

        if type == 'skeleton':
            self.points = self.skeleton_value
            self.health = self.skeleton_health * self.time_scalar
            self.damage = self.skeleton_damage * self.time_scalar
            self.y_pos = GRASS_TOP_Y
            self.obstacle_speed = self.skeleton_speed
            self.obstacle_animation_speed = self.skeleton_walk_animation_speed

            # Skeleton Walk Animation
            skeleton_walk_00 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png').convert_alpha()
            skeleton_walk_01 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_01.png').convert_alpha()
            skeleton_walk_02 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_02.png').convert_alpha()
            skeleton_walk_03 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_03.png').convert_alpha()
            skeleton_walk_04 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_04.png').convert_alpha()
            skeleton_walk_05 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_05.png').convert_alpha()
            skeleton_walk_06 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_06.png').convert_alpha()
            skeleton_walk_07 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_07.png').convert_alpha()
            skeleton_walk_08 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_08.png').convert_alpha()
            skeleton_walk_09 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_09.png').convert_alpha()
            skeleton_walk_10 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_10.png').convert_alpha()
            skeleton_walk_11 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_11.png').convert_alpha()
            skeleton_walk_12 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_12.png').convert_alpha()
            self.frames = [skeleton_walk_00, skeleton_walk_01, skeleton_walk_02, skeleton_walk_03,
                            skeleton_walk_04, skeleton_walk_05, skeleton_walk_06, skeleton_walk_07,
                            skeleton_walk_08, skeleton_walk_09, skeleton_walk_10, skeleton_walk_11,
                            skeleton_walk_12]
            # Sounds
            self.move_sound = pygame.mixer.Sound('Harold\'s Journey/audio/FreeSFX/GameSFX/FootStep/Retro FootStep Gravel 01.wav')
            self.move_sound.set_volume(OBSTACLE_MOVE_VOLUME)
            self.move_limit = 60
            self.move_timer = self.move_limit
        elif type == 'bird':
            self.points = self.bird_value 
            self.health = self.bird_health * self.time_scalar
            self.damage = self.skeleton_damage * self.time_scalar
            
            self.y_pos = GRASS_TOP_Y - (WIZARD_HEIGHT + (WIZARD_HEIGHT / 4))
            self.obstacle_speed = self.bird_speed
            self.obstacle_animation_speed = self.bird_fly_animation_speed
            
            # Placeholders
            bird_fly_00 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_00.png')
            bird_fly_01 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_01.png')
            bird_fly_02 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_02.png')
            bird_fly_03 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_03.png')
            bird_fly_04 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_04.png')
            bird_fly_05 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_05.png')
            bird_fly_06 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_06.png')
            bird_fly_07 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_07.png')
            bird_fly_08 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_08.png')
            bird_fly_09 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_09.png')
            bird_fly_10 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_10.png')
            bird_fly_11 = pygame.image.load('Harold\'s Journey/graphics/enemies/bird/bird_fly_animation/bird_fly_11.png')
            self.frames = [bird_fly_00, bird_fly_01, bird_fly_02, bird_fly_03,
                           bird_fly_04, bird_fly_05, bird_fly_06, bird_fly_07,
                           bird_fly_08, bird_fly_09, bird_fly_10, bird_fly_11]
            
            # Sounds
            self.move_sound = pygame.mixer.Sound('Harold\'s Journey/audio/FreeSFX/GameSFX/Swoosh/Retro Swooosh 07.wav')
            self.move_sound.set_volume(OBSTACLE_MOVE_VOLUME)
            self.move_limit = 60
            self.move_timer = self.move_limit

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))
        self.direction_multiplier = 1 if self.enemy_looking_right else -1
    
    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos
    
    def get_obstacle_rect(self):
        return self.rect
    
    def get_health(self):
        return self.health
    
    def set_health(self, new_health):
        self.health = new_health
        
    def get_points(self):
        return self.points
    
    def get_immunity(self):
        return self.immunity
    
    def set_immunity(self,new_immunity):
        self.immunity = new_immunity
    
    def get_immunity_limit(self):
        return self.IMMUNITY_LIMIT
    
    def get_immunity_timer(self):
        return self.immunity_timer

    def set_immunity_timer(self,new_immunity_timer):
        self.immunity_timer = new_immunity_timer
    
    def calculate_immunity(self):
        temp_immunity_timer = self.get_immunity_timer()
        if temp_immunity_timer > 0:
            self.set_immunity(True)
            self.set_immunity_timer(temp_immunity_timer - 1)
        else:
            self.set_immunity(False)
            
    def get_points(self):
        return self.points
    
    def set_points(self,new_points):
        self.points = new_points
    
    def animation_state(self):
        self.animation_index += self.obstacle_animation_speed
        if self.animation_index >= len(self.frames): self.animation_index = 0
        
        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        
        if self.enemy_looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
        
        if self.move_timer >= self.move_limit:
            pygame.mixer.Channel(OBSTACLE_MOVE_CHANNEL).play(self.move_sound)
            self.move_timer = 0
        self.move_timer += 1

    def update(self):
        self.animation_state()
        self.rect.x += (self.obstacle_speed * self.direction_multiplier)
        self.calculate_immunity()
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100 and not self.enemy_looking_right:
            self.kill()
        if self.rect.x >= WINDOW_WIDTH + 100 and self.enemy_looking_right:
            self.kill()