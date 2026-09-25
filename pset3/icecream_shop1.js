const priceOfIceCream = 3;

let paymentRecieved = prompt("How much money do you have?");

let isPaymentEnough = paymentRecieved >= priceOfIceCream;

if (isPaymentEnough) {
    let change = paymentRecieved - priceOfIceCream;
    print("Thanks! Enjoy the Ice Cream! Your change is $" + change);
} else {
    print("Not enough cash!");
}