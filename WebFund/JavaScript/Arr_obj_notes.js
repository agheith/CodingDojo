// var dojo = {};                                 // creates an empty object
// dojo = {
//   name: 'Coding Dojo',                         // property can store a string
//   number_of_students: 25,                      // property can store a number
//   instructors: ['Andrew', 'Michael', 'Jay'],   // property can store arrays
//   location: {                                  // property can even store another object!
//     city: 'San Jose',
//     state: 'CA',
//     zipcode: 'unknown'
//   }
// }                                              // access object properties with dot (.) notation
//
// dojo.snacks = ['Fig Bar', 'Bagels', 'Apple'];
// dojo.location.city = 'Seattle'
// dojo.location.state = "Washington"
// console.log(dojo.name, dojo.instructors);
//
// var glazedDonuts = [
//   {
//     frosting: 'glazed',
//     style: 'cake',
//     type: 'old fashioned',
//     age: '45',
//     time: 'minutes'
//   },
//   {
//     frosting: 'glazed',
//     style: 'yeast raised',
//     type: 'regular',
//     age: '5',
//     time: 'minutes'
//   },
//   {
//     frosting: 'glazed',
//     style: 'yeast raised',
//     type: 'jelly filled',
//     age: '1',
//     time: 'seconds'
//   }
// ];

// var purchase;
// //You
// if(glazedDonuts[0].age < 25 && (glazedDonuts[0].time == 'seconds' || glazedDonuts[0].time == 'minutes')){
//   //shop owner
//   purchase = glazedDonuts[0];
// }
// else {
//   console.log('sorry it has been out a bit longer');
// }


// var numPurchase = 0;
// for (var donut in glazedDonuts) {
//   if (glazedDonuts[donut].age < 25 && (glazedDonuts[donut].time == 'seconds' || glazedDonuts[donut].time == 'minutes')) {
//     numPurchase++;
//   }
//   else {
//     // console.log('not this donut...');
//   }
// }
// console.log(glazedDonuts[donut]);
