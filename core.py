# Edit by JerryZhang

from datetime import datetime

src_text = '''
Details
Title
WHO/ILO work-related burden of disease and injury: Protocol for systematic reviews of exposure to long working hours and of the effect of exposure to long working hours on stroke
Authors / creators
Descatha, Alexis 
Sembajwe, Grace 
Baer, Michael 
Boccuni, Fabio 
Di Tecco, Cristina 
Duret, Clément 
Evanoff, Bradley A. 
Gagliardi, Diana 
Ivanov, Ivan D. 
Leppink, Nancy 
Marinaccio, Alessandro 
Magnusson Hanson, Linda L. 
Ozguler, Anna 
Pega, Frank 
Pell, John 
Pico, Fernando 
Prüss-Üstün, Annette 
Ronchetti, Matteo 
Roquelaure, Yves 
Sabbath, Erika 
Stevens, Gretchen A. 
Tsutsumi, Akizumi 
Ujita, Yuka 
Iavicoli, Sergio
Is part of
Environment international, 2018-10, Vol.119, p.366-378
Subjects
Human beings 
Life sciences 
Quality-Adjusted Life Years 
Systematic reviews (Medical research) 
Work Schedule Tolerance 
World Health Organization
Description
The World Health Organization (WHO) and the International Labour Organization (ILO) are developing a joint methodology for estimating the national and global work-related burden of disease and injury (WHO/ILO joint methodology), with contributions from a large network of experts. In this paper, we present the protocol for two systematic reviews of parameters for estimating the number of deaths and disability-adjusted life years from stroke attributable to exposure to long working hours, to inform the development of the WHO/ILO joint methodology. We aim to systematically review studies on occupational exposure to long working hours (called Systematic Review 1 in the protocol) and systematically review and meta-analyse estimates of the effect of long working hours on stroke (called Systematic Review 2), applying the Navigation Guide systematic review methodology as an organizing framework, conducting both systematic reviews in tandem and in a harmonized way. Separately for Systematic Reviews 1 and 2, we will search electronic academic databases for potentially relevant records from published and unpublished studies, including Medline, EMBASE, Web of Science, CISDOC and PsychINFO. We will also search electronic grey literature databases, Internet search engines and organizational websites; hand-search reference list of previous systematic reviews and included study records; and consult additional experts. We will include working-age (≥15 years) workers in the formal and informal economy in any WHO and/or ILO Member State, but exclude children (<15 years) and unpaid domestic workers. For Systematic Review 1, we will include quantitative prevalence studies of relevant levels of occupational exposure to long working hours (i.e. 35–40, 41–48, 49–54 and ≥55 h/week) stratified by country, sex, age and industrial sector or occupation, in the years 2005–2018. For Systematic Review 2, we will include randomized controlled trials, cohort studies, case-control studies and other non-randomized intervention studies with an estimate of the relative effect of a relevant level of long working hours on the incidence of or mortality due to stroke, compared with the theoretical minimum risk exposure level (i.e. 35–40 h/week). At least two review authors will independently screen titles and abstracts against the eligibility criteria at a first stage and full texts of potentially eligible records at a second stage, followed by extraction of data from qualifying studies. At least two review authors will assess risk of bias and the quality of evidence, using the most suited tools currently available. For Systematic Review 2, if feasible, we will combine relative risks using meta-analysis. We will report results using the guidelines for accurate and transparent health estimates reporting (GATHER) for Systematic Review 1 and the preferred reporting items for systematic reviews and meta-analyses guidelines (PRISMA) for Systematic Review 2. PROSPERO registration number: CRD42017060124. •WHO and ILO are developing a joint methodology for estimating the national and global work-related burden of disease and injury•A large network of experts is contributing to this WHO/ILO joint methodologywith two systematic reviews described in this protocol.•The authors will systematically review studies on occupational exposure to long working hours (Systematic Review 1).•They will also systematically review and meta-analyse estimates of the effect of long working hours on stroke (Systematic Review 2).•The authors will develop both systematic reviews in tandem and in a harmonized way, using the Navigation Guide systematic review methodology as an organizing framework.
Publisher
Netherlands: Elsevier Ltd
Language
English
Identifier
ISSN: 0160-4120
ISSN: 1873-6750
EISSN: 1873-6750
DOI: 10.1016/j.envint.2018.06.016
PMID: 30005185
Source
Elsevier ScienceDirect Journals Complete - AutoHoldings'''

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
values = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
date = dict(zip(keys, values))
today = f'accessed {datetime.now().date().strftime("%d"f" {date.get(int(datetime.now().date().strftime("%m")[1:]))} %Y")}, '
web = f'<URL>.'

def reference (src_txt):
    title = f'\'{src_txt.split('Title\n')[1].split('\nAuthors / creators')[0]}\', '
    authors = src_txt.split('Authors / creators\n')[1].split('\nIs part of')[0]
    names = authors.split('\n')
    Name = ''
    for parts in names:
        lttrs = ''
        initials = parts.split(', ')[-1].rstrip(' ')
        lettrs = ''.join(lettr[0] for lettr in parts.split(', ')[0].split(' ')) + ', '
        if names.index(parts) == len(names) - 2:
            lettrs = lettrs.replace(', ', ' & ')
        lttrs += lettrs
        name = f'{initials}, {lttrs}'
        Name += name
    Name = Name.rstrip(', ') + ' '

    detail = src_txt.split('Is part of\n')[1].split('\nDescription')[0]
    pubdate = detail.rsplit(', ',maxsplit = 3)[1].split('-')[0] + ', '
    journal = f'\033[3m{detail.rsplit(', ',maxsplit = 3)[0]}\033[0m, '
    volnum = f'vol. {detail.rsplit(', ',maxsplit = 3)[2].split('.')[1].split(' (')[0]}, '
    try:
        detail.rsplit(', ',maxsplit = 3)[2].split('.')[-1].split(', ')[0].split('(')[1]
        num = f'num. {detail.rsplit(', ',maxsplit = 3)[2].split('.')[-1].split(' (')[-1].rstrip(')')}, '
    except IndexError:
        num = ''
    return Name + pubdate + title + journal + volnum + num + today + web
print(reference(src_text))