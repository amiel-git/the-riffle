var cartButton = document.getElementsByClassName("update-cart");

for(var i=0 ; i< cartButton.length ; i++) {
    cartButton[i].addEventListener("click", function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;

        if (user == "AnonymousUser"){
            console.log("User not authenticated")
        }
        else {
            updateUserOrder(productId,action)
        }

    })
}


function updateUserOrder(productId, action) {
    console.log("sending data....")
    var url = "/orders/update-item/"

    fetch(url, {
        method:"POST",
        headers: {
            "Content-Type":"application/json",
            'Accept': 'application/json',
            'X-CSRFToken': csrftoken,    
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })

    .then(response => {
        return response.json()
    })

    .then(data => {
        console.log(data)
    })

}