// get all "Add to Cart" buttons
var updateButtons = document.getElementsByClassName('update-cart');


// acquire csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// add event listener to each button
for (var i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', (event) => {

        var product_id = event.target.dataset.product;
        var action = event.target.dataset.action;

        fetch(updateOrderURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'product_id': product_id,
                'action': action,
            })
        }).then((response) => {
            return response.json();
        }).then((data) => {
            location.reload();
        });
    })
}
