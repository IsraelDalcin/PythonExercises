""" ------------------------------------------DESCRIPTION-------------------------------------------------
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
----------------------------------------------------------------------------------------------------------
""" 

def format_duration(seconds):
    teste_ano = False
    teste_dia = False
    teste_hora = False
    teste_minuto = False
    
    texto = ''
    if seconds == 0:
        return 'now'
    elif seconds == 1:
        return '1 ' + 'second'
    elif seconds == 60:
        return '1 ' + 'minute'
    elif seconds == 3600:
        return '1 ' + 'hour'
    elif seconds == 86400:
        return '1 ' + 'day'
    elif seconds == 31536000:
        return '1 ' + 'year'
    
        # Verificando os anos
    if seconds > 31536000:
        if seconds // 31536000 == 1:
            texto = '1 ' + 'year' + ', '
            seconds -= 31536000
            teste_ano = True
        else:
            texto = str(seconds // 31536000) + ' years' + ', '
            seconds -= (seconds // 31536000) * 31536000
            teste_ano = True
                
    # Verificando os dias
    if seconds > 86400:
        if seconds // 86400 == 1:
            texto += '1 ' + 'day' + ', '
            seconds -= 86400
            teste_dia = True
        else:
            texto += str(seconds // 86400) + ' days' + ', '
            seconds -= (seconds // 86400) * 86400
            teste_dia = True
        
    # Verificando as horas
    if seconds > 3600:
        if seconds // 3600 == 1:
            texto += '1 ' + 'hour' + ', '
            seconds -= 3600
            teste_hora = True
        else:
            texto += str(seconds // 3600) + ' hours' + ', '
            seconds -= (seconds // 3600) * 3600
            teste_hora = True
                
    # Verificando os minutos
    if seconds > 60:
        if seconds // 60 == 1:
            if seconds % 60 == 0:
                if teste_hora == True or teste_dia == True:
                    texto = texto[0:-2]
                    texto += ' and ' + '1 ' + 'minute'    
                    seconds -= 60
                else:
                    texto += '1 ' + 'minute'
                    seconds -= 60    
            else:
                texto += '1 ' + 'minute ' + 'and '
                seconds -= 60
                teste_minuto = True
        else:
            if seconds % 60 == 0:
                if teste_hora == True or teste_dia == True:
                    texto = texto[0:-2]
                    texto += ' and ' + str(seconds // 60) + ' minutes'    
                    seconds -= (seconds // 60) * 60    
                else:
                    texto += str(seconds // 60) + ' minutes'
                    seconds -= (seconds // 60) * 60  
            else:
                texto += str(seconds // 60) + ' minutes ' + 'and '
                seconds -= (seconds // 60) * 60
                teste_minuto = True
            
    if seconds > 1:
        if teste_dia == True and teste_ano == False and teste_minuto == False:
            texto = texto[0:-2]
            texto += ' and ' + str(seconds) + ' seconds'
            return texto
        if  teste_ano == True and teste_minuto == False:
            texto = texto[0:-2]
            texto += ' and ' + str(seconds) + ' seconds'
            return texto
        if  teste_hora == True and teste_dia == False and teste_minuto == False:
            texto = texto[0:-2]
            texto += ' and ' + str(seconds) + ' seconds'
            return texto
        else:
            texto += str(seconds) + ' seconds'
    elif seconds == 1:
        if teste_dia == True and teste_ano == False and teste_hora == False:
            texto = texto[0:-2]
            texto += ' and ' + str(seconds) + ' second'
            return texto
        if teste_dia == False and teste_ano == True and teste_hora == False:
            texto = texto[0:-2]
            texto += ' and ' + str(seconds) + ' second'
            return texto
        if teste_dia == False and teste_ano == False and teste_hora == True:
            texto = texto[0:-2]
            texto += ' and ' + str(seconds) + ' second'
            return texto
        else:
            texto += str(seconds) + ' second'
    return texto