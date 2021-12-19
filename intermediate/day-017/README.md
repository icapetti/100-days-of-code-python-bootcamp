#
## Attributes, Class Constructors and __init__() function.
We can see attributes like a variable that is associated with a a object.
Constructors are functions that are called when an object is created. It's responsible for initializing the object and all of its attributes. Every that an onject is created, the __init__() function is called.

Using the __init__() function to assign values to object attributes:
```python
class Car:
    def __init__(self, make, model, year): # Attributes values are passed in as arguments.
        self.make = make # Attributes are defined as variables of the object.
        self.model = model
        self.year = year
        self.price = 0.0 # We can set default values for attributes, without receiveing them directly from the __init__() function.

```

`self` is a reference to the current instance of the class, and is used to access variables that belong to the class.
`make, model, year` are the attributes that belong to the class, and are assigned values in the __init__() function.

`my_car = Car('Honda', 'Accord', '2002')`

## Quiz Game

The goal is to develop a True/False quiz game that asks the user a question and checks the answer.
The source is a list of dicts with `text` and `answer` like this:

```python
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
```
### Roadmap
1. Create the data dictionary
2. Create the Question class 
    - `text` and `answer` attributes.
    - `__init__()` function for this attributes.
3. Create question_bank list:
```python
question_bank = [
    Question(question1, answer1),
    Question(question2, answer2),
    Question(question3, answer3),
]
```
4. Create QuizBrain class:
    - asking the questions
    - checking if the answer is correct
    - updating the score
    - checking if we're the end of the quiz

5. Use opentdb.com to get other questions.



