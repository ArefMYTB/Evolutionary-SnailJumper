import numpy as np
import matplotlib.pyplot as plt

file = open("myfile.txt","r")
a_string = file.readlines()
print(a_string[1])
file.close()

# numbers = np.empty((len(a_string), 3), float)
numbers = []
for i in range(len(a_string)):
    i_col = []
    for t in a_string[i].split():
        try:
            i_col.append(float(t))
        except ValueError:
            pass
    numbers.append(i_col)
    # numbers = np.append(numbers, [i_col], axis=0)

print(numbers)

# most fitness
xpoints = np.array([1, len(a_string)])
ypoints = np.array([numbers[i][0] for i in range(len(a_string))])

plt.title("Most fitness")
plt.plot(xpoints, ypoints)
plt.show()

# least fitness
xpoints = np.array([1, len(a_string)])
ypoints = np.array([numbers[i][1] for i in range(len(a_string))])

plt.title("least fitness")
plt.plot(xpoints, ypoints)
plt.show()

# most fitness
xpoints = np.array([1, len(a_string)])
ypoints = np.array([numbers[i][2] for i in range(len(a_string))])

plt.title("average fitness")
plt.plot(xpoints, ypoints)
plt.show()