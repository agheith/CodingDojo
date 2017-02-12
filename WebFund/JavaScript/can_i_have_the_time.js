// var HOUR = 8;
// var MINUTE = 50;
// var PERIOD = "AM";
// ...your program should print "It's almost 9 in the morning"
// If minutes less than 30, "just after" the hour, more than 30, "almost" the next hour
// AM / PM, "in the morning", "in the evening",
//
// var HOUR = 7;
// var MINUTE = 15;
// var PERIOD = "PM";
// ...your program should print "It's just after 7 in the evening"


// var HOUR = 7;
// var MINUTE = 15;
// var PERIOD = "PM";

var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

if (HOUR <= 12 && MINUTE < 30 && PERIOD === "PM"){
  console.log("It's just after " + HOUR + PERIOD + " in the evening");
}
else if(HOUR <= 12 && MINUTE > 30 && (PERIOD) === "AM"){
  console.log("It's almost " + (HOUR+1) + PERIOD + " in the morning");
}
