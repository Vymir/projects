inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def read_imagefile(f):
    first_line = f.readline()
    code, width, height, max_level = first_line.split()
    rest = f.read()
    vals = rest.split()
    img_matrix = []
    counter = 0
    for i in range(width):
        row = []
        for j in range(height):
            row.append(int(vals[counter]))
            counter += 1
        img_matrix.append(row)
    return img_matrix


def write_imagefile(f, img_matrix):
    width = len(img_matrix)
    height = len(img_matrix) * len(img_matrix[0])
    f.write(f"P2 {width} {height} 255\n")
    for i in img_matrix:
        for j in i:
            if j == len(img_matrix[0]):
                f.write(f"{j}\n")
            else:
                f.write(f"{j} ")


def misalign(img_matrix):
    copy_matrix = img_matrix.copy()
    for i in range(len(img_matrix) // 2):
        for j in range(len(img_matrix[0])):
            if j % 2 == 0:
                continue
            else:
                copy_matrix[i][j] = img_matrix[len(img_matrix) - i][j]
    return copy_matrix


def sort_columns(img_matrix):
    return

def sort_rows_border(img_matrix):
    return

def convolution(img_matrix, kernel):
    img_height, img_width = len(img_matrix), len(img_matrix[0])
    output_matrix = [[0 for j in range(img_width - 2)] for i in range(img_height - 2)]
    for i in range(img_height - 2):
        for j in range(img_width - 2):
            output_val = 0
            for k in range(3):
                for l in range(3):
                    output_val += kernel[k][l] * img_matrix[i + k][j + l]

            output_matrix[i][j] = output_val

    for i in range(len(output_matrix)):
        for j in range(len(output_matrix[0])):
            if output_matrix[i][j] < 0:
                output_matrix[i][j] = 0
            elif output_matrix[i][j] > 255:
                output_matrix[i][j] = 255

    return output_matrix


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
