# heat equation solution animation
This python code calculates numerical solution to heat equation and outputs an animated gif. the heat equation is
$$ u_{t}=ku_{xx}$$
with initial and boundary conditions:
$$ u(0,t)=a,\quad u(L,t)=b,\quad u(x,0)=g(x)$$
## Setup Environment
Needs python 3.10 installed, then run the command to install the dependencies
```
pip install -r requirements.txt
```

## Specify Parameters
To specify values for initial and boundary condition function open params.json and change it

## Generate Animation of the Solution
To generate the gif animation of the solution for your specified parameters run the command
```
python anim.py
```
the gif will be placed in solutions directory.

To graph each frame on the same plot run the command:
```
python heateq.py
```