

//click yes btn
function hoverYesButton() {


    alert('I love you too <3');
}

//move button on hover
function hoverNoButton() {
    // random from 0 to 1, then multiply with screen size
    let x = Math.random() * window.innerWidth;
    let y = Math.random() * window.innerHeight;

    document.getElementById('no-button').style.left = x + 'px';
    document.getElementById('no-button').style.top = y +'px';
    
}

function hoverYesButton() {
    // random from 0 to 1, then multiply with screen size
    let x = Math.random() * window.innerWidth;
    let y = Math.random() * window.innerHeight;

    document.getElementById('yes-button').style.left = x + 'px';
    document.getElementById('yes-button').style.top = y +'px';
    
}