import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	if padding > 0:
		padding_input = np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0)
	else:
		padding_input = input_matrix
	
	padded_height, padded_width = padding_input.shape

	output_height = (padded_height - kernel_height) // stride + 1
	output_width = (padded_width - kernel_width) // stride + 1

	output_matrix = np.zeros((output_height, output_width))

	for i in range(output_height):
		for j in range(output_width):
			h_start = i * stride
			h_end = h_start + kernel_height
			w_start = j * stride
			w_end = w_start + kernel_width

			window = padding_input[h_start:h_end, w_start:w_end]
			output_matrix[i, j] = np.sum(window * kernel)
    
	return output_matrix
