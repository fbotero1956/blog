
function printMessages(){
console.log("message from JavaScript: no messages at this time!");
document.getElementById("demo").innerHTML = "message from JavaScript: no messages at this time!";
};

window.onload = printMessages;