#Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (x,y,z) on a 3D grid where the sum of i+j+k  is not equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = [x for x in range(x + 1)]
    j = [y for y in range(y + 1)]
    k = [z for z in range(z + 1)]
    results = []
    for x in i:
        for y in j:
            for z in k:
                if ((x + y + z) != n ):
                    results.append([x, y, z])
                    
    print(results)
