from config import *

pygame.init()
pygame.display.set_caption(CAPTION)
surface = pygame.display.set_mode(SIZE)
FONT48 = pygame.font.SysFont(None, 48)
road_rect = pygame.Rect(160, 0, NUM_LANES * LANE_WIDTH,  SIZE[1])

