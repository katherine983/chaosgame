#!/usr/bin/env python
# coding: utf-8

# # Legacy Random Number Generators
# Sources
# [1] K. Entacher, “Bad subsequences of well-known linear congruential pseudorandom number generators,” ACM Trans. Model. Comput. Simul., vol. 8, no. 1, pp. 61–70, Jan. 1998, doi: 10.1145/272991.273009.
# [2] S. K. Park and K. W. Miller, “Random number generators: good ones are hard to find,” Commun. ACM, vol. 31, no. 10, pp. 1192–1201, Oct. 1988, doi: 10.1145/63039.63042.

# By Katie Wuestney

def LCG(seed=1, **params):
    # LCG generator using the params from the pseudorandom number generator from ANSI C rand() 1990
    # seed used to function to return pseudorandom numbers or integers within a range
    x = seed
    #{'a':16807, 'b': 0, 'm': 2147483647}
    a = params.get('a', 16807)
    b = params.get('b', 0)
    m = params.get('m', 2147483647)
    def get_seed():
        return seed
    def gen():
        nonlocal x

        #one of the worst
        # a = 950706376
        # b = 0
        # m = 2**31 - 1
        x = (a*x + b) % m
        return x
    def integers(low, high=None, points=1):
        
        if high is None:
            high = low
            low = 0
        i = 0
        while i < points:
            yield low + (gen() % high)
            i += 1
    gen.get_seed = get_seed
    gen.integers = integers
    return gen

def SIMSCRIPT(seed=1):
    # proposed by Payne et al. [1969] and implemented in the SIMSCRIPT II simulation programming language
    x = seed

    def get_seed():
        return seed
    def gen():
        nonlocal x
        
        a = 630360016
        b = 0
        m = 2**31 - 1
        x = (a*x + b) % m
        return x / m
    def integers(low, high=None, points=1):
        
        if high is None:
            high = low
            low = 0
        i = 0
        while i < points:
            yield low + (gen() % high)
            i += 1
    gen.get_seed = get_seed
    gen.integers = integers
    return gen

def ANSI_C(seed=12345):
    # LCG generator using the params from the pseudorandom number generator from ANSI C rand() 1990
    # seed used to function to return pseudorandom numbers or integers within a range
    x = seed
    def get_seed():
        return seed
    def gen():
        nonlocal x

        #ANSI C rand() 1990
        a = 1103515245
        b = 12345
        m = 2**31
        x = (a*x + b) % m
        return x
    def integers(low, high=None, points=1):
        
        if high is None:
            high = low
            low = 0
        i = 0
        while i < points:
            yield low + (gen() % high)
            i += 1
    gen.get_seed = get_seed
    gen.integers = integers
    return gen

def BCSLIB(seed=0):
    # LCG generator using the params from the pseudorandom number generator implemented by Boeing Computer Services LIB
    # seed used to function to return pseudorandom numbers or integers within a range
    x = seed
    def get_seed():
        return seed
    def gen():
        nonlocal x

        #Boeing Computer Services LIB
        a = 30517578125
        b =  7261067085
        m = 2**35
        x = (a*x + b) % m
        return x
    def integers(low, high=None, points=1):
        
        if high is None:
            high = low
            low = 0
        i = 0
        while i < points:
            yield low + (gen() % high)
            i += 1
    gen.get_seed = get_seed
    gen.integers = integers
    return gen

def RANDU(seed=1):
    x = seed
    def get_seed():
        return seed
    def gen():
        nonlocal x
        a = 65539
        m = 2**31
        x = (a*x) % m
        return x
    def integers(low, high=None, points=1):
        
        if high is None:
            high = low
            low = 0
        i = 0
        while i < points:
            yield low + (gen() % high)
            i += 1
    gen.get_seed = get_seed
    gen.integers = integers
    return gen

def PASCAL(seed=1):
    x = seed
    def get_seed():
        return seed
    def gen():
        nonlocal x
        #one of the worst
        a = 129
        b = 907633385
        m = 2**32
        x = ((a*x + b) % m)
        return x 
    def integers(low, high=None, points=1):
        
        if high is None:
            high = low
            low = 0
        i = 0
        while i < points:
            yield low + (gen() % high)
            i += 1
    gen.get_seed = get_seed
    gen.integers = integers
    return gen
