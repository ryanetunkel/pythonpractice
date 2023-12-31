"""Projectile Class"""
from random import randint, choice

from global_vars import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, type, source):
        super().__init__()

        # Projectiles
        # These might not all be universal, especially damage and speed, will be varied

        # Unused
        self.projectile_speed = 5
        self.projectile_damage = 1

        if type == 'fireball': # Can't currently handle any projectile other than 'fireball'
            # Fireball - Mess with these values and the wizard's casting aniamtion to get good looking animation
            self.fireball_move_animation_speed = 0.4
            self.fireball_transition_animation_speed = 0.4
            
            # Wizard related 
            temp_wizard_rect = source.sprite.get_wizard_rect()
            self.wizard_was_looking_right = source.sprite.get_looking_right()
            self.direction_multiplier = 1 if self.wizard_was_looking_right else -1
            
            # Start position
            self.fireball_x_start = temp_wizard_rect.centerx + ((4 * PIXEL_SIZE) + (WIZARD_WIDTH/2) * self.direction_multiplier)
            self.fireball_y_start = temp_wizard_rect.centery + (6 * PIXEL_SIZE)

            # Position
            self.fireball_x_pos = self.fireball_x_start
            self.fireball_y_pos = self.fireball_y_start

            # Speed
            self.fireball_x_start_speed = 0
            self.fireball_speed = 5
            
            # Gravity
            self.fireball_gravity_when_held = 0

            # Statistics - To Be Implemented
            self.fireball_damage = source.sprite.get_wizard_damage_total()
            self.fireball_piercing = source.sprite.get_wizard_piercing_total()
            
            # Fireball Creation
            self.created = 0

            # Fireball Transition Animation
            fireball_trans_0 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_0.png').convert_alpha()
            fireball_trans_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_1.png').convert_alpha()
            fireball_trans_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_2.png').convert_alpha()
            fireball_trans_3 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_3.png').convert_alpha()
            self.fireball_trans = [fireball_trans_0, fireball_trans_1, fireball_trans_2, fireball_trans_3]

            # Fireball Movement Animation
            fireball_move_0 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_0.png').convert_alpha()
            fireball_move_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_1.png').convert_alpha()
            fireball_move_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_2.png').convert_alpha()
            fireball_move_3 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_3.png').convert_alpha()
            self.fireball_move = [fireball_move_0, fireball_move_1, fireball_move_2, fireball_move_3]

            self.fireball_index = 0
            self.image = self.fireball_trans[self.fireball_index]
            # self.image = pygame.transform.scale_by(self.image,1)
            if not self.wizard_was_looking_right:
                self.image = pygame.transform.flip(self.image,True,False)
            self.rect = self.image.get_rect(center = (self.fireball_x_pos,self.fireball_y_pos)) 
    
    def get_fireball_damage(self):
        return self.fireball_damage
    
    def set_fireball_damage(self):
        return self.fireball_damage
    
    def get_fireball_piercing(self):
        return self.fireball_piercing

    def set_fireball_piercing(self,new_fireball_piercing):
        self.fireball_piercing = new_fireball_piercing
    
    def animation_state(self):
        if self.created < 4:
            self.created += self.fireball_transition_animation_speed
            self.fireball_index += self.fireball_transition_animation_speed
            
            if self.fireball_index >= len(self.fireball_trans): self.fireball_index = 0
            self.image = self.fireball_trans[int(self.fireball_index)]
        else:
            self.fireball_index += self.fireball_move_animation_speed # speed of animation, adjust as needed
            if self.fireball_index >= len(self.fireball_move): self.fireball_index = 0
            
            self.image = self.fireball_move[int(self.fireball_index)]
        # self.image = pygame.transform.scale_by(self.image,1)
        
        if not self.wizard_was_looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
    
    def update(self):
        self.animation_state()
        if self.created >= 4:
            self.rect.x += (self.projectile_speed * self.direction_multiplier)
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100 and not self.wizard_was_looking_right:
            self.kill()
        elif self.rect.x >= WINDOW_WIDTH + 100 and self.wizard_was_looking_right:
            self.kill()