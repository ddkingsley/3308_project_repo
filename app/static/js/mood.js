const ringColors = ["Black", "Yellow", "Orange", "Light Green", "Green", "Blue", "Dark Blue", "Violet", "Pink"];

// You feel angry, fearful, or apathetic.
// Your emotions are mixed or conflicted. You may feel distracted or slightly anxious.
// You are upset. You feel nervous, stressed, or confused about something.
// You are anxious about something or someone. You are guarded and alert. You may feel mild jealousy or stress.
// This is the default color. Your emotions are stable today: you do not feel execessive negativity or positivity.
// You are cheerful and optimistic today
// You are content.
// You have romance on your mind. You may feel moody, mischievous or sensual. You are prone to unpredictable choices today.
// You are overcome with strong emotions. You are infatutated with someone or something.

window.onload = function() {
    answerButton = document.querySelector(".checkButton");
    answerButton.addEventListener('click', get_mood)
}

function get_mood() {
    var answer = document.getElementById("colorText");

    answer.textContent = generate_color()
    meaning = document.getElementById("colorMeaning")

    var defaultRing = document.getElementById("default");
    defaultRing.style.display = "none";

    var originalButton = document.querySelector(".checkButton");
    originalButton.style.display = "none";

    var tryAgainButton = document.querySelector(".resetButton");
    tryAgainButton.style.display = "block";

    tryAgainButton.addEventListener('click', reset);

    // Black
    if (answer.textContent == ringColors[0])
    {
        var blackRing = document.getElementById("black");
        blackRing.style.display = "block"; 
        meaning.textContent = "You feel angry, fearful, or apathetic.";
    }
    // Yellow
    if (answer.textContent == ringColors[1])
    {
        var yellowRing = document.getElementById("yellow");
        yellowRing.style.display = "block";
        meaning.textContent = "Your emotions are mixed or conflicted. You may feel distracted or slightly anxious.";
    }
    // Orange
    if (answer.textContent == ringColors[2])
    {
        var orangeRing = document.getElementById("orange");
        orangeRing.style.display = "block";
        meaning.textContent = "You are upset. You feel nervous, stressed, or confused about something.";
    }
    // Light Green
    if (answer.textContent == ringColors[3])
    {
        var lGreenRing = document.getElementById("lGreen");
        lGreenRing.style.display = "block";
        meaning.textContent = "You are anxious about something or someone. You are guarded and alert. You may feel mild jealousy or stress.";
    }
    // Green
    if (answer.textContent == ringColors[4])
    {
        var greenRing = document.getElementById("green");
        greenRing.style.display = "block";
        meaning.textContent = "This is the default color. Your emotions are stable today: you do not feel execessive negativity or positivity.";
    }
    // Blue
    if (answer.textContent == ringColors[5])
    {
        var blueRing = document.getElementById("blue");
        blueRing.style.display = "block";
        meaning.textContent = "You are cheerful and optimistic.";
    }
    // Dark Blue
    if (answer.textContent == ringColors[6])
    {
        var dBlueRing = document.getElementById("dBlue");
        dBlueRing.style.display = "block";
        meaning.textContent = "You are content.";
    }
    // Violet
    if (answer.textContent == ringColors[7])
    {
        var violetRing = document.getElementById("violet");
        violetRing.style.display = "block";
        meaning.textContent = "You have romance on your mind. You feel moody, mischievous, or sensual. You are prone to unpredictable choices today.";
    }
    // Pink
    if (answer.textContent == ringColors[8])
    {
        var pinkRing = document.getElementById("pink");
        pinkRing.style.display = "block";
        meaning.textContent = "You are overcome with strong emotions. You are infatuated with someone or something.";
    }

}

function reset() {
    var answer = document.getElementById("colorText");
    answer.textContent = "";


    var meaning = document.getElementById("colorMeaning");
    meaning.textContent = "";

    var defaultColor = document.getElementById("default");
    defaultColor.style.display = "block";

    var originalButton = document.querySelector(".checkButton");
    originalButton.style.display = "block";

    var tryAgainButton = document.querySelector(".resetButton");
    tryAgainButton.style.display = "none";

    var oldblackRing = document.getElementById("black");
    oldblackRing.style.display = "none"; 

    var oldyellowRing = document.getElementById("yellow");
    oldyellowRing.style.display = "none";

    var oldorangeRing = document.getElementById("orange");
    oldorangeRing.style.display = "none";

    var oldlGreenRing = document.getElementById("lGreen");
    oldlGreenRing.style.display = "none";

    var oldgreenRing = document.getElementById("green");
    oldgreenRing.style.display = "none";

    var oldblueRing = document.getElementById("blue");
    oldblueRing.style.display = "none";

    var olddBlueRing = document.getElementById("dBlue");
    olddBlueRing.style.display = "none";

    var oldvioletRing = document.getElementById("violet");
    oldvioletRing.style.display = "none";

    var oldpinkRing = document.getElementById("pink");
    oldpinkRing.style.display = "none";

    originalButton.addEventListener('click', get_mood)
}
  
function generate_color() {
	var answers_length = ringColors.length;
	var random_answer_index = Math.floor(Math.random() * answers_length) 
	//console.log(answers_length)
	//console.log(random_answer_index)
	//console.log(mystic_answers[random_answer_index])
	return ringColors[random_answer_index]
}
