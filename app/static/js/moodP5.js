let r, g, b; //red, green, blue variables

//setup creates canvas for p5 animation in canvasHolderMood div in mood.html, sets speed of animation
function setup() {
  createCanvas(720, 400).parent('canvasHolderMood');
  frameRate(1);
}

//draws circle that randomly changes colors
function draw() {
  //randomly choose rgb values
  r = random(255);
  g = random(255);
  b = random(255);
  background(236,236,237);
  strokeWeight(2);
  stroke(r, g, b);
  fill(r, g, b, 127);
  ellipse(360, 200, 200, 200);
}
