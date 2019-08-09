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
    const answer = document.getElementById("colorText");

    answer.textContent = generate_color()
    meaning = document.getElementById("colorMeaning");

    // Black
    if (answer.textContent == ringColors[0])
    {
        meaning.textContent = "You feel angry, fearful, or apathetic.";
    }
    // Yellow
    if (answer.textContent == ringColors[1])
    {
        meaning.textContent = "Your emotions are mixed or conflicted. You may feel distracted or slightly anxious.";
    }
    // Orange
    if (answer.textContent == ringColors[2])
    {
        meaning.textContent = "You are upset. You feel nervous, stressed, or confused about something.";
    }
    // Light Green
    if (answer.textContent == ringColors[3])
    {
        meaning.textContent = "You are anxious about something or someone. You are guarded and alert. You may feel mild jealousy or stress.";
    }
    // Green
    if (answer.textContent == ringColors[4])
    {
        meaning.textContent = "This is the default color. Your emotions are stable today: you do not feel execessive negativity or positivity.";
    }
    // Blue
    if (answer.textContent == ringColors[5])
    {
        meaning.textContent = "You are cheerful and optimistic.";
    }
    // Dark Blue
    if (answer.textContent == ringColors[6])
    {
        meaning.textContent = "You are content.";
    }
    // Violet
    if (answer.textContent == ringColors[7])
    {
        meaning.textContent = "You have romance on your mind. You feel moody, mischievous, or sensual. You are prone to unpredictable choices today.";
    }
    // Pink
    if (answer.textContent == ringColors[8])
    {
        meaning.textContent = "You are overcome with strong emotions. You are infatuated with someone or something.";
    }
}

//function reset() {
    //const answer = document.getElementById("colorText");
    //answer.textContent = "";
    //const meaning = document.getElementById("colorMeaning");
    //meaning.textContent = "";
    //document.body.removeChild(next)
    //answerButton = document.createElement('button')
    //answerButton.innerHTML = "Check Ring";
    //document.body.appendChild(answerButton)
    //answerButton.addEventListener('click', get_mood)
  //}
  
function generate_color() {
	var answers_length = ringColors.length;
	var random_answer_index = Math.floor(Math.random() * answers_length) 
	//console.log(answers_length)
	//console.log(random_answer_index)
	//console.log(mystic_answers[random_answer_index])
	return ringColors[random_answer_index]
}