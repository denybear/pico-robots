def gradient (initial_color, target_color, number_of_rows):

    result = []

    # get the total difference between each color channel
    red_difference=target_color[0]-initial_color[0]
    green_difference=target_color[1]-initial_color[1]
    blue_difference=target_color[2]-initial_color[2]

    # divide the difference by the number of rows, so each color changes by this amount per row
    red_delta = red_difference/number_of_rows
    green_delta = green_difference/number_of_rows
    blue_delta = blue_difference/number_of_rows

    # display the color for each row
    for i in range(0, number_of_rows):
        # apply the delta to the red, green and blue channels
        interpolated_color=(initial_color[0] + int(red_delta * i), 
                            initial_color[1] + int(green_delta * i),
                            initial_color[2] + int(blue_delta * i))
        result.append (interpolated_color)

    return result