shapes_score = {'Rock' : 1, 'Paper' : 2, 'Scissors' : 3}
outcome_score = {'Won' : 6, 'Draw' : 3, 'Lost' : 0}

match = {
    'A' : 'Rock',
    'B' : 'Paper',
    'C' : 'Scissors',
    'X' : 'Rock',
    'Y' : 'Paper',
    'Z' : 'Scissors'
}

player_1_score = []
player_2_score = []

def outcome_calculator(input_player_1, input_player_2) :
    global player_1_score, player_2_score
    if input_player_1 == input_player_2 or input_player_2 == input_player_1 :
        player_1_score.append(outcome_score['Draw'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Draw'] + shapes_score[input_player_2])
    elif input_player_1 == 'Rock' and input_player_2 == 'Scissors' :
        player_1_score.append(outcome_score['Won'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Lost'] + shapes_score[input_player_2])
    elif input_player_1 == 'Paper' and input_player_2 == 'Scissors' :
        player_1_score.append(outcome_score['Lost'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Won'] + shapes_score[input_player_2])
    elif input_player_1 == 'Paper' and input_player_2 == 'Rock' :
        player_1_score.append(outcome_score['Won'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Lost'] + shapes_score[input_player_2])
    elif input_player_2 == 'Rock' and input_player_1 == 'Scissors' :
        player_1_score.append(outcome_score['Lost'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Won'] + shapes_score[input_player_2])
    elif input_player_2 == 'Paper' and input_player_1 == 'Scissors' :
        player_1_score.append(outcome_score['Won'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Lost'] + shapes_score[input_player_2])
    elif input_player_2 == 'Paper' and input_player_1 == 'Rock' :
        player_1_score.append(outcome_score['Lost'] + shapes_score[input_player_1])
        player_2_score.append(outcome_score['Won'] + shapes_score[input_player_2]) 

class need_to_follow_instructions :

    def outcome_is_lost(input_player_1) :
        if input_player_1 == 'Rock' :
            player_2_score.append(outcome_score['Lost'] + shapes_score['Scissors'])
        elif input_player_1 == 'Scissors' :
            player_2_score.append(outcome_score['Lost'] + shapes_score['Paper'])
        elif input_player_1 == 'Paper' :
            player_2_score.append(outcome_score['Lost'] + shapes_score['Rock'])
    
    def outcome_is_draw(input_player_1) :
        if input_player_1 == 'Rock' :
            player_2_score.append(outcome_score['Draw'] + shapes_score['Rock'])
        elif input_player_1 == 'Paper' :
            player_2_score.append(outcome_score['Draw'] + shapes_score['Paper'])
        elif input_player_1 == 'Scissors' :
            player_2_score.append(outcome_score['Draw'] + shapes_score['Scissors'])   

    def outcome_is_won(input_player_1) :
        if input_player_1 == 'Rock' :
            player_2_score.append(outcome_score['Won'] + shapes_score['Paper'])
        elif input_player_1 == 'Paper' :
            player_2_score.append(outcome_score['Won'] + shapes_score['Scissors'])
        elif input_player_1 == 'Scissors' :
            player_2_score.append(outcome_score['Won'] + shapes_score['Rock'])   

with open(r"input.txt", "r") as input_file :
    choice = int(input("First part (1) Second part (2)\n"))
    if choice == 1 :
        # First part of the challenge
        for game in input_file :
            player_1_choice, player_2_choice = game.split(' ')
            p1 = player_1_choice
            p2 = player_2_choice.replace('\r', '').replace('\n', '')
            outcome_calculator(input_player_1=match[p1], input_player_2=match[p2])
        print ("Results of the first challenge : ")
        print ("Player 1 total score is {0}".format(sum(player_1_score)))
        print ("Player 2 total score is {0}".format(sum(player_2_score)))
        # Second part of the challenge
    elif choice == 2 :
        for game in input_file :
            player_1_choice, player_2_choice = game.split(' ')
            p1 = player_1_choice
            p2 = player_2_choice.replace('\r', '').replace('\n', '')
            if p2 == 'X' : # Lose
                need_to_follow_instructions.outcome_is_lost(input_player_1=match[p1])
            elif p2 == 'Y' : # Draw
                need_to_follow_instructions.outcome_is_draw(input_player_1=match[p1])
            elif p2 == 'Z' : # Win
                need_to_follow_instructions.outcome_is_won(input_player_1=match[p1])
        print ("Results of the second challenge : ")
        print ("Player 2 total score is {0}".format(sum(player_2_score)))
