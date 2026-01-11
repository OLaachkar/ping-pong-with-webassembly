import pygame
from constants import *
from paddle import *
from ball import *
import asyncio

async def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong RL - Step 1")
    clock = pygame.time.Clock()
    player = Paddle(x=30,y=SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    )
    machine = Paddle(x=850, y=SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    )
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SPEED * random.choice([-1, 1]), BALL_SPEED * random.uniform(-0.5, 0.5), BALL_RADIUS )

    player_score = 0
    machine_score = 0
    fps_timer = 0
    frames = 0
    winner = None
    font = pygame.font.SysFont(None, 48)
    while True:
        dt = clock.tick(60) / 1000.0
        fps_timer += dt
        frames += 1
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if winner is not None:
            draw_winner(screen, winner, font)
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                return
        else:    

            if fps_timer >= 1:
                pygame.display.set_caption(f"Pong RL - FPS: {frames}")
                fps_timer = 0
                frames = 0
            if player_score == 2:
                winner = "PLAYER WON"

            if machine_score ==2:
                winner = "MACHINE WON"
            
            player.update(dt, up_key=keys[pygame.K_w], down_key=keys[pygame.K_s])
            ball.update(dt, player, machine)
            machine.machine_update(dt, ball)
            screen.fill("black")
            if ball.rect.right < 0:
                machine_score += 1
                ball.reset(1)

            elif ball.rect.left > SCREEN_WIDTH:
                player_score += 1
                ball.reset(-1)

            ball.draw(screen)
            player.draw(screen)
            machine.draw(screen)
            score_text = font.render(f"{player_score}  {machine_score}", True, "White")
            screen.blit(score_text, (SCREEN_WIDTH // 2 - 40, 20))
            pygame.display.flip()
            await asyncio.sleep(0)
            
def draw_winner(screen, text, font):
    screen.fill("black")
    winner_text = font.render(text, True, "White")
    rect_winner = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    refresh_text = font.render("refresh to retry!", True, "White")
    rect_refresh = refresh_text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50))
    screen.blit(winner_text, rect_winner)
    screen.blit(refresh_text, rect_refresh)
    pygame.display.flip()

asyncio.run(main())