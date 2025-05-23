import enum


class FizzBuzzEnum(str, enum.Enum):
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    FIZZ_BUZZ = "FizzBuzz"


def fizzbuzz_stage1(n: int = 100) -> None:
    """
    fizzbuzz statge 1

    print number from 1 to n
        - if number is multiple of 3 print `Fizz`
        - if number is multiple of 5 print `Buzz`
        - if number is multiple of 3 and 5 print `FizzBuzz`

    Args:
        n: range of numbers to print start from 1

    Returns:
        None
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print(FizzBuzzEnum.FIZZ_BUZZ.value)
        elif i % 5 == 0:
            print(FizzBuzzEnum.BUZZ.value)
        elif i % 3 == 0:
            print(FizzBuzzEnum.FIZZ.value)
        else:
            print(i)


def fizzbuzz_stage2(n: int = 100) -> None:
    """
    fizzbuzz statge 2

    print number from 1 to n
        - if number is multiple of 3 or has 3 in it  print `Fizz`
        - if number is multiple of 5 or has 5 in it  print `Buzz`
        - if number is multiple of 3 and 5 print `FizzBuzz`

    Args:
        n: range of numbers to print start from 1

    Returns:
        None
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print(FizzBuzzEnum.FIZZ_BUZZ.value)
            continue

        # TODO: What happens if number % 3 == 0 and has 5 in number?
        fizz = i % 3 == 0 or "3" in str(i)
        buzz = i % 5 == 0 or "5" in str(i)

        if not fizz and not buzz:
            print(i)
        elif fizz and buzz:
            print(FizzBuzzEnum.FIZZ_BUZZ.value)
        elif fizz:
            print(FizzBuzzEnum.FIZZ.value)
        else:
            print(FizzBuzzEnum.BUZZ.value)


if __name__ == "__main__":
    print("-" * 10, "Stage 1 Start", "-" * 10)
    fizzbuzz_stage1()
    print("-" * 10, "Stage 1 End", "-" * 10)

    print("-" * 10, "Stage 2 Start", "-" * 10)
    fizzbuzz_stage2()
    print("-" * 10, "Stage 2 End", "-" * 10)
