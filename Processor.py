import numpy as np
import cv2
import pickle

filename = "C:/Users/v_sam/Documents/PxlRT/FilesToPrint/list_save_test.pkl"
dump_directory = "C:/Users/v_sam/Documents/PxlRT/FilesToPrint/"
original_list = pickle.load(open(filename, "rb"))
np_original_list = np.array(original_list)

number_colours = np_original_list.max()

multiplier = int(255 / number_colours)

scaled_array = np_original_list * multiplier
# backtorgb = cv2.cvtColor(scaled_array,cv2.COLOR_GRAY2RGB)

print(scaled_array)

cv2.imwrite(dump_directory + "test_image_full.jpg", scaled_array)

size_x = 12
size_y = 12

width = scaled_array.shape[1]
height = scaled_array.shape[0]

full_sections_x = int(width / size_x)
partial_sections_x = 1 if (width % size_x) > 0 else 0

full_sections_y = int(height / size_y)
partial_sections_y = 1 if (height % size_y) > 0 else 0

for row in range(full_sections_y + partial_sections_y):
    start_row = row * size_y
    end_row = ((row + 1) * size_y) if ((row + 1) * size_y) <= height else (height + 1)
    for col in range(full_sections_x + partial_sections_x):
        start_col = col * size_x
        end_col = ((col + 1) * size_x) if ((col + 1) * size_x) <= width else (width + 1)

        sub_array = np.flip(np_original_list[start_row:end_row, start_col:end_col], 1)
        sub_array_list = sub_array.tolist()
        sub_scaled_array = scaled_array[start_row:end_row, start_col:end_col]

        save_filename = dump_directory + "print_new_list_row" + str(row) + "_col" + str(col) + ".pkl"
        pickle_out = open(save_filename, "wb")
        pickle.dump(sub_array_list, pickle_out)
        pickle_out.close()

        save_filename = dump_directory + "view_new_list_row" + str(row) + "_col" + str(col) + ".pkl"
        pickle_out = open(save_filename, "wb")
        pickle.dump(sub_scaled_array, pickle_out)
        pickle_out.close()

        save_filename = dump_directory + "jpg_new_list_row" + str(row) + "_col" + str(col) + ".jpg"
        cv2.imwrite(save_filename, sub_scaled_array)
