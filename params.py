import json
import numpy as np

""" Parameters """
with open('parameters.json') as f:
    params = json.load(f)

if params['Sample_Solutions']['Use']:
    delta_x = 0.1
    delta_t = 0.00513
    match params['Sample_Solutions']['solution']:
        case 'default_1':
            # Physical
            a = 1
            b = 2
            L = 2
            k = 1
            # Numerical Solution Parameters
            t_final = 1
            N_t = 196
            N_x = 21
            N_p = 10
            NAME = 'default_1'
            FPS = 5
            
            def g(x: float) -> float:
                num = 0.523598775598
                return 2*np.sin(num*x+num)
            
            def u_0(t: float) -> float:
                return 1
            
            def u_L(t: float) -> float:
                return 2
        case 'pos_x_squared':
            # Physical
            a = 1
            b = 1
            L = 2
            k = 1
            # Numerical Solution Parameters
            t_final = 1
            N_t = 196
            N_x = 21
            N_p = 10
            NAME = 'pos_x_squared'
            FPS = 15
            
            def g(x: float) -> float:
                return 1-x*(x-2)
            
            def u_0(t: float) -> float:
                return 1
            
            def u_L(t: float) -> float:
                return 1
        case 'neg_x_squared':
            # Physical
            a = 1
            b = 1
            L = 2
            k = 1
            # Numerical Solution Parameters
            t_final = 1
            N_t = 196
            N_x = 21
            N_p = 10
            NAME = 'neg_x_squared'
            FPS = 15
            
            def g(x: float) -> float:
                return x*(x-2)+1
            
            def u_0(t: float) -> float:
                return 1
            
            def u_L(t: float) -> float:
                return 1
        case _ :
            raise Exception(f'no sample solution with name: {params["Sample_Solutions"]["solution"]}')
else:
    NAME = params['Solution_Name']
    # Physical
    a = params['Physical_Parameters']['a']
    b = params['Physical_Parameters']['b']
    L = params['Physical_Parameters']['L']
    k = params['Physical_Parameters']['k']

    # Solution Parameters
    t_final = params['Solution_Parameters']['final_t']
    N_t = params['Solution_Parameters']['amount_of_t_points']
    N_x = params['Solution_Parameters']['amount_of_x_points']
    N_p = params['Solution_Parameters']['partial_sum_amount']
    FPS = params['Solution_Parameters']['FPS']

    delta_x = params['Numerical_Solution_Parameters']['delta_x']
    delta_t = params['Numerical_Solution_Parameters']['delta_t']

    # Function g(x)
    def g(x: float) -> float:
        return eval(params['Physical_Parameters']['g_function'])
    
    def u_0(t: float) -> float:
        return eval(params['Numerical_Solution_Parameters']['mu_1'])
            
    def u_L(t: float) -> float:
        return eval(params['Numerical_Solution_Parameters']['mu_2'])


if __name__ == '__main__':
    print(b)
