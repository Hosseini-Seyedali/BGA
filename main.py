"""
Author   : Hosseini, SeyedAli
Created  : Nov6, 2022

A simulaion of electrolyte medical equipment
"""
# Define map procedures
procedures_map = {
    
    'A' : 'OFF',
    'E' : 'ON',
    'R' : 'RINSED',
    'I' : 'INSERT BLOOD SAMPLE',
    'K' : 'ANALISE',
    'O' : 'REMOVE BLOOD SAMPLE',
    'M' : 'MEASURE',
    'D' : 'DISPLAY RESULT',
    'P' : 'PRINT RESULT',
    'Q' : 'QUIT',
}

procedures_map_A = {   
    'E' : 'ON',
}

procedures_map_E = {   
    
    'A' : 'OFF',
    'R' : 'RINSED',
    'Q' : 'QUIT',
}

procedures_map_R = {
    
    'A' : 'OFF',
    'I' : 'INSERT BLOOD SAMPLE',
    'Q' : 'QUIT',
}

procedures_map_I = {

    'R' : 'RINSED',
    'K' : 'ANALYSE',
    'Q' : 'QUIT',
}

procedures_map_K = {
    
    'R' : 'RINSED',
    'O' : 'REMOVE BLOOD SAMPLE',
    'Q' : 'QUIT',
}

procedures_map_O = {
    
    'R' : 'RINSED',
    'M' : 'MEASURE',
    'Q' : 'QUIT',
}

procedures_map_M = {
    
    'R' : 'RINSED',
    'D' : 'DISPLAY RESULT',
    'P' : 'PRINT RESULT',
    'Q' : 'QUIT',
}

procedures_map_D = {
    
    'R' : 'RINSED',
    'P' : 'PRINT RESULT',
    'Q' : 'QUIT',
}

procedures_map_P = {
    
    'R' : 'RINSED',
    'Q' : 'QUIT',
}

# Switch the device ON
procedures_str_A = '\n'.join([
    f'{key} - {value}' for key, value in procedures_map_A.items()
])

selected_procedure = input(f"""\nPLEASE PRESS 'E' TO SWITCH ON: \n\n{procedures_str_A}\n""").upper()
procedure = procedures_map_A[selected_procedure]

# Based on what procedure we choose, the program show us the following procedure
# and tell us wha the next procedures are.
while True:

    if procedure == 'OFF':
        print(f'\n')
        print('>>> YOU SWITCHED OFF <<<')
        print(f'\n')
        

        procedures_str_A = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_A.items()
        ])
        
        selected_procedure = input(f"""PLEASE PRESS 'E' TO SWICH ON: \n{procedures_str_A}: \n""").upper()
        procedure = procedures_map_A[selected_procedure]
        
    elif procedure == 'ON':
        print(f'\n')
        print('>>> YOU SWITCHED ON <<<')
        print(f'\n')

        procedures_str_E = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_E.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_E}: \n""").upper()
        procedure = procedures_map_E[selected_procedure]
        
    elif procedure == 'RINSED':
        print(f'\n')
        print('>>> YOU RINSED THE MACHINE <<<')
        print(f'\n')

        procedures_str_R = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_R.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_R}: \n""").upper()
        procedure = procedures_map_R[selected_procedure]
        
    elif procedure == 'INSERT BLOOD SAMPLE':
        print(f'\n')
        print('>>> THE SAMPLE INSERTED <<<')
        print(f'\n')

        procedures_str_I = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_I.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_I}: \n""").upper()
        procedure = procedures_map_I[selected_procedure]
        
    elif procedure == 'ANALYSE':
        print(f'\n')
        print('>>> THE ANALYSIS HAS BEEN COMPLETED <<<')
        print(f'\n')

        procedures_str_K = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_K.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_K}: \n""").upper()
        procedure = procedures_map_K[selected_procedure]
        
    elif procedure == 'REMOVE BLOOD SAMPLE':
        print(f'\n')
        print('>>> THE SAMPLE REMOVED <<<')
        print(f'\n')

        procedures_str_O = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_O.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_O}: \n""").upper()
        procedure = procedures_map_O[selected_procedure]
        
    elif procedure == 'MEASURE':
        print(f'\n')
        print('>>> THE SAMPLE MEASURED <<<')
        print(f'\n')

        procedures_str_M = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_M.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_M}: \n""").upper()
        procedure = procedures_map_M[selected_procedure]
        
    elif procedure == 'DISPLAY RESULT':
        print(f'\n')
        print('>>> DISPLAY THE RESULT <<<')
        print(f'\n')

        procedures_str_D = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_D.items()
        ])
        print('***************************************************')
        print('* Serum Electrolytes     Normal Value     Results *')
        print('*-------------------------------------------------*')

        print('*      Sudium          135-145  mmol/L      141   *')
        print('*     Potassium        3.6-5.5  mmol/L      4.2   *')
        print('*      Calcium         8.8-10.7 mmol/L      9.4   *')
        print('*     Magnesium        1.4-2.7  mmol/L      2.1   *')
        print('***************************************************\n')
        
        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_D}: \n""").upper()
        procedure = procedures_map_D[selected_procedure]


    elif procedure == 'PRINT RESULT':
        print(f'\n')
        print('>>> THE RESULT HAS BEEN PRINTED <<<')
        print(f'\n')

        procedures_str_P = '\n'.join([
            f'{key} - {value}' for key, value in procedures_map_P.items()
        ])

        selected_procedure = input(f"""PLEASE INSERT THE NEXT PROCEDURE: \n{procedures_str_P}: \n""").upper()
        procedure = procedures_map_P[selected_procedure]
        
    elif procedure == 'QUIT':
        print(f'\n')
        print('>>> YOU QUITTED <<<')
        break

