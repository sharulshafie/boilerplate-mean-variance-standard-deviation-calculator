import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        return calculations

    list_of_digit = np.array(list)
    new_list = list_of_digit.reshape(3,3)

    # Mean each axis
    axis_mean_column = np.mean(new_list, axis=0)
    axis_mean_row = np.mean(new_list, axis=1)
    axis_mean_flatted = np.mean(new_list)

    # Variance each axis 
    axis_var_column = np.var(new_list, axis=0)
    axis_var_row = np.var(new_list, axis=1)
    axis_var_flatted = np.var(new_list)

    # Standard Deviation each axis
    axis_std_column = np.std(new_list, axis=0)
    axis_std_row = np.std(new_list, axis=1)
    axis_std_flatted = np.std(new_list)

    # Max each axis
    axis_max_column = np.max(new_list, axis=0)
    axis_max_row = np.max(new_list, axis=1)
    axis_max_flatted = np.max(new_list)

    # Min each axis
    axis_min_column = np.min(new_list, axis=0)
    axis_min_row = np.min(new_list, axis=1)
    axis_min_flatted = np.min(new_list)

    # Sum each axis
    axis_sums_column = np.sum(new_list, axis=0)
    axis_sums_row = np.sum(new_list, axis=1)  
    axis_sums_flatted = np.sum(new_list)

    calculations = {
        "mean" : [axis_mean_column.tolist(), axis_mean_row.tolist(), axis_mean_flatted],
        "variance" : [axis_var_column.tolist(), axis_var_row.tolist(), axis_var_flatted],
        "standard deviation" : [axis_std_column.tolist(), axis_std_row.tolist(), axis_std_flatted],
        "max" : [axis_max_column.tolist(), axis_max_row.tolist(), axis_max_flatted],
        "min" : [axis_min_column.tolist(), axis_min_row.tolist(), axis_min_flatted],
        "sum": [axis_sums_column.tolist(), axis_sums_row.tolist(), axis_sums_flatted]
    }

    return calculations