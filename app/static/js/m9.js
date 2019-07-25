window.onload = function() {
	answerButton = document.createElement('button')
	answerButton.innerHTML = "Give me ze answer!";
	document.body.appendChild(answerButton)
	answerButton.addEventListener('click', get_answer)
}
function get_answer() {
  const answer = document.getElementById("circle_text");
  generate_answer()
  answer.textContent = "Nein!";
  document.body.removeChild(answerButton)
  next = document.createElement('button')
  next.innerHTML = "Would you like to try again?";
  document.body.appendChild(next)
  next.addEventListener('click', reset)
}
function reset() {
  const answer = document.getElementById("circle_text");
  answer.textContent = "9";
  document.body.removeChild(next)
  answerButton = document.createElement('button')
  answerButton.innerHTML = "Give me ze answer!";
  document.body.appendChild(answerButton)
  answerButton.addEventListener('click', get_answer)
}
const mystic_answers = ["Better not tell you now", "Yes", "Definitly", "Maybe", "No, but you're on the right track", 
"that's kind of a stupid question", "Your question was bad and you should feel bad", "42", "Nein!",
"cosmic energies are telling me... no", "Does a bear deficate in the woods?", "I think you already know the answer"];
function generate_answer() {
	var answers_length = mystic_answers.length;
	var random_answer_index = Math.floor(Math.random() * answers_length) 
	//console.log(answers_length)
	//console.log(random_answer_index)
	//console.log(mystic_answers[random_answer_index])
}
