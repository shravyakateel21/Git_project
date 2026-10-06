function showSolution(questionNumber, selectedAnswer, correctAnswer) {

    const solution =
        document.getElementById("solution" + questionNumber);

    solution.style.display = "block";


    // Get all options for this question
    const options =
        document.querySelectorAll(
            'input[name="question' + questionNumber + '"]'
        );


    options.forEach(function(input) {

        const label = input.parentElement;

        label.style.background = "";
        label.style.borderColor = "";


        if (input.checked) {

            if (selectedAnswer === correctAnswer) {

                label.style.background = "#e8f8ee";
                label.style.borderColor = "#28a745";

            } else {

                label.style.background = "#ffeaea";
                label.style.borderColor = "#dc3545";

            }

        }

    });

}


/* TIMER */

let time = 5 * 60;

const timer = document.getElementById("timer");


if (timer) {

    const countdown = setInterval(function() {

        let minutes = Math.floor(time / 60);

        let seconds = time % 60;

        seconds =
            seconds < 10
            ? "0" + seconds
            : seconds;


        timer.textContent =
            minutes + ":" + seconds;


        time--;


        if (time < 0) {

            clearInterval(countdown);

            alert(
                "Time is over! Your test will be submitted."
            );

            document.getElementById("testForm").submit();

        }

    }, 1000);

}