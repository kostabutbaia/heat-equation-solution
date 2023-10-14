import json
import numpy as np

""" Parameters """
with open('parameters.json') as f:
    params = json.load(f)

if params['Sample_Solutions']['Use']:
    match params['Sample_Solutions']['solution']:
        case 'default_1':
            # Physical
            a = 1
            b = 2
            L = 2
            k = 1
            # Numerical Solution Parameters
            t_final = 1
            N_t = 100
            N_x = 10
            N_p = 10
            NAME = 'default_1'
            FPS = 5
            
            def g(x: float) -> float:
                num = 0.523598775598
                return 2*np.sin(num*x+num)
        case _ :
            print('no such default solution')
else:
    NAME = params['Solution_Name']
    # Physical
    a = params['Physical_Parameters']['a']
    b = params['Physical_Parameters']['b']
    L = params['Physical_Parameters']['L']
    k = params['Physical_Parameters']['k']

    # Numerical Solution Parameters
    t_final = params['Numerical_Solution_Parameters']['final_t']
    N_t = params['Numerical_Solution_Parameters']['amount_of_t_points']
    N_x = params['Numerical_Solution_Parameters']['amount_of_x_points']
    N_p = params['Numerical_Solution_Parameters']['partial_sum_amount']
    FPS = params['Numerical_Solution_Parameters']['FPS']

    # Function g(x)
    def g(x: float) -> float:
        return eval(params['Physical_Parameters']['g_function'])


if __name__ == '__main__':
    print(b)
