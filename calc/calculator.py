def calculate(grades, syllabus):
    s1_s2 = (syllabus['s1_s2']['c101']   * float(grades['g_101'])    + \
             syllabus['s1_s2']['c102']   * float(grades['g_102'])    + \
             syllabus['s1_s2']['c103']   * float(grades['g_103'])    + \
             syllabus['s1_s2']['c103P']  * float(grades['g_103P'])   + \
             syllabus['s1_s2']['c104']   * float(grades['g_104'])    + \
             syllabus['s1_s2']['c104P']  * float(grades['g_104P'])    + \
             syllabus['s1_s2']['c105']   * float(grades['g_105'])    + \
             syllabus['s1_s2']['c106']   * float(grades['g_106'])    + \
             syllabus['s1_s2']['c107']   * float(grades['g_107'])    + \
             syllabus['s1_s2']['c108']   * float(grades['g_108'])    + \
             syllabus['s1_s2']['c109P']  * float(grades['g_109P'])   + \
             syllabus['s1_s2']['c110AP'] * float(grades['g_110AP'])  + \
             syllabus['s1_s2']['c110BP'] * float(grades['g_110BP'])) / syllabus['s1_s2']['credits']

    s3 = (syllabus['s3']['c301']   * float(grades['g_301'])   + \
          syllabus['s3']['c302']   * float(grades['g_302'])   + \
          syllabus['s3']['c303']   * float(grades['g_303'])   + \
          syllabus['s3']['c304']   * float(grades['g_304'])   + \
          syllabus['s3']['c305']   * float(grades['g_305'])   + \
          syllabus['s3']['c306']   * float(grades['g_306'])   + \
          syllabus['s3']['c307P']  * float(grades['g_307P'])  + \
          syllabus['s3']['c308P']  * float(grades['g_308P'])) / syllabus['s3']['credits']
    
    s4 = (syllabus['s4']['c401']   * float(grades['g_401'])   + \
          syllabus['s4']['c402']   * float(grades['g_402'])   + \
          syllabus['s4']['c403']   * float(grades['g_403'])   + \
          syllabus['s4']['c404']   * float(grades['g_404'])   + \
          syllabus['s4']['c405']   * float(grades['g_405'])   + \
          syllabus['s4']['c406']   * float(grades['g_406'])   + \
          syllabus['s4']['c407P']  * float(grades['g_407P'])  + \
          syllabus['s4']['c408P']  * float(grades['g_408P'])) / syllabus['s4']['credits']
    
    s5 = (syllabus['s5']['c501']   * float(grades['g_501'])   + \
          syllabus['s5']['c502']   * float(grades['g_502'])   + \
          syllabus['s5']['c503']   * float(grades['g_503'])   + \
          syllabus['s5']['c504']   * float(grades['g_504'])   + \
          syllabus['s5']['c505']   * float(grades['g_505'])   + \
          syllabus['s5']['c506']   * float(grades['g_506'])   + \
          syllabus['s5']['c507P']  * float(grades['g_507P'])  + \
          syllabus['s5']['c508P']  * float(grades['g_508P'])) / syllabus['s5']['credits']

    s6 = (syllabus['s6']['c601']   * float(grades['g_601'])   + \
          syllabus['s6']['c602']   * float(grades['g_602'])   + \
          syllabus['s6']['c603']   * float(grades['g_603'])   + \
          syllabus['s6']['c604']   * float(grades['g_604'])   + \
          syllabus['s6']['c605']   * float(grades['g_605'])   + \
          syllabus['s6']['cL01']   * float(grades['g_L01'])   + \
          syllabus['s6']['c607P']  * float(grades['g_607P'])  + \
          syllabus['s6']['c608P']  * float(grades['g_608P'])) / syllabus['s6']['credits']

    s7 = (syllabus['s7']['c701']   * float(grades['g_701'])   + \
          syllabus['s7']['c702']   * float(grades['g_702'])   + \
          syllabus['s7']['c703']   * float(grades['g_703'])   + \
          syllabus['s7']['c704']   * float(grades['g_704'])   + \
          syllabus['s7']['cL02']   * float(grades['g_L02'])   + \
          syllabus['s7']['cL03']   * float(grades['g_L03'])   + \
          syllabus['s7']['c707P']  * float(grades['g_707P'])  + \
          syllabus['s7']['c708P']  * float(grades['g_708P'])  + \
          syllabus['s7']['c709P']  * float(grades['g_709P'])) / syllabus['s7']['credits']

    s8 = (syllabus['s8']['c801']   * float(grades['g_801'])   + \
          syllabus['s8']['c802']   * float(grades['g_802'])   + \
          syllabus['s8']['cL04']   * float(grades['g_L04'])   + \
          syllabus['s8']['cL05']   * float(grades['g_L05'])   + \
          syllabus['s8']['c805P']  * float(grades['g_805P'])  + \
          syllabus['s8']['c806P']  * float(grades['g_806P'])  + \
          syllabus['s8']['c807P']  * float(grades['g_807P'])) / syllabus['s8']['credits']
    
    cgpa = (s1_s2 * syllabus['s1_s2']['credits'] + \
            s3 * syllabus['s3']['credits']  + \
            s4 * syllabus['s4']['credits']  + \
            s5 * syllabus['s5']['credits']  + \
            s6 * syllabus['s6']['credits']  + \
            s7 * syllabus['s7']['credits']  + \
            s8 * syllabus['s8']['credits']) / syllabus['credits']
    
    if (cgpa - 0.5)*10 < 0:
        percentage = 0
    else:
        percentage = (cgpa - 0.5)*10

    return {'cgpa' : round(cgpa, 2), 's1_s2' : round(s1_s2, 2),
            's3'   : round(s3, 2),   's4'    : round(s4, 2),
            's5'   : round(s5, 2),   's6'    : round(s6, 2),
            's7'   : round(s7, 2),   's8'    : round(s8, 2),
            'percentage' : percentage}
