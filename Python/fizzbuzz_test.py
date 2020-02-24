#pylint

from FizzBuzz import run_round

def describe_a_fizzbuzz_program_that():

    def has_a_smoke_test():
        assert True

    def check_if_number_is_multiple_of_3_or_5():
        """Checks stuff"""
        assert run_round(3) == "Fizz"
        assert run_round(2) == "2"
        assert run_round(15) == "FizzBuzz"