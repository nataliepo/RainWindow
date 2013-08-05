var DROP_HEIGHT = 75;
var DROP_WIDTH = 2;
var NUM_DROPS = 400;

Drop = function(x,y){
  this.x = x;
  this.y = y;
  this.width = DROP_WIDTH;
  this.height = DROP_HEIGHT; 
};

window.requestAnimFrame = (function(callback) {
  return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
  function(callback) {
    window.setTimeout(callback, 1000 / 60);
  };
})();

function drawDrop(drop, context) {
  context.beginPath();
  context.moveTo(drop.x, drop.y);
  context.lineTo(drop.x - drop.width / 2, drop.y + (drop.height * .6));
  context.bezierCurveTo(
    drop.x - drop.width / 2,
    drop.y + drop.height,
    drop.x + drop.width / 2,
    drop.y + drop.height,
    drop.x + drop.width / 2,
    drop.y + (drop.height * .6));
  context.closePath();
  context.fillStyle = 'white';
  context.fill();
  context.strokeStyle = 'white';
  context.stroke();
}

function validDropCoor(drop, mousePos) {
  return (Math.abs(drop.x - mousePos.x) > 50);
}

function animate(drops, canvas, context) {
  var linearSpeed = 20;
  context.clearRect(0, 0, canvas.width, canvas.height);
  for (i = 0; i < drops.length; i++) {
    var d = drops[i];
      d.y = (d.y + linearSpeed) % canvas.height;
      if (typeof(mousePos) == "undefined" || validDropCoor(d, mousePos)) {
        drawDrop(d, context);
      }
  }
  requestAnimFrame(function() {
    animate(drops, canvas, context);
  });
}

function getMousePos(canvas, evt) {
  var rect = canvas.getBoundingClientRect();
  return {
    x: evt.clientX - rect.left,
    y: evt.clientY - rect.top
  };
}

function randomDrop() {
  var x = Math.floor((Math.random()*1024)+1);
  var y = Math.floor((Math.random()*1024)+1);
  return new Drop(x, -y);
}

window.addEventListener('load', function (ev) {
  var canvas = document.getElementById('myCanvas');
  canvas.addEventListener('mousemove', function(evt) {
    mousePos = getMousePos(canvas, evt);
  }, false);

  var context = canvas.getContext('2d');
  var drops = []
  
  for (var i=0;i<NUM_DROPS;i++) { 
    var d = randomDrop()
    drops.push(d);
    drawDrop(d, context);
  }

  setTimeout(function() {
    var startTime = (new Date()).getTime();
    animate(drops, canvas, context, startTime);
  }, 1000);

}, false);



