const activities = [
    "babysit tadpoles",
    "flies for lunch",
    "tongue stretch",
    "swimming lesson"
];
let actsIndex = prompt("What is your activity index?")
actsIndex = actsIndex % 4;
print(activities[actsIndex])