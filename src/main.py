import pygame
import sys

def main():
    pygame.init()

    # Windows setup
    width, height = 800,600
    screen = pygame.display.set_mode((width, height)) # Create a window of specified width and height
    pygame.display.set_caption("Rogue-like Game")

    # Set a background color (RGB)
    background_color = (10, 10, 10)  # Dark gray background

    # Player setup
    player = pygame.Rect(50, 50, 20, 20)  # Player represented as a rectangle
    player.center = (width // 2, height // 2) # Start the player in the center of the screen
    speed = 5  # Player movement speed

    clock = pygame.time.Clock() # Create a clock object to control the frame rate

    while True:
        # Fill the screen with background color
        screen.fill(background_color)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # Detect key presses for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.left > 0:  # Move left if 'A' is pressed and player is within the left boundary
            player.x -= speed
        if keys[pygame.K_d] and player.right < width:  # Move right if 'D' is pressed and player is within the right boundary
            player.x += speed
        if keys[pygame.K_w] and player.top > 0:  # Move up if 'W' is pressed and player is within the top boundary
            player.y -= speed
        if keys[pygame.K_s] and player.bottom < height:  # Move down if 'S' is pressed and player is within the bottom boundary
            player.y += speed

        # Draw the player
        pygame.draw.rect(screen, (125, 0, 0), player)

        pygame.display.flip()  # Update the display
        clock.tick(90)  # Limit to 60 frames per second


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)