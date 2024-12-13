#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：toolset
@File    ：example.py
@Email   ：2220138602@QQ.COM
@Date    ：2024/9/3 9:56
"""

string = (
    "'head touched\r\n [0] 2040 [0] 2041 [0] 2042 [0] 2043 [0] 2044 [0] 2045 [0] 2046 [0] 2047 [0] 2048 [1235] 2049 (0)"
    "[999] 2050 [0] 2051 [0] 2052 [0] 2053 [0] 2054 [0] 2055 [0] 2056 [0] 2057 [0] 2058 [0] 2059 [0] 2060 [999] "
    "2061 (1) [0] 2062 [0] 2063 [0] 2064 [0] 2065 [0] 2066 [0] 2067 [0] 2068 [0] 2069 [0] 2070 [0] 2071 [0] "
    "2072 ["
    "0] 2073 (2) [0] 2074 [0] 2075 [0] 2076 [0] 2077 [0] 2078 [0] 2079 [0] 2080 [0] 2081 [0] 2082 [0] 2083 [0] "
    "2084"
    "[0] 2085 [0] 2086 (3) [0] 2087 [0] 2088 [0] 2089 [0] 2090 [0] 2091 [0] 2092 [0] 2093 [0] 2094 [0] 2095 [0] "
    "2096 [0] 2097 [0] 2098 [0] 2099 (4) [0] 2100 [0] 2101 [0] 2102 [0] 2103 [0] 2104 [0] 2105 [0] 2106 [0] "
    "2107 ["
    "0] 2108 [0] 2109 [0] 2110 [0] 2111 (5) [0] 2112 [0] 2113 [0] 2114 [0] 2115 [0] 2116 [0] 2117 [0] 2118 [0] "
    "2119"
    "[0] 2120 [0] 2121 [0] 2122 [0] 2123 (6) [0] 2124 [0] 2125 [0] 2126 [0] 2127 [0] 2128 [0] 2129 [0] 2130 [0] "
    "2131 [0] 2132 (7) [0] 2133 [0] 2134 [0] 2135 [0] 2136 [0] 2137 [1063] 2138 [2352] 2139 [2546] 2140 [2526] "
    "2141"
    "[2481] 2142 (8) [2445] 2143 [1826] 2144 [2190] 2145 [2231] 2146 [2213] 2147 [1802]")


def matchmaking_rounds(character_string: str):
    s_index = 0
    current_list = []
    find_result = re.findall(r'\([\d+]\)', character_string)
    for item in find_result:
        e_index = character_string.find(item, s_index)
        currents = re.findall(r'\[(.*?)\]', character_string[s_index:e_index])
        s_index = e_index + len(item)
        if item == '(0)':
            continue
        current_list.append(list(map(int, currents)))
    return current_list


if __name__ == '__main__':
    import re

    # print(re.split(r"\((.*?)\)", string))
    # 使用正则表达式切割字符串，并保留括号中的内容

    # print(matchmaking_rounds(string))
    code = 'E4 BD A8 E5 A6 88 E9 88 Bc'
    # 使用UTF-8编码将十六进制字符串转换为字符串
    print(code.encode('utf-8').decode('unicode_escape'))

