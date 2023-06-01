// import axios from 'axios';

class RenderCart {
    constructor() {
        // this.gamesData = await this.fetchData();
    }

    async fetchData(){
        const response = await axios.get(cartURL);
        return response.data;
            // .then(response => {
             
            // })
            // .catch(error => {
            //   console.error(error);
            // });
    }

    cartChangeQuantity(productId, action) {

        if (cart[productId] !== undefined) {
    
            if (action == 'plus' && cart[productId]['quantity'] < 10){
                cart[productId]['quantity'] += 1
            }
    
            if (action == 'minus'){
                if (cart[productId]['quantity'] > 1){
                    cart[productId]['quantity'] -= 1
                }
                if (cart[productId]['quantity'] <= 0){
                    delete cart[productId];
                }
            }
    
        }
    
        document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
        updateCartCounter();
        this.render()
        
    }
    
    removeCookieItem(productId){
    
        if (cart[productId] !== undefined){
            delete cart[productId];
        }
    
        document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
        updateCartCounter();
        this.render()
    }

    async render() {
        let htmlCatalog = '';
        let sumCatalog = 0;
        let AmountOfItems = 0;
        let gamesData = await this.fetchData();
        // console.log(this.gamesData);

        for (let key in cart) {
            if (cart[key] !== undefined) {
                for (let i = 0; i < gamesData.length; i++) {
                    if (gamesData[i].id == key) {
                        htmlCatalog += `
                        <div class="cart_container_products_cartitem">
                        <div class="shop_container_products_item_imagewrapper">
                            <a href="" target="_blank" class="img-shadow centered_a"><img class="shop_container_products_item_image"  src="${gamesData[i].image}" alt=""></a>
                        </div>

                        <div class="cart_container_products_cartitem_title">
                            <a href="" target="_blank">
                                <div class="cart_container_products_cartitem_titlelink">
                                ${gamesData[i].title}
                                </div>
                            </a>
                        </div>

                        <div class="cart_container_products_cartitem_price">
                            ${gamesData[i].price}₴
                        </div>

                        <div class="cart_container_products_cartitem_counter">
                            <div class="cart_container_products_cartitem_counter__minus" onclick="cartPage.cartChangeQuantity(${key}, 'minus')">-</div>
                            <div class="cart_container_products_cartitem_counter__value">${cart[key].quantity}</div>
                            <div class="cart_container_products_cartitem_counter__plus" onclick="cartPage.cartChangeQuantity(${key}, 'plus')">+</div>
                        </div>

                        <div class="cart_container_products_cartitem_price">
                            ${gamesData[i].price*cart[key].quantity}₴
                        </div>

                        <div class="cart_container_products_cartitem_button"  onclick="cartPage.removeCookieItem(${key});">
                            Remove
                        </div>

                        </div>
                        `;
                        sumCatalog += gamesData[i].price*cart[key].quantity;
                        AmountOfItems += cart[key].quantity;
                    }
                }                
            }
        };

        const html = `
            <div class="cart_container_products" id="cart">${htmlCatalog}</div>
            <div class="cart_container_total">
                <div class="cart_container_total_quantity">
                    <div>Кількість товарів</div>
                    <div>${AmountOfItems}</div>
                </div>
                <div class="cart_container_total_price">
                    <div>Разом:</div>
                    <div>${sumCatalog.toLocaleString()}₴</div>
                </div>
                <div class="cart_container_total_button">
                    Оформити замовлення
                </div>
            </div>
        `;
        const ROOT_CART = document.getElementById('cart');
        ROOT_CART.innerHTML = html;
    }
}

const cartPage = new RenderCart();
cartPage.render();

