import sys
import time

def progress(percent=0, width=110):
    left = width * percent // 100
    right = width - left

    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

def startAnimations():
    print('\n')
    print('█ █▄░█ █ ▀█▀ █ ▄▀█ █░░ █ ▀█ █ █▄░█ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀')
    print('█ █░▀█ █ ░█░ █ █▀█ █▄▄ █ █▄ █ █░▀█ █▄█   █▄█ █▀█ █░▀░█ ██▄')
    print('\n')

    for i in range(101):
        progress(i)
        time.sleep(0.02)

    print('\n')

    print('█ █▄░█ █ ▀█▀ █ ▄▀█ █░░ █ ▀█ █ █▄░█ █▀▀    █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀ █▀▄')
    print('█ █░▀█ █ ░█░ █ █▀█ █▄▄ █ █▄ █ █░▀█ █▄█    █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄ █▄▀')

    print('\n')

    time.sleep(2)

    print('▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄')
    print('░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░')
    print('\n')

    time.sleep(2)

    print('█▄▄ █▀█ █ █▄░█ █▀▀ █ █▄░█ █▀▀   ▀█▀ █▀█   █░░ █ █▀▀ █▀▀')
    print('█▄█ █▀▄ █ █░▀█ █▄█ █ █░▀█ █▄█   ░█░ █▄█   █▄▄ █ █▀░ ██▄')
    print('\n')

    for i in range(101):
        progress(i)
        time.sleep(0.01)

    print('\n')
    print('\n')
    print('\n')

    print('█ █▄░█ █▀ ▀█▀ █▀█ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀ ▄')
    print('█ █░▀█ ▄█ ░█░ █▀▄ █▄█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█ ▄ \n')
    print('    Key in the country when prompted. \n\
    If the answer is correct and the country have \n\
    not been key in before, \n\
    you would see "Country Available" \n\
    Wrong / keyed in answers will lead to the program \n\
    showing an error message \n\
    No Chinese accepted \n\
    (Spelling mistakes will be marked as wrong) \n \n')

    print('█▀█ █▀▀ ▄▀█ █▀▄ █▄█ ▀█')
    print('█▀▄ ██▄ █▀█ █▄▀ ░█░ ░▄')
    print('\n')
    input('Type "Yes" to continue: ')
    print('\n')

    print('█▀▀█')
    print('░░▀▄')
    print('█▄▄█')
    print('\n')
    time.sleep(1)

    print('█▀█')
    print('░▄▀')
    print('█▄▄')
    print('\n')
    time.sleep(1)

    print('▄█░')
    print('░█░')
    print('▄█▄')
    print('\n')
    time.sleep(1)

startAnimations()

countriesList = ['Afghanistan',
                 'Albania',
                 'Algeria',
                 'Andorra',
                 'Angola',
                 'Antigua and Barbuda',
                 'Argentina',
                 'Armenia',
                 'Australia',
                 'Austria',
                 'Azerbaijan',
                 'Bahamas',
                 'Bahrain',
                 'Bangladesh',
                 'Barbados',
                 'Belarus',
                 'Belgium',
                 'Belize',
                 'Benin',
                 'Bhutan',
                 'Bolivia',
                 'Bosnia and Herzegovina',
                 'Botswana',
                 'Brazil',
                 'Brunei',
                 'Bulgaria',
                 'Burkina Faso',
                 'Burundi',
                 "Côte d' Ivoire",
                 'Cabo Verde',
                 'Cambodia',
                 'Cameroon',
                 'Canada',
                 'Central African Republic',
                 'Chad',
                 'Chile',
                 'China',
                 'Colombia',
                 'Comoros',
                 'Congo',
                 'Costa Rica',
                 'Croatia',
                 'Cuba',
                 'Cyprus',
                 'Czechia',
                 'Democratic Republic of the Congo',
                 'Denmark',
                 'Djibouti',
                 'Dominica',
                 'Dominican Republic',
                 'Ecuador',
                 'Egypt',
                 'El Salvador',
                 'Equatorial Guinea',
                 'Eritrea',
                 'Estonia',
                 'Eswatini',
                 'Ethiopia',
                 'Fiji',
                 'Finland',
                 'France',
                 'Gabon',
                 'Gambia',
                 'Georgia',
                 'Germany',
                 'Ghana',
                 'Greece',
                 'Grenada',
                 'Guatemala',
                 'Guinea',
                 'Guinea-Bissau',
                 'Guyana',
                 'Haiti',
                 'Holy See',
                 'Honduras',
                 'Hungary',
                 'Iceland',
                 'India',
                 'Indonesia',
                 'Iran',
                 'Iraq',
                 'Ireland',
                 'Israel',
                 'Italy',
                 'Jamaica',
                 'Japan',
                 'Jordan',
                 'Kazakhstan',
                 'Kenya',
                 'Kiribati',
                 'Kuwait',
                 'Kyrgyzstan',
                 'Laos',
                 'Latvia',
                 'Lebanon',
                 'Lesotho',
                 'Liberia',
                 'Libya',
                 'Liechtenstein',
                 'Lithuania',
                 'Luxembourg',
                 'Madagascar',
                 'Malawi',
                 'Malaysia',
                 'Maldives',
                 'Mali',
                 'Malta',
                 'Marshall Islands',
                 'Mauritania',
                 'Mauritius',
                 'Mexico',
                 'Micronesia',
                 'Moldova',
                 'Monaco',
                 'Mongolia',
                 'Montenegro',
                 'Morocco',
                 'Mozambique',
                 'Myanmar',
                 'Namibia',
                 'Nauru',
                 'Nepal',
                 'Netherlands',
                 'New Zealand',
                 'Nicaragua',
                 'Niger',
                 'Nigeria',
                 'North Korea',
                 'North Macedonia',
                 'Norway',
                 'Oman',
                 'Pakistan',
                 'Palau',
                 'Palestine State',
                 'Panama',
                 'Papua New Guinea',
                 'Paraguay',
                 'Peru',
                 'Philippines',
                 'Poland',
                 'Portugal',
                 'Qatar',
                 'Romania',
                 'Russia',
                 'Rwanda',
                 'Saint Kitts and Nevis',
                 'Saint Lucia',
                 'Saint Vincent and the Grenadines',
                 'Samoa',
                 'San Marino',
                 'Sao Tome and Principe',
                 'Saudi Arabia',
                 'Senegal',
                 'Serbia',
                 'Seychelles',
                 'Sierra Leone',
                 'Singapore',
                 'Slovakia',
                 'Slovenia',
                 'Solomon Islands',
                 'Somalia',
                 'South Africa',
                 'South Korea',
                 'South Sudan',
                 'Spain',
                 'Sri Lanka',
                 'Sudan',
                 'Suriname',
                 'Sweden',
                 'Switzerland',
                 'Syria',
                 'Tajikistan',
                 'Tanzania',
                 'Thailand',
                 'Timor Leste',
                 'Togo',
                 'Tonga',
                 'Trinidad and Tobago',
                 'Tunisia',
                 'Turkey',
                 'Turkmenistan',
                 'Tuvalu',
                 'Uganda',
                 'Ukraine',
                 'United Arab Emirates',
                 'United Kingdom',
                 'United States Of America',
                 'Uruguay',
                 'Uzbekistan',
                 'Vanuatu',
                 'Venezuela',
                 'Vietnam',
                 'Yemen',
                 'Zambia',
                 'Zimbabwe',
                 ]

countriesInput = []
while True:
    no = 0
    def rating():
        if no == 0:
            print('█▄▄ █▀█ █░█ █░█')
            print('█▄█ █▀▄ █▄█ █▀█')

        elif no <= 20:
            print('▀█▀ █▀█ █▄█   █▄▄ █▀▀ ▀█▀ ▀█▀ █▀▀ █▀█')
            print('░█░ █▀▄ ░█░   █▄█ ██▄ ░█░ ░█░ ██▄ █▀▄')

        elif no <= 50:
            print('█▄░█ █▀█ ▀█▀   █▄▄ ▄▀█ █▀▄')
            print('█░▀█ █▄█ ░█░   █▄█ █▀█ █▄▀')

        elif no <= 100:
            print('█▄░█ █ █▀▀ █▀▀')
            print('█░▀█ █ █▄▄ ██▄')

        elif no <= 150:
            print('█▀█ █▀█ █▀█ █▀▄ █ █▀▀ █▄█')
            print('█▀▀ █▀▄ █▄█ █▄▀ █ █▄█ ░█░')

        else:
            print('▄▀█ ▀█▀ █░░ ▄▀█ █▀')
            print('█▀█ ░█░ █▄▄ █▀█ ▄█')

    print('\n')
    UserInput = input('Country Input: ')
    UserInputCapitalize = UserInput.title()

    if UserInputCapitalize == 'End':
        idx = len(countriesList)
        no = 195 - idx
        print('\n')
        print(str(no) + ' / 195 countries keyed in')
        print('\n')
        print('YOUR RATING BY MACHINE:')
        rating()
        time.sleep(5)
        sys.exit()

    else:
        exist = countriesList.count(UserInputCapitalize)
        if exist > 0:
            print('\n')
            print("█▀▀ █▀█ █░█ █▄░█ ▀█▀ █▀█ █▄█   █▀▀ ▀▄▀ █ █▀ ▀█▀ █▀ █")
            print('█▄▄ █▄█ █▄█ █░▀█ ░█░ █▀▄ ░█░   ██▄ █░█ █ ▄█ ░█░ ▄█ ▄')
            countriesList.remove(UserInputCapitalize)
            countriesInput.append(UserInputCapitalize)
        else:
            keyedIn = countriesInput.count(UserInputCapitalize)
            
            if keyedIn > 0:
                print('\n')
                print('█▄▀ █▀▀ █▄█ █▀▀ █▀▄   █ █▄░█')
                print('█░█ ██▄ ░█░ ██▄ █▄▀   █ █░▀█')
                print('\n')

            else:
                print('\n')
                print('█▀▀ █▀█ █▀█ █▀█ █▀█')
                print('██▄ █▀▄ █▀▄ █▄█ █▀▄')
                print('\n')
                print("PYTHON DON'T UNDERSTAND THE INPUT")