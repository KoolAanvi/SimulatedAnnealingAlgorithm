import numpy
import matplotlib.pyplot as plt 

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(a,b):
        return (numpy.sqrt((a.x-b.x)**2 + (a.y-b.y)**2))*100
        #return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))

    def get_total_distance(coords):
        dist = 0
        for first, second in zip(coords[:1],coords[1:]):
            dist += Coordinate.get_distance(first, second)
        dist += Coordinate.get_distance(coords[0],coords[-1])
        return dist

if __name__ == '__main__':
    coords = []
    for i in range(4): #set amount of random coordinates
        coords.append(Coordinate(numpy.random.uniform(), numpy.random.uniform()))
    
    #Plot
    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    for first, second in zip(coords[:-1], coords[1:]):
        ax1.plot([first.x, second.x],[first.y, second.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x],[coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')
    

    #Simulated annealing algorithm
    cost0 = Coordinate.get_total_distance(coords)

    T = 30
    factor = 0.99
    T_init = T
    for i in range(1000):
        print(i, 'cost=', cost0)

        T = T*factor
        for j in range(100):
            r1, r2 = numpy.random.randint(0, len(coords), size=2)

            temp = coords[r1]
            coords[r1] = coords[r2]
            coords[r2] = temp

            cost1 = Coordinate.get_total_distance(coords)

            if cost1 < cost0:
                cost0 = cost1
            else:
                x = numpy.random.uniform()
                if x < numpy.exp((cost0-cost1)/T):
                    cost0 = cost1
                else:
                    temp = coords[r1]
                    coords[r1] = coords[r2]
                    coords[r2] = temp

    #Plot the result
    for first, second in zip(coords[:-1], coords[1:]):
        ax2.plot([first.x, second.x],[first.y, second.y], 'b')
    ax2.plot([coords[0].x, coords[-1].x],[coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax2.plot(c.x,c.y,'ro')
    plt.show()

