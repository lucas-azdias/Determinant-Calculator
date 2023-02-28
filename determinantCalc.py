while True:
    n = int(input("Type the order of the matrix: "))
    if n >= 0:
        break

m = list()
mTemp = list()

for i in range(0, n):
    while len(mTemp) != n:
        mTemp = input(f"Type the elements of the row number {i+1} (Use a comma to separate them): ").strip(" ").split(",")
    for p in range(0, n):
        m.append(float(mTemp[p]))
    mTemp = list()

#It shows the value when it's an integer as an integer, and not as a float
def showAsInt(x):
    if x.is_integer():
        return int(x)
    return x

#Ever choosing the first row (j = 0) to calculate with the Laplace's Theorem
def calcDet(m, n):

    det = float()
    mMin = list()
    mCof = list()
    mTemp = list()

    if n == 1:
        return m[0]

    j = 0

    for i in range(0, n):
        for jTemp in range(0, n):
            for iTemp in range(0, n):
                if iTemp != i and jTemp != j:
                    mTemp.append(m[iTemp + jTemp * n])
        if n == 2:
            mMin.append(mTemp[0])
        elif n == 3:
            mMin.append(mTemp[0] * mTemp[3] - mTemp[1] * mTemp[2])
        elif n >= 4:
            mMin.append(calcDet(mTemp, n - 1))
        mCof.append(mMin[i]*pow(-1, i + j))
        det += m[i + j * n] * mCof[i]

        mTemp = list()
                    
    return det

print(f"The determinant of this matrix is: {showAsInt(calcDet(m, n))}")
