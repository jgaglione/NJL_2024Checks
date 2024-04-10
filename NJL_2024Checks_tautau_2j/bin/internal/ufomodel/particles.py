# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Fri 26 Aug 2022 13:24:43


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 9000005,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MM,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.ZERO,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.ZERO,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Pi53uno = Particle(pdg_code = 9000006,
                   name = 'Pi53uno',
                   antiname = 'Pi53uno~',
                   spin = 1,
                   color = 3,
                   mass = Param.MassB,
                   width = Param.WPi53uno,
                   texname = 'Pi53uno',
                   antitexname = 'Pi53uno~',
                   charge = 5/3,
                   GhostNumber = 0,
                   LeptonNumber = -1,
                   Y = 0)

Pi53uno__tilde__ = Pi53uno.anti()

Pi13uno = Particle(pdg_code = 9000007,
                   name = 'Pi13uno',
                   antiname = 'Pi13uno~',
                   spin = 1,
                   color = 3,
                   mass = Param.MassB,
                   width = Param.WPi13uno,
                   texname = 'Pi13uno',
                   antitexname = 'Pi13uno~',
                   charge = -1/3,
                   GhostNumber = 0,
                   LeptonNumber = -1,
                   Y = 0)

Pi13uno__tilde__ = Pi13uno.anti()

Piu23uno = Particle(pdg_code = 9000008,
                    name = 'Piu23uno',
                    antiname = 'Piu23uno~',
                    spin = 1,
                    color = 3,
                    mass = Param.MassB,
                    width = Param.WPiu23uno,
                    texname = 'Piu23uno',
                    antitexname = 'Piu23uno~',
                    charge = 2/3,
                    GhostNumber = 0,
                    LeptonNumber = -1,
                    Y = 0)

Piu23uno__tilde__ = Piu23uno.anti()

Pid23uno = Particle(pdg_code = 9000009,
                    name = 'Pid23uno',
                    antiname = 'Pid23uno~',
                    spin = 1,
                    color = 3,
                    mass = Param.MassB,
                    width = Param.WPid23uno,
                    texname = 'Pid23uno',
                    antitexname = 'Pid23uno~',
                    charge = 2/3,
                    GhostNumber = 0,
                    LeptonNumber = -1,
                    Y = 0)

Pid23uno__tilde__ = Pid23uno.anti()

Pi53due = Particle(pdg_code = 9000010,
                   name = 'Pi53due',
                   antiname = 'Pi53due~',
                   spin = 1,
                   color = 3,
                   mass = Param.MassB,
                   width = Param.WPi53due,
                   texname = 'Pi53due',
                   antitexname = 'Pi53due~',
                   charge = 5/3,
                   GhostNumber = 0,
                   LeptonNumber = -1,
                   Y = 0)

Pi53due__tilde__ = Pi53due.anti()

Pi13due = Particle(pdg_code = 9000011,
                   name = 'Pi13due',
                   antiname = 'Pi13due~',
                   spin = 1,
                   color = 3,
                   mass = Param.MassB,
                   width = Param.WPi13due,
                   texname = 'Pi13due',
                   antitexname = 'Pi13due~',
                   charge = -1/3,
                   GhostNumber = 0,
                   LeptonNumber = -1,
                   Y = 0)

Pi13due__tilde__ = Pi13due.anti()

Piu23due = Particle(pdg_code = 9000012,
                    name = 'Piu23due',
                    antiname = 'Piu23due~',
                    spin = 1,
                    color = 3,
                    mass = Param.MassB,
                    width = Param.WPiu23due,
                    texname = 'Piu23due',
                    antitexname = 'Piu23due~',
                    charge = 2/3,
                    GhostNumber = 0,
                    LeptonNumber = -1,
                    Y = 0)

Piu23due__tilde__ = Piu23due.anti()

Pid23due = Particle(pdg_code = 9000013,
                    name = 'Pid23due',
                    antiname = 'Pid23due~',
                    spin = 1,
                    color = 3,
                    mass = Param.MassB,
                    width = Param.WPid23due,
                    texname = 'Pid23due',
                    antitexname = 'Pid23due~',
                    charge = 2/3,
                    GhostNumber = 0,
                    LeptonNumber = -1,
                    Y = 0)

Pid23due__tilde__ = Pid23due.anti()

Pi53tre = Particle(pdg_code = 9000014,
                   name = 'Pi53tre',
                   antiname = 'Pi53tre~',
                   spin = 1,
                   color = 3,
                   mass = Param.MassB,
                   width = Param.WPi53tre,
                   texname = 'Pi53tre',
                   antitexname = 'Pi53tre~',
                   charge = 5/3,
                   GhostNumber = 0,
                   LeptonNumber = -1,
                   Y = 0)

Pi53tre__tilde__ = Pi53tre.anti()

Pi13tre = Particle(pdg_code = 9000015,
                   name = 'Pi13tre',
                   antiname = 'Pi13tre~',
                   spin = 1,
                   color = 3,
                   mass = Param.MassB,
                   width = Param.WPi13tre,
                   texname = 'Pi13tre',
                   antitexname = 'Pi13tre~',
                   charge = -1/3,
                   GhostNumber = 0,
                   LeptonNumber = -1,
                   Y = 0)

Pi13tre__tilde__ = Pi13tre.anti()

Piu23tre = Particle(pdg_code = 9000016,
                    name = 'Piu23tre',
                    antiname = 'Piu23tre~',
                    spin = 1,
                    color = 3,
                    mass = Param.MassB,
                    width = Param.WPiu23tre,
                    texname = 'Piu23tre',
                    antitexname = 'Piu23tre~',
                    charge = 2/3,
                    GhostNumber = 0,
                    LeptonNumber = -1,
                    Y = 0)

Piu23tre__tilde__ = Piu23tre.anti()

Pid23tre = Particle(pdg_code = 9000017,
                    name = 'Pid23tre',
                    antiname = 'Pid23tre~',
                    spin = 1,
                    color = 3,
                    mass = Param.MassB,
                    width = Param.WPid23tre,
                    texname = 'Pid23tre',
                    antitexname = 'Pid23tre~',
                    charge = 2/3,
                    GhostNumber = 0,
                    LeptonNumber = -1,
                    Y = 0)

Pid23tre__tilde__ = Pid23tre.anti()

