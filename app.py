from flask import Flask, render_template, request

app = Flask(__name__)


questions = [

    {
        "question": "If 5 workers can complete a work in 10 days, how many days will 10 workers take?",

        "options": [
            "2 days",
            "5 days",
            "10 days",
            "20 days"
        ],

        "answer": "5 days",

        "solution": "More workers take less time. Total work = 5 × 10 = 50 worker-days. For 10 workers, time = 50 ÷ 10 = 5 days."
    },


    {
        "question": "What is 20% of 250?",

        "options": [
            "25",
            "40",
            "50",
            "60"
        ],

        "answer": "50",

        "solution": "20% of 250 = (20 ÷ 100) × 250 = 50."
    },


    {
        "question": "A train travels 120 km in 2 hours. What is its speed?",

        "options": [
            "40 km/h",
            "50 km/h",
            "60 km/h",
            "80 km/h"
        ],

        "answer": "60 km/h",

        "solution": "Speed = Distance ÷ Time. Therefore, Speed = 120 ÷ 2 = 60 km/h."
    },


    {
        "question": "If the ratio of boys to girls is 2:3 and there are 20 boys, how many girls are there?",

        "options": [
            "20",
            "25",
            "30",
            "35"
        ],

        "answer": "30",

        "solution": "2 parts = 20 boys. Therefore, 1 part = 10. Girls = 3 parts = 3 × 10 = 30."
    },


    {
        "question": "What is the average of 10, 20 and 30?",

        "options": [
            "15",
            "20",
            "25",
            "30"
        ],

        "answer": "20",

        "solution": "Average = Sum of values ÷ Number of values. (10 + 20 + 30) ÷ 3 = 60 ÷ 3 = 20."
    }

]


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/test")
def test():

    name = request.args.get("name", "Student")

    return render_template(
        "test.html",
        name=name,
        questions=questions
    )


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")

    score = 0

    for i, question in enumerate(questions):

        user_answer = request.form.get(
            f"question{i}"
        )

        if user_answer == question["answer"]:

            score += 1


    total = len(questions)

    percentage = (score / total) * 100


    return render_template(
        "result.html",
        name=name,
        score=score,
        total=total,
        percentage=percentage
    )


if __name__ == "__main__":

    app.run(debug=True)