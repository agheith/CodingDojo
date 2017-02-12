
var array =([1, "apple", -3, "orange", 0.5]);
function nums_only(){
  var newArr = [];
  for (var i = 0; i< array.length; i++){
    if ( typeof (array[i]) === "number"){
        newArr.push(array[i]);
    }
  }
  return newArr;
}
console.log(nums_only());
