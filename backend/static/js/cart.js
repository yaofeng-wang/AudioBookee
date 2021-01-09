var updateButtons = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateButtons.length; i++) {

    document.addEventListener('click', (event) => {
        var url = '/update/item';
        var product_id = updateButtons[i].dataset.product_id;
        var action = updateButtons[i].dataset.action;
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: {
                'product_id': product_id,
                'action': action
            }
        }).then(response => {
            return response.json()
        }).then(data => {
            // location.reload();
        });
    })
}