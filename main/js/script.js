

function functie()
{
    var text;
    text = "<p> URL: " + window.location.href + ".</p>";
    text += "<p> Locatia: " + window.location.pathname + ".</p>";
    text += "<p> Numele browserului: " + window.navigator.appName + ".</p>";
    document.getElementById("sect1").innerHTML += text;
   
   printTime();
   setInterval(printTime,1000); 
}

function printTime()
{
    var d=new Date();
    document.getElementById("date").innerHTML ="Data 📅 : "+ d.toDateString();

    var h=d.getHours();
    var m=d.getMinutes();
    document.getElementById("time").innerHTML = "Ora ⏰ : "+ h+ ":"+m;
}

function lotoFunction() {
    var corecte = 0;
    var number = [];

    document.getElementById("intrari").innerHTML = " Numerele jucate:"
    document.getElementById("extrase").innerHTML = "Numerele extrase: "
    document.getElementById("nimerite").innerHTML = "Numerele extrase: "
    
    for (i = 0; i < 8; ++i) {
        number[i] = parseInt("0x" + document.getElementById("number" + (i + 1)).value);
        document.getElementById("intrari").innerHTML += number[i] + "  ";
    }

    for (i = 0; i < 8; ++i) {
        x = Math.floor(Math.random() * 256);
        document.getElementById("extrase").innerHTML += x + "  ";
        for (j = 0; j < 8; ++j) {
            if (x == number[j]) {
                corecte++;
            }
        }
    }
    document.getElementById("nimerite").innerHTML = corecte + " numere nimerite!"
}

var fillColor;
var strokeColor;

function changeColor() {
    fillColor = document.getElementById("fill").value;
    strokeColor = document.getElementById("stroke").value;
}

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
    
}

function mouseClickedOnCanvas(evt) {
    const canvas = document.getElementById("canvas");
    mousePos = getMousePos(canvas, evt);
    var ctx = canvas.getContext("1d");
    if (mousePosOld === undefined)
    {
        mousePosOld = mousePos;
    }
    else
    {
        ctx.strokeStyle = strokeColor;
        ctx.fillStyle = fillColor;
        ctx.beginPath();
        ctx.rect(mousePosOld.x, mousePosOld.y, mousePos.x - mousePosOld.x, mousePos.y - mousePosOld.y);
        ctx.fill();
        ctx.stroke();
        mousePosOld = undefined;
    }
}

function schimbaContinut(){
    
}