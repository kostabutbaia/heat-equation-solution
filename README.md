# heat equation solution animation
This python code calculates numerical solution to heat equation and outputs an animated gif. the heat equation is
$$u_{t}=ku_{xx}$$
with initial and boundary conditions:
$$u(0,t)=a,\quad u(L,t)=b,\quad u(x,0)=g(x)$$
## Setup Environment
Needs python 3.10 installed, then run the command to install the dependencies
```
pip install -r requirements.txt
```

## Specify Parameters
To specify values for initial and boundary condition function open `parameters.json` and change it

### Sample Solutions
You can try sample solutions which are already in the code, in json set `Use` to true and for example try `default_1`
```json
"Sample_Solutions": {
    "Use": true,
    "solution": "default_1"
},
```
There are 3 sample solutions: `default_1`, `pos_x_squared` and `neg_x_squared`
### Custom Solution
Set `Use` for sample to false and specify your own parameters, for example
```json
{   
    "Sample_Solutions": {
        "Use": false,
        "solution": "default_1"
    },
    "Solution_Name": "custom",
    "Physical_Parameters": {
        "a": 1,
        "b": 1,
        "L": 2,
        "k": 1,
        "g_function": "1-x*(x-2)"
    },
    "Numerical_Solution_Parameters": {
        "amount_of_x_points": 30,
        "amount_of_t_points": 100,
        "final_t": 1,
        "partial_sum_amount": 10,
        "FPS": 15
    }
}
```
For large `amount_of_x_points`, `amount_of_t_points` and `partial_sum_amount` the code takes long time to compute the solution 

## Animation and Graph of the Solution
To generate the gif animation of the solution for your specified parameters run the command
```
python anim.py
```
The gif will be placed in solutions directory.

To graph each frame on the same plot run the command:
```
python heateq.py
```
For 3d surface plot of $u(x,t)$ run the command
```
python 3dgraph.py
```