import math
import statistics

def zScore(y,mu,sigma):
    z=(y-mu)/sigma
    z=round(z,2)
    return z

def normpdf(z,mu=0,sigma=1):
    c=1/(sigma*math.sqrt(2*math.pi))
    exp= -1*( (z-mu)**2)/(2*(sigma**2))
    
    p=c*(math.e**exp)
    return round(p,3)

def normcdf(z1,z2,mu=0,sigma=1):
    z=z1;p=0;dz=.001
    while (z>=z1 and z<=z2):
        c=1/(sigma*math.sqrt(2*math.pi))
        exp= -1*( (z-mu)**2)/(2*(sigma**2))
    
        p+=c*(math.e**exp) * dz #eqn for normalpdf integrated over dz
        z+=dz
    return round(p,3)

def invNorm(p,mu=0,sigma=1):

    
    z = mu + sigma * z #adjusting if not standard normal model
    return round(z,3)

if __name__ == "__main__":
    print(normcdf(-99,2))
    print(invNorm(.55))