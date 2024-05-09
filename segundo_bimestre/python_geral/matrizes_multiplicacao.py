# CLASSE DAS MATRIZES
class Mat(list):
    def __matmul__(self, B):
        A = self
        return Mat([[sum(A[i][k]*B[k][j] for k in range(len(B)))
                    for j in range(len(B[0])) ] for i in range(len(A))])

# DEFINIÇÃO DAS MATRIZES
A = Mat([[1,2], [3,4]])
B = Mat([[4,3], [2,1]])

C = (A @ B)

print(f"MULTIPLICAÇÃO DAS MATRIZES {A} e {B}")
for i in range(2):
    for j in range(2):
        print(C[i][j], end=" ")
    print()