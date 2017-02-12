function fancyArr(arr, symbole){
  // var temp = 0;
  // if(reversed === true){
    // for (var i = 0; i < arr.length -1; i++){
      // temp = arr[i];
      // arr[i] = arr[arr.length - 1 - i];
      // arr[arr.length - 1 - i] = temp;
    //}
  //}
  for (var i = 0; i < arr.length; i++){
    console.log(i + symbole + arr[i]);
  }
}
fancyArr(["James", "Jill", "Jane", "Jack"], "->");

// reversed inside parameter
