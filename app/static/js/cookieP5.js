function setup() {
    createCanvas(200, 200).parent('canvasHolderCookie');
    a = 100;
  }
  
  function draw() {
    background(236,236,237);
    
    let c;
    
    c = color(101, 99, 144);
    fill(c)
    rect(0, 0, 200, 200);

    c = color(255,255,255);
	fill(c)
    rect(90, a, 20, 50);
    
	c = color(245, 233, 218);
	fill(c);
    triangle(100, 125, 125, 50, 150, 125);
    triangle(50, 125, 75, 50, 100, 125);
    triangle(50, 125, 100, 160, 150, 125);
    
    a = a - 1
      if (a < 0) {
      a = 100;
    }
  
  }