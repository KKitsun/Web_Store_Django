let classNameActive = 'shop_container_products_item_button_active';
let buttonLabelAdd = 'Додати в кошик';
let buttonLabelRemove = 'Вилучити з кошика';

function updateCartCounter() {
    let counter = 0;
    for (const [key, value] of Object.entries(cart)) {
        counter += value.quantity;
    }
    const cartCounter = document.getElementById('header_cart_counter');
    cartCounter.innerHTML = counter;
    if (counter > 0) {
        cartCounter.style.opacity = 1;
    } else {
        cartCounter.style.opacity = 0;
    }
}
updateCartCounter();

function addCookieItem(element, productId){

    if (cart[productId] == undefined){
		cart[productId] = {'quantity':1};

        element.classList.add(classNameActive);
        element.innerHTML = buttonLabelRemove;
    } else {
		delete cart[productId];

        element.classList.remove(classNameActive);
        element.innerHTML = buttonLabelAdd;
	}

    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    updateCartCounter();
}

function cartChangeQuantity(productId, action) {

    if (cart[productId] !== undefined) {

        if (action == 'plus' && cart[productId]['quantity'] < 10){
            cart[productId]['quantity'] += 1
        }

        if (action == 'minus'){
            cart[productId]['quantity'] -= 1
            if (cart[productId]['quantity'] <= 0){
                delete cart[productId];
            }
        }

    }

    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    updateCartCounter();
    location.reload()
    
}

function removeCookieItem(productId){

    if (cart[productId] !== undefined){
		delete cart[productId];
    }

    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    updateCartCounter();
    location.reload()
}