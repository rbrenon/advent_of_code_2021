class Player():
    def __init__(self, position=0):
        self.position = position
        self.score = 0
        self.rolls = 0


def main():
    player_1 = Player(8)
    player_2 = Player(1)
    die_value = 0
    continue_rolling = True

    while player_1.score < 1000 and player_2.score < 1000:
        if not continue_rolling:
            break
        else:
            for player in [player_1, player_2]:
                if not continue_rolling:
                    break
                else:
                    roll_score = 0
                    for roll in range(1, 4):
                        die_value += 1
                        player.rolls += 1
                        roll_score += die_value

                    player.position = 10 if (player.position + roll_score) % 10 == 0 else (player.position + roll_score) % 10
                    player.score += player.position
                    if player.score >= 1000:
                        continue_rolling = False

        print(f"player 1: pos={player_1.position}, score={player_1.score}, roll count={player_1.rolls}, player 2: pos={player_2.position}, score={player_2.score}, roll count={player_2.rolls}")

    print(min(player_1.score, player_2.score) * (player_1.rolls + player_2.rolls))


if __name__ == "__main__":
    main()
