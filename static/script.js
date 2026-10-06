const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");
const taskList = document.getElementById("taskList");


// Load tasks when website opens

document.addEventListener("DOMContentLoaded", loadTasks);


// Add button

addButton.addEventListener("click", addTask);


// Press Enter to add task

taskInput.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        addTask();
    }

});


// GET TASKS

async function loadTasks() {

    const response = await fetch("/api/tasks");

    const tasks = await response.json();

    taskList.innerHTML = "";

    tasks.forEach(task => {

        displayTask(task);

    });

    updateStats(tasks);
}


// ADD TASK

async function addTask() {

    const text = taskInput.value.trim();

    if (text === "") {

        alert("Please enter a task.");

        return;
    }


    const response = await fetch("/api/tasks", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            task: text
        })

    });


    const task = await response.json();

    displayTask(task);

    taskInput.value = "";

    loadTasks();
}


// DISPLAY TASK

function displayTask(task) {

    const div = document.createElement("div");

    div.className = "task";

    if (task.completed) {
        div.classList.add("completed");
    }


    div.innerHTML = `

        <input
            type="checkbox"
            class="check"
            ${task.completed ? "checked" : ""}
        >

        <span class="task-text">
            ${task.task}
        </span>

        <button class="delete">
            Delete
        </button>

    `;


    // COMPLETE TASK

    const checkbox =
        div.querySelector(".check");


    checkbox.addEventListener("change", async function() {

        const completed =
            checkbox.checked ? 1 : 0;


        await fetch(`/api/tasks/${task.id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                completed: completed
            })

        });


        div.classList.toggle(
            "completed",
            checkbox.checked
        );

        loadTasks();

    });


    // DELETE TASK

    const deleteButton =
        div.querySelector(".delete");


    deleteButton.addEventListener("click", async function() {

        await fetch(`/api/tasks/${task.id}`, {

            method: "DELETE"

        });


        div.remove();

        loadTasks();

    });


    taskList.appendChild(div);
}


// UPDATE STATISTICS

function updateStats(tasks) {

    const total = tasks.length;

    const completed =
        tasks.filter(task => task.completed).length;

    const pending =
        total - completed;


    document.getElementById(
        "totalTasks"
    ).textContent = total;


    document.getElementById(
        "completedTasks"
    ).textContent = completed;


    document.getElementById(
        "pendingTasks"
    ).textContent = pending;
}


// DARK MODE

document.getElementById("themeButton")
    .addEventListener("click", function() {

        document.body.classList.toggle("dark");

    });