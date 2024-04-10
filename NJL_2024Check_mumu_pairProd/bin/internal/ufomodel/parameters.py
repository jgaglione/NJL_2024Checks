# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Fri 26 Aug 2022 13:24:43



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

lc = Parameter(name = 'lc',
               nature = 'external',
               type = 'real',
               value = 5400.,
               texname = '\\text{lc}',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

mpi = Parameter(name = 'mpi',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{mpi}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

FPi53 = Parameter(name = 'FPi53',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{FPi53}',
                  lhablock = 'FRBlock',
                  lhacode = [ 3 ])

FPi13 = Parameter(name = 'FPi13',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{FPi13}',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

FPid23 = Parameter(name = 'FPid23',
                   nature = 'external',
                   type = 'real',
                   value = 5000.,
                   texname = '\\text{FPid23}',
                   lhablock = 'FRBlock',
                   lhacode = [ 5 ])

FPiu23 = Parameter(name = 'FPiu23',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{FPiu23}',
                   lhablock = 'FRBlock',
                   lhacode = [ 6 ])

cabi2 = Parameter(name = 'cabi2',
                  nature = 'external',
                  type = 'real',
                  value = 0.227736,
                  texname = '\\text{cabi2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WPi53uno = Parameter(name = 'WPi53uno',
                     nature = 'external',
                     type = 'real',
                     value = 30,
                     texname = '\\text{WPi53uno}',
                     lhablock = 'DECAY',
                     lhacode = [ 9000006 ])

WPi13uno = Parameter(name = 'WPi13uno',
                     nature = 'external',
                     type = 'real',
                     value = 30,
                     texname = '\\text{WPi13uno}',
                     lhablock = 'DECAY',
                     lhacode = [ 9000007 ])

WPiu23uno = Parameter(name = 'WPiu23uno',
                      nature = 'external',
                      type = 'real',
                      value = 30,
                      texname = '\\text{WPiu23uno}',
                      lhablock = 'DECAY',
                      lhacode = [ 9000008 ])

WPid23uno = Parameter(name = 'WPid23uno',
                      nature = 'external',
                      type = 'real',
                      value = 30,
                      texname = '\\text{WPid23uno}',
                      lhablock = 'DECAY',
                      lhacode = [ 9000009 ])

WPi53due = Parameter(name = 'WPi53due',
                     nature = 'external',
                     type = 'real',
                     value = 30,
                     texname = '\\text{WPi53due}',
                     lhablock = 'DECAY',
                     lhacode = [ 9000010 ])

WPi13due = Parameter(name = 'WPi13due',
                     nature = 'external',
                     type = 'real',
                     value = 30,
                     texname = '\\text{WPi13due}',
                     lhablock = 'DECAY',
                     lhacode = [ 9000011 ])

WPiu23due = Parameter(name = 'WPiu23due',
                      nature = 'external',
                      type = 'real',
                      value = 30,
                      texname = '\\text{WPiu23due}',
                      lhablock = 'DECAY',
                      lhacode = [ 9000012 ])

WPid23due = Parameter(name = 'WPid23due',
                      nature = 'external',
                      type = 'real',
                      value = 30,
                      texname = '\\text{WPid23due}',
                      lhablock = 'DECAY',
                      lhacode = [ 9000013 ])

WPi53tre = Parameter(name = 'WPi53tre',
                     nature = 'external',
                     type = 'real',
                     value = 30,
                     texname = '\\text{WPi53tre}',
                     lhablock = 'DECAY',
                     lhacode = [ 9000014 ])

WPi13tre = Parameter(name = 'WPi13tre',
                     nature = 'external',
                     type = 'real',
                     value = 30,
                     texname = '\\text{WPi13tre}',
                     lhablock = 'DECAY',
                     lhacode = [ 9000015 ])

WPiu23tre = Parameter(name = 'WPiu23tre',
                      nature = 'external',
                      type = 'real',
                      value = 30,
                      texname = '\\text{WPiu23tre}',
                      lhablock = 'DECAY',
                      lhacode = [ 9000016 ])

WPid23tre = Parameter(name = 'WPid23tre',
                      nature = 'external',
                      type = 'real',
                      value = 30,
                      texname = '\\text{WPid23tre}',
                      lhablock = 'DECAY',
                      lhacode = [ 9000017 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

MassB = Parameter(name = 'MassB',
                  nature = 'internal',
                  type = 'real',
                  value = 'mpi',
                  texname = '\\text{MassB}')

ONE1x1 = Parameter(name = 'ONE1x1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE1x1}')

ONE1x2 = Parameter(name = 'ONE1x2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE1x2}')

ONE1x3 = Parameter(name = 'ONE1x3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE1x3}')

ONE2x1 = Parameter(name = 'ONE2x1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE2x1}')

ONE2x2 = Parameter(name = 'ONE2x2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE2x2}')

ONE2x3 = Parameter(name = 'ONE2x3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE2x3}')

ONE3x1 = Parameter(name = 'ONE3x1',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE3x1}')

ONE3x2 = Parameter(name = 'ONE3x2',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE3x2}')

ONE3x3 = Parameter(name = 'ONE3x3',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{ONE3x3}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

Ypi13 = Parameter(name = 'Ypi13',
                  nature = 'internal',
                  type = 'real',
                  value = 'FPi13**2/lc**2',
                  texname = '\\text{Ypi13}')

Ypi53 = Parameter(name = 'Ypi53',
                  nature = 'internal',
                  type = 'real',
                  value = 'FPi53**2/lc**2',
                  texname = '\\text{Ypi53}')

Ypid23 = Parameter(name = 'Ypid23',
                   nature = 'internal',
                   type = 'real',
                   value = 'FPid23**2/lc**2',
                   texname = '\\text{Ypid23}')

Ypiu23 = Parameter(name = 'Ypiu23',
                   nature = 'internal',
                   type = 'real',
                   value = 'FPiu23**2/lc**2',
                   texname = '\\text{Ypiu23}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

