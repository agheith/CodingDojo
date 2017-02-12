//There is an old tale about a king who offered a servant $10,000 as a reward.
//The servant instead asked that for 30 days he be given an amount that would double,
// starting with a penny. (1 penny for the first day, 2 for the second, 4 for the third, then 8, 16, 32 pennies, and so on).

// How much was the reward after 30 days?

function rewardInDays(days){
  var reward = 0.01;
  var pay = 0.01;
  for (var i = 1; i < days; i++){
      pay = pay * 2;
      reward = reward + pay;
  }
console.log("The reward after " + days + " days is " + reward);
}
rewardInDays(30);

//How many days would it take the servant to make $10,000?
// How about 1 billion?
function howManyDays(goal){
  var reward = 0.01;
  var pay = 0.01;
  var day = 1;
  while (reward < goal){
    pay = pay * 2;
    reward = reward + pay;
    day++;
  }
  console.log("It takes " + day + " days to make " + goal);
}
howManyDays(10000);
