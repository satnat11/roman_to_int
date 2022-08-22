class Solutions:
    ROMAN_TO_INTEGER={
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX':9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD':400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int :
        conveter=0

        for key,value in self.ROMAN_TO_INTEGER.items():
            while s.endswith(key):
                s=s.removesuffix(key)
                conveter += value
        return conveter
s=Solutions()
str='XV'
ans=s.romanToInt(str)
print(ans)