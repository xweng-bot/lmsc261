const conesSoldPerHour = 14;
const inventory = 400;

for (let hour = 1; hour <= 12; hour++) {
    let conesSold = conesSoldPerHour * hour;
    let inventoryLeft = inventory - conesSold;
    print(conesSoldPerHour * hour + " sold at hour " + hour);
    print(conesSold + " sold at hour " + hour + " " + inventoryLeft + " left");

}

