import json
import random


class Questionnaire:

    def __init__(self) -> None:
        self._correct: list = []
        self._wrong: list = []
        self._get_questions()
        self._randomize_order()
        self._start()

    def _print_result(self) -> None:
        Total: int = len(self._correct) * 100 / self._total_questions
        result: str = f"""
Questions correctly answered: {len(self._correct)}
Questions wrongly answered: {len(self._wrong)}
Total: {Total}
Now, a list of all wrong answers:
---------------------------------
"""
        print(result)
        for n in self._wrong:
            right_answer:str = f"""
Question: {n["question"]}
Answer: {n["answer"]}
Explanation: {n["explanation"]}
"""
            print(f"{right_answer} \n---------------------------------n")

    def _randomize_order(self):
        random.shuffle(self._json_file)

    def _define_exam(self) -> str:
        print("Which exam are you gonna take? 1|2")
        exam = int(input())
        while exam != 1 and exam != 2:
            exam = int(input())
        
        if exam == 1:
            return "files/questions_parcial_1.json"
        else:
            return "files/questions_parcial_2.json"


    def _get_questions(self) -> None:

        questionnaire:str = self._define_exam()

        with open(questionnaire, "r") as file:
            self._json_file: list = list(json.load(file))

        self._total_questions: int = len(self._json_file)

    def _check_answer(self, answer: str) -> str:

        while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
            print("WRONG ANSWER. MUST BE [y/n] or [yes/no]")
            answer = input().lower()

        return answer

    def _get_answer(self) -> str:

        answer: str = input().lower()

        answer = self._check_answer(answer)

        answer = True if answer == "y" or answer == "yes" else False

        return answer

    def _start(self) -> None:
        counter: int = 1
        while len(self._json_file) > 0:
            question: str = f"""
Question[{counter}/{self._total_questions}]: {self._json_file[-1]["question"]}
Your answer: [y/n] || [yes/no]"""

            print(question)
            answer: str = self._get_answer()

            if self._json_file[-1]["answer"] == answer:
                self._correct.append(self._json_file[-1])
            else:
                print("WRONG")
                self._wrong.append(self._json_file[-1])

            self._json_file.pop()
            counter = 1 + counter

        self._print_result()


if __name__ == "__main__":
    x = Questionnaire()
