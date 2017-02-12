var numberType = 0;
numbersOnly([1, "apple", -3, "orange", 0.5]);
// noNumbers([1, "apple", -3, "orange", 0.5, 90, "cherries", -193, 98, 27, 298, "yesss", "23s"]);

function numbersOnly(arr){
    var arrnew = [];
    for (var i = 0; i < arr.length; i++){
        if (typeof(arr[i]) !== typeof(numberType)){
            continue;
        }
        arrnew.push(arr[i])
    }
    console.log(arrnew);
    return arrnew;
}
