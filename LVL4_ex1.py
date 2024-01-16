""" ------------------------------------------DESCRIPTION-------------------------------------------------

I got lots of files beginning like this:

Program title: Primes
Author: Kern
Corporation: Gold
Phone: +1-503-555-0091
Date: Tues April 9, 2005
Version: 6.7
Level: Alpha
Here we will work with strings like the string data above and not with files.

The function change(s, prog, version) given:

s=data, prog="Ladder" , version="1.1" will return:

"Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1"

Rules:

The date should always be "2019-01-01".

The author should always be "g964".

Replace the current "Program Title" with the prog argument supplied to your function. Also remove "Title", so in the example case "Program Title: Primes" becomes "Program: Ladder".

Remove the lines containing "Corporation" and "Level" completely.

Phone numbers and versions must be in valid formats.

A valid version in the input string data is one or more digits followed by a dot, followed by one or more digits. So 0.6, 5.4, 14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 1.9.9 are invalid.

A valid input phone format is +1-xxx-xxx-xxxx, where each x is a digit.

If the phone or version format is not valid, return "ERROR: VERSION or PHONE".

If the version format is valid and the version is anything other than 2.0, replace it with the version parameter supplied to your function. If it’s 2.0, don’t modify it.

If the phone number is valid, replace it with "+1-503-555-0090".

Note
You can see other examples in the "Sample tests".
----------------------------------------------------------------------------------------------------------
""" 

import re
def change(s, prog, version):
    print(s)
    print(prog)
    print(version) 
    error = 'ERROR: VERSION or PHONE'
    s_splitted = re.split(r'\n|:', s)
    s_main = dict()
    s_main ['program'] = prog
    s_main ['author'] = 'g964'
    s_main ['phone'] = s_splitted[7].strip()
    s_main ['date'] = '2019-01-01'
    s_main ['version'] = s_splitted[11].strip()
    phone_check = s_main['phone'].split('-')
    version_split = s_main['version'].split('.')
    if len(version_split) != 2 or '' in version_split:
        return error
    else:
        if s_main['version'] != '2.0':
            s_main['version'] = version
    check_phone_boolean = bool
    for e,i in enumerate(phone_check):
        if e == 0:
            if i != '+1':
                return error
                check_phone_boolean = False
        elif e < 3:
            if not i.isnumeric() or len(i) < 3:
                return error
                check_phone_boolean = False
        else:
            if not i.isnumeric() or len(i) < 4:
                return error
                check_phone_boolean = False
    if check_phone_boolean:
        s_main['phone'] = "+1-503-555-0090"
    return (f'Program: {s_main["program"]} Author: {s_main["author"]} Phone: {s_main["phone"]} Date: {s_main["date"]} Version: {s_main["version"]}')