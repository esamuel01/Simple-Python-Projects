def convert_to_celcius(fahrenheit):
    '''(number) -> number
    Return the number of Celcius degrees equivalent to
    fahrenheit degrees
    
    >>> convert_to_celcius(32)
    0.0
    >>> convert_to_celcius(212)
    100.0
    '''
    return (fahrenheit - 32) * (5 / 9)
