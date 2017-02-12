var daysUntilMyBirthday = 60;

for ( daysUntilMyBirthday; daysUntilMyBirthday >=1  ;daysUntilMyBirthday--){
 if(daysUntilMyBirthday > 30){
   console.log( daysUntilMyBirthday + " days until my birthday. Such a long time... :(")
  } else if ( daysUntilMyBirthday <= 30 &&  daysUntilMyBirthday >=5 ){
    console.log( daysUntilMyBirthday + " days until my birthday. COMING UP!!!")
  } else if ( daysUntilMyBirthday <= 4 &&  daysUntilMyBirthday >=3){
    console.log( daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!! SCREAM IT")
  } else if ( daysUntilMyBirthday === 2 ){
    console.log( daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!")
  } else if ( daysUntilMyBirthday === 1 ){
    console.log( daysUntilMyBirthday + " DAY UNTIL MY BIRTHDAY!!!")
  } else {
    console.log ("BDAY");
  }
}