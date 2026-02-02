"""Solution to Ellen's Alien Game exercise."""

class Alien:
    total_aliens_created = 1

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        return None

def new_aliens_collection(alien_start_positions):
    aliens = []
    for coordinate in alien_start_positions:
        alien = Alien(coordinate[0], coordinate[1])
        aliens.append(alien)
    return aliens
