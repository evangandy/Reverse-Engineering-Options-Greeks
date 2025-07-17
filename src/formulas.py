def calculate_delta(s1, s2, o1, o2):
    """
    Calculate delta as the ratio of option price change to stock price change.
    
    Args:
        s1: Initial stock price
        s2: Final stock price
        o1: Initial option price
        o2: Final option price
    
    Returns:
        The calculated delta value
    """
    stock_change = s2 - s1
    option_change = o2 - o1

    return option_change / stock_change

def calculate_gamma(s1, s2, s3, d1, d2):
    """
    Calculate gamma as the rate of change of delta with respect to the underlying price.
    
    Args:
        s1: First stock price
        s2: Second stock price
        s3: Third stock price (middle price point)
        d1: Delta calculated from first and second price points
        d2: Delta calculated from second and third price points
    
    Returns:
        The calculated gamma value
    """
    delta_change = d2 - d1
    stock_change = s3 - s1
    
    return delta_change / stock_change