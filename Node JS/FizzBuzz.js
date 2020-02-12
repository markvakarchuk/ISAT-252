var length_of_round = 100;
var fizz_divider = 3;
var buzz_divider = 5;
var fizzbuzz_divider = fizz_divider*buzz_divider;

for (var i = 1; i < length_of_round; i++){
    if (i % fizzbuzz_divider == 0){
        console.log("FizzBuzz");
    } else if (i % fizz_divider == 0){
        console.log("Fizz");
    } else if ( i % buzz_divider == 0){
        console.log("Buzz");
    } else{
        console.log(i);
    }
}