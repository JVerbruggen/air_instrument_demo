def lerp(fromMin, fromMax, toMin, toMax, value):
    fromDelta = fromMax - fromMin
    portion = (value - fromMin) / fromDelta # 0.0-1.0
    toDelta = toMax - toMin
    result = toDelta * portion + toMin
    return result

def log_lerp():
    ...