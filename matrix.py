import random
from math import sqrt

def print_matrix(N:list):
    for i in N:
        for q in i:
            print(f"{q}", end=" ")
        print("")

def shape(N:list):
    return (len(N),len(N[0]))

def add_matrixa(A:list,B:list):
    C = copy(A)
    for i in range(shape(C)[0]):
        for j in range(shape(B)[1]):
            C[i].append(B[i][j])
    return C

def add(A:list, B:list):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    else:
        Z = []
        q = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                q.append(A[i][j] + B[i][j])
            Z.append(q)
            q = []
        return Z

def subtract(A:list, B:list):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    else:
        Z = []
        q = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                q.append(A[i][j] - B[i][j])
            Z.append(q)
            q = []
        return Z

def multiply_scalar(A:list, x:int):
    B = copy(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] *= x
    return B

def divide_scalar(A:list, x:int):
    B = copy(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] /= x
    return B

def transpose(A:list):
    Z = []
    for i in range(shape(A)[1]):
        Z.append([])
    for i in range(shape(A)[0]):
        for j in range(shape(A)[1]):
            Z[j].append(A[i][j])
    return Z

def multiply(A:list,B:list):
    if shape(A)[1] != shape(B)[0]:
        return False

    rows_A = shape(A)[0]
    cols_A = shape(A)[1]
    cols_B = shape(B)[1]

    Z = []
    for i in range(rows_A):
        q = []
        for j in range(cols_B):
            total_sum = 0
            for k in range(cols_A):
                total_sum += A[i][k] * B[k][j]
            q.append(total_sum)
        Z.append(q)
    return Z

def zeros(rows:int,colwns:int):
    Z = []
    for i in range(rows):
        q = []
        for j in range(colwns):
            q.append(0)
        Z.append(q)
    return Z

def ones(rows:int,colwns:int):
    Z = []
    for i in range(rows):
        q = []
        for j in range(colwns):
            q.append(1)
        Z.append(q)
    return Z

def identity(x):
    Z = []
    for i in range(x):
        q = []
        for j in range(x):
            q.append(0)
        Z.append(q)
    for i in range(x):
        for j in range(x):
            if i == j:
                Z[i][j] = 1
    return Z

def random_matrix(rows:int, colwns:int, a,b):
    Z = []
    for i in range(rows):
        q = []
        for j in range(colwns):
            q.append(random.randint(a,b))
        Z.append(q)
    return Z

def copy(A:list):
    B = []
    for i in range(shape(A)[0]):
        q = []
        for j in range(shape(A)[1]):
            q.append(A[i][j])
        B.append(q)
    return B

def is_square(A:list):
    if shape(A)[0] == shape(A)[1]:
        return True
    return False

def trace(A:list):
    if shape(A)[0] == shape(A)[1]:
        summ = 0
        for i in range(shape(A)[0]):
            summ += A[i][i]
        return summ
    else: return "Eblan???"

def diagonal(A:list):
    if shape(A)[0] == shape(A)[1]:
        diag = []
        for i in range(shape(A)[0]):
            diag.append(A[i][i])
        return diag
    else: return "Eblan???"

def swap_rows(A:list, first_rows:int, second_rows:int):
    B = copy(A)
    z = B[first_rows]
    B[first_rows] = B[second_rows]
    B[second_rows] = z
    return B

def get_rows(A:list,number_rows:int):
    B = copy(A)
    return B[number_rows]

def get_colums(A:list, number_colums):
    B = copy(A)
    C = []
    for i in range(shape(A)[0]):
        C.append(B[i][number_colums])
    return C

def determinant_2x2(A:list):
    B = copy(A)
    del_1 = 1
    del_2 = 1
    for i in range(shape(B)[0]):
        for j in range(shape(B)[1]):
            if i == j:
                del_1 *= B[i][j]
            else:
                del_2 *= B[i][j]
    return del_1 - del_2

def sub_matrix(A:list,number_row: int, number_colum:int):
    B = []
    for i in range(shape(A)[0]):
        q = []
        for j in range(shape(A)[1]):
            if i != number_row and j != number_colum:
                q.append(A[i][j])
        if len(q) >0:
            B.append(q)
    return B

def determinant_3x3(A:list):
    finall_deteminant = 0
    B = copy(A)
    for i in range(shape(A)[1]):
        finall_deteminant += (-1)**(1+i+1)*B[0][i]*determinant_2x2(sub_matrix(B,0,i))
    return finall_deteminant

def determinant(A:list):
    if shape(A)[0] == 1:
        final_determinant = A[0][0]
        return final_determinant
    else:
        final_determinant = 0
        for i in range(shape(A)[0]):
            final_determinant += (-1)**(1+i+1)*A[0][i]*determinant(sub_matrix(A,0,i))
        return final_determinant

def inverse(A:list):
    B = []
    det = determinant(A)
    A_T = transpose(A)
    for i in range(shape(A_T)[0]):
        q = []
        for j in range(shape(A_T)[1]):
            q.append((-1)**(i+j)*determinant(sub_matrix(A_T,i,j)))
        B.append(q)
    B = divide_scalar(B,det)
    return B


def gaussian_elimination(A: list):
    A_I = [row[:] for row in A]
    rows, cols = shape(A_I)
    for k in range(rows):
        K = A_I[k][k]
        if abs(K) < 1e-9:
            for next_row in range(k + 1, rows):
                if abs(A_I[next_row][k]) > 1e-9:
                    swap_rows(A_I, k, next_row)
                    break
            K = A_I[k][k]
        if abs(K) < 1e-9:
            continue
        A_I[k] = [x / K for x in A_I[k]]
        for i in range(k + 1, rows):
            factor = A_I[i][k]
            A_I[i] = [x - y * factor for x, y in zip(A_I[i], A_I[k])]
    return A_I

def rank(A:list):
    A_step = gaussian_elimination(A)
    rows = shape(A_step)[0]
    zero_rows_count = 0
    for row in A_step:
        if all(abs(element) < 1e-9 for element in row):
            zero_rows_count += 1
    return rows - zero_rows_count


def reverse_gaussian_elimination(A: list):
    A_I = [row[:] for row in A]
    rows, cols = shape(A_I)
    for k in range(rows - 1, -1, -1):
        K = A_I[k][k]
        if abs(K) < 1e-9:
            for next_row in range(k - 1, -1, -1):
                if abs(A_I[next_row][k]) > 1e-9:
                    swap_rows(A_I, k, next_row)
                    break
            K = A_I[k][k]
        if abs(K) < 1e-9:
            continue
        for i in range(k - 1, -1, -1):
            factor = A_I[i][k] / K
            A_I[i] = [x - y * factor for x, y in zip(A_I[i], A_I[k])]
    return A_I


def make_identity(A:list):
    A_I = copy(A)
    for k in range(0,shape(A_I)[0]):
        K = A_I[k][k]
        for i in range(len(A_I[k])):
            A_I[k][i] /= K
    return A_I


def solve(A: list, b: list):
    C = add_matrixa(A, b)
    processed_matrix = reverse_gaussian_elimination(gaussian_elimination(C))
    x = get_colums(processed_matrix, -1)
    return x

def eigenvalues_2x2(A:list):
    B = copy(A)
    if shape(A) != (2,2):
        raise ValueError("Функция для матрицы 2 на 2")
    a = B[0][0]
    d = B[1][1]

    trace = a + d
    det = determinant(B)
    D = trace**2 - 4*det
    if D < 0:
        raise ValueError("Комплексные значыения не поддерживаются")
    lambda1 = (trace + sqrt(D))/2
    lambda2 = (trace + sqrt(D))/2
    return [lambda1,lambda2]

def eigenvectors_2x2(A:list,lam: int):
    M = subtract(A, multiply_scalar(identity(2),lam))
    a,b = M[0]
    if abs(a) > 1e-12:
        y = 1
        x = -b/a
    elif abs(b)> 1e-12:
        x = 1
        y = -a/b
    else:
        # if first str = 0
        a,b = M[1]
        if abs(a) > 1e-12:
            y = 1
            x = -b / a
        elif abs(b) > 1e-12:
            x = 1
            y = -a / b
        else:
            return [1,0]
    return [x,y]




