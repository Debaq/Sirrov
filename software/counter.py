
def movement_eye(input=None, direction=None, nistagmus=None)->list:
    
    if input is None:
        input = ["KB"]
    if nistagmus is None:
        nistagmus = [False,0]
    if direction is None:
        direction = "horizontal"

    counter()
    return []


def counter (amplitude = 30, center_value = 30, speed = 1, nistagmus=None)->list:
    if nistagmus is None:
        nistagmus = [False,0]
    data = []
    min_value = 0
    max_value = 60
    

    new_max = center_value + amplitude
    new_min = center_value - amplitude

    for i in range(new_min, new_max+1, speed):
        if i >= min_value and i <= max_value:
            data.append(i)


    return data 


def frame_direction(direction:int,number_frames:int)->list:
    pass


def nistagmus(high = True)->list:
    pass



print(counter())