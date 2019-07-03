let r, g, b;

function setup() {
  createCanvas(720, 400).parent('canvasHolder');
  frameRate(1);
}

function draw() {
  r = random(255);
  g = random(255);
  b = random(255);
  background(127);
  strokeWeight(2);
  stroke(r, g, b);
  fill(r, g, b, 127);
  ellipse(360, 200, 200, 200);
}