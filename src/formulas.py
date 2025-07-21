def calculate_delta(s1, s2, o1, o2):
    """
    Calculate delta as ratio of option price change to stock price change.
    
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

def calculate_rho(r1, r2, o1, o2):
    """
    Calculate rho as the rate of change of option price with respect to interest rate.
    
    Args:
        r1: Initial interest rate (as decimal, e.g., 0.05 for 5%)
        r2: Final interest rate (as decimal, e.g., 0.06 for 6%)
        o1: Initial option price
        o2: Final option price
    
    Returns:
        The calculated rho value
    """
    rate_change = r2 - r1
    option_change = o2 - o1
    
    return option_change / rate_change