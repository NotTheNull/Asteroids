import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    #Checks if self and entity are colliding
    #collision is defined as the distance being less than the sum of both radii
    #entity: CircleShape
    def check_collision(self, entity):
        actual_distance = pygame.math.Vector2.distance_to(self.position, entity.position)
        min_safe_distance = self.radius + entity.radius
        return actual_distance <= min_safe_distance
