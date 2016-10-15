# Optimization File
import numpy as np
from scipy import stats
# Version A
    # Step 1: take in Parser output array values
testinput = np.array([[24,213,110],[154,24,223],[87,43,201],[215,87,4],[32,127,3],[86,23,200],[14,85,135],[154,24,223],[87,43,201],[87,43,201],[215,87,4],
[86,23,200],[14,85,135],[154,24,223],[87,43,201],[87,43,201],[215,87,4]])

# Part 1: X - Y Values
    # Step 2: create a new Array
pixelated = np.array([[]])
inputlength = len(testinput)
indexarray = np.array([])
xvals = np.array([])
xvalmean = np.array([])
yvals = np.array([])
yvalmean = np.array([])
fiveadv = np.array([])
tenadv = np.array([])
fifteenadv = np.array([])

    # Step 3: base Array at 0, which corresponds to the frame rate
for i in range(0, inputlength):
    indexarray = np.append(i, indexarray)
indexarray = np.flipud(indexarray)
indexarray = indexarray.astype(int)
    # Step 4: add x and y values to Array
pixelated = np.insert(testinput, 0, indexarray, axis=1)


# Part 2: Pallet (Four Cameras)
    # Step 5: take the average of x values & y values
for i in range(0, inputlength):
    xvals = np.append(pixelated[i][1], xvals)
    # print xvals
xvalmean = np.mean(xvals)
for i in range(0, inputlength):
    yvals = np.append(pixelated[i][2], yvals)
yvalmean = np.mean(yvals)

    # Step 6: assign average value for x value for left and right projectors & y value for top and bottom projectors
pixelated = np.insert(pixelated, 4, [1], axis=1)
pixelated = np.insert(pixelated, 5, xvalmean, axis=1)
pixelated = np.insert(pixelated, 6, [2], axis=1)
pixelated = np.insert(pixelated, 7, yvalmean, axis=1)
pixelated = np.insert(pixelated, 8, [3], axis=1)
pixelated = np.insert(pixelated, 9, xvalmean, axis=1)
pixelated = np.insert(pixelated, 10, [4], axis=1)
pixelated = np.insert(pixelated, 11, yvalmean, axis=1)

# Part 3: Delay Optimization
    # Step 7: add to Array the x-value for the next five frame rates
fiveadv = np.flipud(xvals)
fiveadv = np.delete(fiveadv, [0,1,2,3,4])
fiveadv = np.append(fiveadv, [0,0,0,0,0])

tenadv = np.flipud(xvals)
tenadv = np.delete(tenadv, [0,1,2,3,4,5,6,7,8,9])
tenadv = np.append(tenadv, [0,0,0,0,0,0,0,0,0,0])

fifteenadv = np.flipud(xvals)
fifteenadv = np.delete(fifteenadv, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
fifteenadv = np.append(fifteenadv, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

pixelated = np.insert(pixelated, 12, fiveadv, axis=1)
pixelated = np.insert(pixelated, 13, tenadv, axis=1)
pixelated = np.insert(pixelated, 14, fifteenadv, axis=1)

    # Step 8: repeat for y values
fiveadv = np.flipud(yvals)
fiveadv = np.delete(fiveadv, [0,1,2,3,4])
fiveadv = np.append(fiveadv, [0,0,0,0,0])

tenadv = np.flipud(yvals)
tenadv = np.delete(tenadv, [0,1,2,3,4,5,6,7,8,9])
tenadv = np.append(tenadv, [0,0,0,0,0,0,0,0,0,0])

fifteenadv = np.flipud(yvals)
fifteenadv = np.delete(fifteenadv, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
fifteenadv = np.append(fifteenadv, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

pixelated = np.insert(pixelated, 15, fiveadv, axis=1)
pixelated = np.insert(pixelated, 16, tenadv, axis=1)
pixelated = np.insert(pixelated, 17, fifteenadv, axis=1)

print pixelated
