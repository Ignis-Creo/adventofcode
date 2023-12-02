green = 13
red = 12
blue = 14

game_ids = []

with open('day2data.txt', 'r') as f:

    for line in f:
        line_split = line.split(':')
        game_id = line_split[0].split()[1]
        hands_shown = line_split[1].split(';')
        max_red = 0
        max_green = 0
        max_blue = 0

        for hand in hands_shown:
            colours = hand.split(',')

            for colour in colours:
                colour = colour.strip()
                number = int(colour.split()[0]) 

                if 'blue' in colour:
                        max_blue = number if max_blue < number else max_blue

                if 'red' in colour :
                        max_red = number if max_red < number else max_red
                    
                if 'green' in colour:
                        max_green= number if max_green < number else max_green
                    
        game_ids.append(max_green * max_blue * max_red)

print(game_ids)
print(sum(game_ids))

