def present_answers(questions, answers):
    num     = 0
    running = True

    while running:
        print(questions[num], '\n', answers[num], '\n')

        num += 1
        if num == len(questions):
            running = False