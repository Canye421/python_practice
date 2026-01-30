def calculate_mse(actual, predicted):
    squred_errors = []

    if len(actual) == 0 or len(predicted) == 0 or len(actual) != len(predicted):
        raise ValueError("Input lists must be of the same non-zero length.")
    else:
        for a in zip(actual , predicted):
            squred_error = (a[0] - a[1])**2
            squred_errors.append(squred_error)
    
    return sum(squred_errors)/len(squred_errors)
    
        



    
    # Your AI math practice goes here!
    