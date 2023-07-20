def romanToInt(self, s: str) -> int:
        symbol = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD": 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000
        }
        
        x = 0
        i = len(s) - 1 
        while i-1 >= 0: 
            try:
                x += symbol[s[i-1] + s[i]]
                i -= 2
            except:
                x += symbol[s[i]]
                i -= 1
                
        if i == 0:
            x+= symbol[s[i]]
        
        return x
