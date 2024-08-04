#utility functions for the pattern generator

#utility when we format a link
def leftPadString(string, desiredLen, char='0'):
    if len(string) >= desiredLen:
        return string
    else:
        return (desiredLen - len(string))*char+string
