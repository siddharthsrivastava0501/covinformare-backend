from flask import Flask

app = Flask(__name__)

article = { 'GB': { 'general': 'https://www.nhs.uk/conditions/coronavirus-covid-19/', 'vaccine': 'https://www.nhs.uk/conditions/coronavirus-covid-19/coronavirus-vaccination/', 'masks': 'https://www.gov.uk/government/publications/face-coverings-when-to-wear-one-and-how-to-make-your-own/face-coverings-when-to-wear-one-and-how-to-make-your-own', 'selfisolation': 'https://www.nhs.uk/conditions/coronavirus-covid-19/self-isolation-and-treatment/'},
            'US': { 'general': 'https://www.cdc.gov/coronavirus/2019-ncov/index.html', 'vaccine': 'https://www.cdc.gov/coronavirus/2019-ncov/vaccines/', 'masks': 'https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/diy-cloth-face-coverings.html', 'selfisolation': 'https://www.cdc.gov/coronavirus/2019-ncov/your-health/quarantine-isolation.html'},
            'CA': { 'general': 'https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html', 'vaccine': 'https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/vaccines.html', 'masks': 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/prevention-risks/about-non-medical-masks-face-coverings.html', 'selfisolation': 'https://travel.gc.ca/travel-covid/travel-restrictions/isolation'},
            'AU': { 'general': 'https://covid19inlanguage.homeaffairs.gov.au/', 'vaccine': 'https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/covid-19-vaccines', 'masks': 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/how-to-protect-yourself-and-others-from-coronavirus-covid-19/masks', 'selfisolation': 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/how-to-protect-yourself-and-others-from-coronavirus-covid-19/isolation-for-coronavirus-covid-19'},
            'NZ': { 'general': 'https://covid19.govt.nz/', 'vaccine': 'https://covid19.govt.nz/covid-19-vaccines/', 'masks': 'https://covid19.govt.nz/health-and-wellbeing/protect-yourself-and-others-from-covid-19/wear-a-face-covering/', 'selfisolation': 'https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-health-advice-public/covid-19-self-isolation-managed-isolation-quarantine'},
            'WHO': {'general': 'https://covid19.who.int/','vaccine': "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/covid-19-vaccines", 'masks':'https://covid19.who.int/measures','selfisolation':'https://covid19.who.int/measures'}}

@app.route('/')
def default():
    return '<p> Default route </p>'


@app.route('/<country>/<type>/')
def relevantArticle(country, type):
    return article[country][type]

if __name__ == "__main__":
    app.run(debug=True)