green = 13
red = 12
blue = 14

game_ids = []

with open('day2data.txt', 'r') as f:

    for line in f:
        line_split = line.split(':')
        game_id = line_split[0].split()[1]
        hands_shown = line_split[1].split(';')
        impossible = False

        for hand in hands_shown:
            colours = hand.split(',')
            for colour in colours:
                colour = colour.strip()
                if 'blue' in colour and int(colour.split()[0]) > blue:
                    impossible = True
                    break
                if 'red' in colour and int(colour.split()[0]) > red:
                    impossible = True
                    break
                if 'green' in colour and int(colour.split()[0]) > green:
                    impossible = True
                    break

            if impossible:
                break
            
        
        if not impossible:
            print(line)
            game_ids.append(int(game_id))

print(game_ids)
print(sum(game_ids))

