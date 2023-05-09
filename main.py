import random
import pandas as pd

def get_random_people() -> list[str]:
    return list(range(1, 401))


print(get_random_people())


def get_available_questions() -> dict[str, dict[str, tuple[str]]]:
    return {
        "sabes que es el vih": {"answers": ("si", "no")},
        "a que edad comenzaste a informarte sobre las ETS": {"answers": ("< 18", "> 18", "no tenia idea hasta ahorita")},
        "te haz realizado estudios para saber si estas libre de enfermedades venereas": {"answers": ("si", "no")},
        "te proteges al momento de tener relaciones sexuales": {"answers": ("si", "no")},
        "cual es el metodo anticonceptivo que usas": {"answers": ("condón", "no uso")},
        "cada cuanto recurres a un especialista para un chequeo general": {"answers": ("1 vez al año", "nunca he ido", "2 veces al año")},
        "eres consciente sobre la pandemia de vih que tepic a enfrentado en los ultimos años": {"answers": ("si", "no")},
        "sabes los sintomas del VIH y como detectarlo": {"answers": ("si", "no")},
        "tienes algún conocido que sufra de esta enfermedad": {"answers": ("si", "no")},
    }

def choice_answers(people: list[int], questions: dict):
    structured: dict = {}

    for person in people:
        structured[person] = []
        for question in questions.keys():
            structured[person].append(random.choice(questions[question]["answers"]))

    return structured
        

def answers_to_dataframe(answers: dict) -> None:
    df = pd.DataFrame(answers)

    df.to_excel("encuesta.xlsx", index=False)
    


def main():
    people = get_random_people()
    questions_to_use = get_available_questions()
    questions = choice_answers(people, questions_to_use)
    print(questions)
    answers_to_dataframe(questions)






if __name__ == "__main__":
    main()
