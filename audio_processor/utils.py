def to_ratio(fromMin, fromMax, value):
    return (value - fromMin) / (fromMax - fromMin)
    
def lerp(fromMin, fromMax, toMin, toMax, value):
    ratio = to_ratio(fromMin, fromMax, value)
    # return lin_lerp(toMin, toMax, ratio)
    return log_lerp(toMin, toMax, ratio)

def lin_lerp(minValue, maxValue, ratio):
    return (maxValue - minValue) * ratio + minValue

def log_lerp(minValue, maxValue, ratio):
    return minValue * ((maxValue/minValue) ** ratio)