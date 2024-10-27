from questions import sports_category, indian_gk, programming_questions


def get_attempt_history():
    ATTEMPT_HISTORY = []
    with open("attempts_history.csv", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line.split(",")[1] == "":
                continue
            ATTEMPT_HISTORY.append(
                {
                    "username": line.split(",")[0],
                    "points": int(line.split(",")[1]),
                }
            )
            
    return ATTEMPT_HISTORY


def get_questions():

    import random

    def selecting(l1, l2, l3):
        l = []
        indices = []
        while len(l) < 15:
            index = random.randint(0, len(l1) - 1)
            if index not in indices:
                l.append(l1[index])
                l.append(l2[index])
                l.append(l3[index])
                indices.append(index)
        random.shuffle(l)

        return l

    return selecting(l1=sports_category, l2=indian_gk, l3=programming_questions)
