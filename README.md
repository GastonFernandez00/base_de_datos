# Base de Datos

## How to use.
- Set the virtual environment
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

- Run the program from the root directory.
    ```bash
    python3 -u src/questionnaire.py
    ```

## Description of Directories.
- docs:
    - Contains a resume in PDF format.

- files:
    - Contains the questions for each exam, in json format. The question are phrased with 'yes or no' answers in mind.
    - Structure:
        ```json
        {
            "question":"the sun is black",
            "answer":false,
            "explanation":""
        }        
        ```

- src:
    - Only contains the `questionnaire` file.

## Description of the Questionnaire.

- Class `questionnaire`:
    - Functions:
        - `__init__`: Stores the right and wrong answers. These are later used to make some metrics. \
        Also starts the full loop of the program by calling the rest of the functions.
        
        - `_print_result`: Calculates and prints ${right\_answers}\over{total\_answers}$ $* 100$ \
        Prints the total amount of `right_answers` and `wrong_answers` \
        And most importantly, lists the answers that were wrongly answered, with the right answer and its explanation, if it was provided.
        
        - `_randomize_order`: Takes the whole JSON file and shuffles it.
        
        - `_define_exam`: Asks which exam is going to be read, 1 or 2, and opens the questions related to it.

        - `_get_questions`: Calls `_define_exam` and with its answer, opens the right file as a JSON object, and stores the questions as a list of JSON objects. Also stores the amount of questions that there are.

        - `_check_answer`: The use input is passed to it, and checks if it is `yes|y|no|n`, otherwise ask for a new input.

        - `_get_answer`: Takes the user input and calls `_check_answer`, after that, returns whether the user answered yes or not.

        - `_start`: Main loop, runs through all the questions.


        
