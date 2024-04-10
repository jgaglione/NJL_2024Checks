# This file was automatically created by FeynRules 2.3.48
# Mathematica version: 12.3.1 for Mac OS X ARM (64-bit) (July 8, 2021)
# Date: Fri 26 Aug 2022 13:24:43


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.Pi53due__tilde__,P.c):'((-MassB**2 + MM**2)*(-3*MassB**2*Ypi53**2 + 3*MM**2*Ypi53**2))/(32.*cmath.pi*abs(MM)**3)',
                                            (P.Pid23due__tilde__,P.s):'((-MassB**2 + MM**2)*(-3*MassB**2*Ypid23**2 + 3*MM**2*Ypid23**2))/(32.*cmath.pi*abs(MM)**3)',
                                            (P.W__minus__,P.vm):'((MM**2 - MW**2)*((ee**2*MM**2)/(2.*sw**2) + (ee**2*MM**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MM)**3)'})

Decay_Pi13due = Decay(name = 'Decay_Pi13due',
                      particle = P.Pi13due,
                      partial_widths = {(P.s,P.vm__tilde__):'(MassB**4*Ypi13**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pi13tre = Decay(name = 'Decay_Pi13tre',
                      particle = P.Pi13tre,
                      partial_widths = {(P.b,P.vt__tilde__):'(MassB**4*Ypi13**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pi13uno = Decay(name = 'Decay_Pi13uno',
                      particle = P.Pi13uno,
                      partial_widths = {(P.d,P.ve__tilde__):'(MassB**4*Ypi13**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pi53due = Decay(name = 'Decay_Pi53due',
                      particle = P.Pi53due,
                      partial_widths = {(P.c,P.mu__plus__):'((MassB**2 - MM**2)*(3*MassB**2*Ypi53**2 - 3*MM**2*Ypi53**2))/(48.*cmath.pi*abs(MassB)**3)'})

Decay_Pi53tre = Decay(name = 'Decay_Pi53tre',
                      particle = P.Pi53tre,
                      partial_widths = {(P.t,P.ta__plus__):'((3*MassB**2*Ypi53**2 - 3*MT**2*Ypi53**2 - 3*MTA**2*Ypi53**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MT**2 + MT**4 - 2*MassB**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MassB)**3)'})

Decay_Pi53uno = Decay(name = 'Decay_Pi53uno',
                      particle = P.Pi53uno,
                      partial_widths = {(P.u,P.e__plus__):'(MassB**4*Ypi53**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Pid23due = Decay(name = 'Decay_Pid23due',
                       particle = P.Pid23due,
                       partial_widths = {(P.s,P.mu__plus__):'((MassB**2 - MM**2)*(3*MassB**2*Ypid23**2 - 3*MM**2*Ypid23**2))/(48.*cmath.pi*abs(MassB)**3)'})

Decay_Pid23tre = Decay(name = 'Decay_Pid23tre',
                       particle = P.Pid23tre,
                       partial_widths = {(P.b,P.ta__plus__):'((MassB**2 - MTA**2)*(3*MassB**2*Ypid23**2 - 3*MTA**2*Ypid23**2))/(48.*cmath.pi*abs(MassB)**3)'})

Decay_Pid23uno = Decay(name = 'Decay_Pid23uno',
                       particle = P.Pid23uno,
                       partial_widths = {(P.d,P.e__plus__):'(MassB**4*Ypid23**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Piu23due = Decay(name = 'Decay_Piu23due',
                       particle = P.Piu23due,
                       partial_widths = {(P.c,P.vm__tilde__):'(MassB**4*Ypiu23**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_Piu23tre = Decay(name = 'Decay_Piu23tre',
                       particle = P.Piu23tre,
                       partial_widths = {(P.t,P.vt__tilde__):'((MassB**2 - MT**2)*(3*MassB**2*Ypiu23**2 - 3*MT**2*Ypiu23**2))/(48.*cmath.pi*abs(MassB)**3)'})

Decay_Piu23uno = Decay(name = 'Decay_Piu23uno',
                       particle = P.Piu23uno,
                       partial_widths = {(P.u,P.ve__tilde__):'(MassB**4*Ypiu23**2)/(16.*cmath.pi*abs(MassB)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.Pi53tre,P.ta__minus__):'((-3*MassB**2*Ypi53**2 + 3*MT**2*Ypi53**2 + 3*MTA**2*Ypi53**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MT**2 + MT**4 - 2*MassB**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Piu23tre,P.vt):'((-MassB**2 + MT**2)*(-3*MassB**2*Ypiu23**2 + 3*MT**2*Ypiu23**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.Pi53tre__tilde__,P.t):'((-3*MassB**2*Ypi53**2 + 3*MT**2*Ypi53**2 + 3*MTA**2*Ypi53**2)*cmath.sqrt(MassB**4 - 2*MassB**2*MT**2 + MT**4 - 2*MassB**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.Pid23tre__tilde__,P.b):'((-MassB**2 + MTA**2)*(-3*MassB**2*Ypid23**2 + 3*MTA**2*Ypid23**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.Pi13due__tilde__,P.Piu23due):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi13tre__tilde__,P.Piu23tre):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi13uno__tilde__,P.Piu23uno):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi53due,P.Pid23due__tilde__):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi53tre,P.Pid23tre__tilde__):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi53uno,P.Pid23uno__tilde__):'(((-6*ee**2*MassB**2)/sw**2 + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MassB**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MM**2 + MW**2)*(-0.5*(ee**2*MM**2)/sw**2 - (ee**2*MM**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MM**2 - ee**2*MZ**2 - (cw**2*ee**2*MM**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MM**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MM**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi13due__tilde__,P.Pi13due):'((-2*ee**2*MassB**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi13tre__tilde__,P.Pi13tre):'((-2*ee**2*MassB**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi13uno__tilde__,P.Pi13uno):'((-2*ee**2*MassB**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi53due__tilde__,P.Pi53due):'((14*ee**2*MassB**2 - (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi53tre__tilde__,P.Pi53tre):'((14*ee**2*MassB**2 - (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi53uno__tilde__,P.Pi53uno):'((14*ee**2*MassB**2 - (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pid23due__tilde__,P.Pid23due):'((-14*ee**2*MassB**2 + (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pid23tre__tilde__,P.Pid23tre):'((-14*ee**2*MassB**2 + (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pid23uno__tilde__,P.Pid23uno):'((-14*ee**2*MassB**2 + (7*ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (49*ee**2*MassB**2*sw**2)/(3.*cw**2) + (49*ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Piu23due__tilde__,P.Piu23due):'((2*ee**2*MassB**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Piu23tre__tilde__,P.Piu23tre):'((2*ee**2*MassB**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Piu23uno__tilde__,P.Piu23uno):'((2*ee**2*MassB**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MassB**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MassB**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MassB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

