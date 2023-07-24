import json
import sys


def rescale_axis(val: float, val_min: float, val_max: float, new_val_min: float, new_val_max: float) -> float:
    """
    Rescales axis given the endpoints of the new axis as well as the endpoints of the old axis.

    val:            current value within the means of the current axis to rescale
    val_min:        minimimum endpoint of current axis to rescale
    val_max:        maximum endpoint of current axis to rescale
    new_val_min:    minimum endpoint of new axis to rescale to
    new_val_max:    maximum endpoint of new axis to rescale to

    Returns rescaled value of val
    """
    return ((val - val_min) * (new_val_max - new_val_min)) / (val_max - val_min) + new_val_min

  
def get_coordinates(file_name: str) -> list[list[float, float]]:
    """
    Get "coordinates" item from JSON file or text file
    """

    # If input file is a json file
    if file_name.split(".")[-1] == "json":

        # Open JSON file
        file = open(file_name)

        # Get JSON object in the form of Python dictionary
        data = json.load(file)

        # Get the "coordinates" item 
        return data["coordinates"][0]
    
    # Else if input file is a text file
    elif file_name.split(".")[-1] == "txt":

        # Open text file and read input
        input_file = open(file_name, "r")
        lines = input_file.readlines()

        # Return coordinate data
        return [[float(line.split(",")[0]), float(line.split(",")[1])] for line in lines]
    

def get_min_max(axis: str, data: list[list[float, float]]) -> list[float, float]:
    """
    Get the minimum/maximum values based on the given axis.
    """
    min = float("inf")
    max = float("-inf")

    if axis == "x":
        for point in data:
            if point[0] < min:
                min = point[0]
            if point[0] > max:
                max = point[0]
        return [min, max]

    elif axis == "y":
        for point in data:
            if point[1] < min:
                min = point[1]
            if point[1] > max:
                max = point[1]
        return [min, max]

    else:
        print("Please use \"x\" or \"y\" for axis argument.")
        return [-1, -1]


# def print_rescaled_coord(coordinates: list[list[float, float]], old_x_min: float, old_x_max: float, old_y_min: float, old_y_max: float, new_x_min: float, new_x_max: float, new_y_min: float, new_y_max):
def print_rescaled_coord(coordinates: list[list[float, float]], old_x_range: list[float, float], old_y_range: list[float, float], new_x_range: list[float, float], new_y_range: list[float, float]):

    """
    Prints rescaled coordinates given the new endpoints of the x and y axes.
    """
    for point in coordinates:
        print(str(rescale_axis(point[0], old_x_range[0], old_x_range[1], new_x_range[0], new_x_range[1])) + "," + str(rescale_axis(point[1], old_y_range[0], old_y_range[1], new_y_range[1], new_y_range[0])), end=" ")
    print()



if __name__ == "__main__":

    # Command line arguments: 
    # sys.argv[1] : FILE_NAME
    # sys.argv[2] : NEW_X_MIN
    # sys.argv[3] : NEW_X_MAX
    # sys.argv[4] : NEW_Y_MIN
    # sys.argv[5] : NEW_Y_MAX

    file_name = sys.argv[1]
    coordinates = get_coordinates(file_name) 
    old_x_range = get_min_max("x", coordinates)
    old_y_range = get_min_max("y", coordinates)
    new_x_range = [float(sys.argv[2]), float(sys.argv[3])] # Assuming new x range has minimum endpoint of 0
    new_y_range = [float(sys.argv[4]), float(sys.argv[5])] # Assuming new y range has minimum endpoint of 0
    print_rescaled_coord(coordinates, old_x_range, old_y_range, new_x_range, new_y_range)





