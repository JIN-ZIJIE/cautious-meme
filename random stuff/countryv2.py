import tkinter as tk
from tkinter import messagebox
from time import sleep

root = tk.Tk()

root.title('国家之战')

# Variables
countriesListEN = ['Afghanistan',
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
                   'Czech Replublic',
                   'Democratic Republic Of The Congo',
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
                   'Guinea-bissau',
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
                   'Saint Kitts And Nevis',
                   'Saint Lucia',
                   'Saint Vincent And The Grenadines',
                   'Samoa',
                   'San Marino',
                   'Sao Tome And Principe',
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
                   'Trinidad And Tobago',
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
countriesListCN = [
    '阿富汗',
    '阿尔巴尼亚',
    '阿尔及利亚',
    '安道尔',
    '安哥拉',
    '安提瓜和巴布达',
    '阿根廷',
    '亚美尼亚',
    '澳大利亚',
    '奥地利',
    '阿塞拜疆',
    '巴哈马',
    '巴林',
    '孟加拉国',
    '巴巴多斯',
    '白俄罗斯',
    '比利时',
    '伯利兹',
    '贝宁',
    '不丹',
    '玻利维亚',
    '波斯尼亚和黑塞哥维那',
    '博茨瓦纳',
    '巴西',
    '文莱',
    '保加利亚',
    '布基纳法索',
    '布隆迪',
    '科特迪瓦',
    '佛得角',
    '柬埔寨',
    '喀麦隆',
    '加拿大',
    '中非共和国',
    '乍得',
    '智利',
    '中国',
    '哥伦比亚',
    '科摩罗',
    '刚果',
    '哥斯达黎加',
    '克罗地亚',
    '古巴',
    '塞浦路斯',
    '捷克共和国',
    '刚果民主共和国',
    '丹麦',
    '吉布提',
    '多米尼克',
    '多明尼加共和国',
    '厄瓜多尔',
    '埃及',
    '萨尔瓦多',
    '赤道几内亚',
    '厄立特里亚',
    '爱沙尼亚',
    '斯威士兰',
    '埃塞俄比亚',
    '斐济',
    '芬兰',
    '法国',
    '加蓬',
    '冈比亚',
    '乔治亚州',
    '德国',
    '加纳',
    '希腊',
    '格林纳达',
    '危地马拉',
    '几内亚',
    '几内亚比绍',
    '圭亚那',
    '海地',
    '教廷',
    '洪都拉斯',
    '匈牙利',
    '冰岛',
    '印度',
    '印度尼西亚',
    '伊朗',
    '伊拉克',
    '爱尔兰',
    '以色列',
    '意大利',
    '牙买加',
    '日本',
    '约旦',
    '哈萨克斯坦',
    '肯尼亚',
    '基里巴斯',
    '科威特',
    '吉尔吉斯斯坦',
    '老挝',
    '拉脱维亚',
    '黎巴嫩',
    '莱索托',
    '利比里亚',
    '利比亚',
    '列支敦士登',
    '立陶宛',
    '卢森堡',
    '马达加斯加',
    '马拉维',
    '马来西亚',
    '马尔代夫',
    '马里',
    '马耳他',
    '马绍尔群岛',
    '毛里塔尼亚',
    '毛里求斯',
    '墨西哥',
    '密克罗尼西亚',
    '摩尔多瓦',
    '摩纳哥',
    '蒙古',
    '黑山',
    '摩洛哥',
    '莫桑比克',
    '缅甸',
    '纳米比亚',
    '瑙鲁',
    '尼泊尔',
    '荷兰',
    '新西兰',
    '尼加拉瓜',
    '尼日尔',
    '尼日利亚',
    '朝鲜',
    '北马其顿',
    '挪威',
    '阿曼',
    '巴基斯坦',
    '帕劳',
    '巴勒斯坦国',
    '巴拿马',
    '巴布亚新几内亚',
    '巴拉圭',
    '秘鲁',
    '菲律宾',
    '波兰',
    '葡萄牙',
    '卡塔尔',
    '罗马尼亚',
    '俄罗斯',
    '卢旺达',
    '圣基茨和尼维斯',
    '圣卢西亚',
    '圣文森特和格林纳丁斯',
    '萨摩亚',
    '圣马力诺',
    '圣多美和普林西比',
    '沙特阿拉伯',
    '塞内加尔',
    '塞尔维亚',
    '塞舌尔',
    '塞拉利昂',
    '新加坡',
    '斯洛伐克',
    '斯洛文尼亚',
    '所罗门群岛',
    '索马里',
    '南非',
    '韩国',
    '南苏丹',
    '西班牙',
    '斯里兰卡',
    '苏丹',
    '苏里南',
    '瑞典',
    '瑞士',
    '叙利亚',
    '塔吉克斯坦',
    '坦桑尼亚',
    '泰国',
    '东帝汶',
    '多哥',
    '汤加',
    '特立尼达和多巴哥',
    '突尼斯',
    '土耳其',
    '土库曼斯坦',
    '图瓦卢',
    '乌干达',
    '乌克兰',
    '阿拉伯联合酋长国',
    '英国',
    '美国',
    '乌拉圭',
    '乌兹别克斯坦',
    '瓦努阿图',
    '委内瑞拉',
    '越南',
    '也门',
    '赞比亚',
    '津巴布韦',
]

labelCountryList = []
countriesInput = []
UserInputCapitalize = ''

# Screen
canvas1 = tk.Canvas(root, width=600, height=350, bg='#e7f5ff')
canvas1.pack()

# Labels
labelTop = tk.Label(root, text='Country Input / 输入国家', bg='#e7f5ff')
labelTop.config(font=('helvetica', 20))
canvas1.create_window(200, 25, window=labelTop)

labelBottom1 = tk.Label(root, text=(UserInputCapitalize), bg='#e7f5ff')
labelBottom1.config(font=('helvetica', 14))
canvas1.create_window(200, 230, window=labelBottom1)

labelBottom2 = tk.Label(root, text=(UserInputCapitalize), bg='#e7f5ff')
labelBottom2.config(font=('helvetica', 14))
canvas1.create_window(200, 270, window=labelBottom2)

# Side List
labelCountryList = tk.Listbox(root, listvariable='', bg='#e7f5ff', height=18)
labelCountryList.config(font=('helvetica', 12))
canvas1.create_window(480, 175, window=labelCountryList)

# Input Field
inputfield = tk.Entry(root, bg='#bac8ff', font=('helvetica', 16))
canvas1.create_window(200, 140, window=inputfield)

root.resizable(False, False)

# functions
def clear_text():
    inputfield.delete(0, 1000)


def result(UserInputCapitalize):
    UserInput = inputfield.get()
    UserInputCapitalize = UserInput.title()
    
    global idx

    if UserInputCapitalize == 'End':
        idx = len(countriesListEN)
        no = 195 - idx
        end1 = str(no) + ' / 195 countries keyed in'
        end2 = '输入了 ' + str(no) + ' / 195 个国家'
        tk.messagebox.showinfo(title='游戏结束', message=end1 + '\n' + '\n' + end2)

        sleep(1)
        root.destroy()

    elif UserInputCapitalize == 'No Of Country':
        idx = len(countriesListEN)
        no = 195 - idx
        end1 = str(no) + ' / 195 countries keyed in'
        end2 = '输入了 ' + str(no) + ' / 195 个国家'
        tk.messagebox.showinfo(title='Info', message=end1 + '\n' + '\n' + end2)

    else:
        existEN = countriesListEN.count(UserInputCapitalize)
        existCN = countriesListCN.count(UserInputCapitalize)

        # Checks for english countries
        if existEN > 0:
            tmp = ''

            # shows country exists
            labelBottom1.config(text='Country Exists!')
            labelBottom2.config(text='国家存在！')

            # remove it in chinese list
            ListIdx = countriesListEN.index(UserInputCapitalize)
            tmp = countriesListCN[ListIdx]
            countriesListCN.pop(ListIdx)

            # remove in english list
            countriesListEN.remove(UserInputCapitalize)

            # add into input list
            countriesInput.append(UserInputCapitalize)
            countriesInput.append(tmp)

            # adds it into listbox
            var = tk.StringVar(value=countriesInput)
            labelCountryList.config(listvariable=var)

        # Does checks if country is chinese
        elif existCN > 0:
            tmp = ''

            # shows country exists
            labelBottom1.config(text='Country Exists!')
            labelBottom2.config(text='国家存在！')

            # remove it in english list
            ListIdx = countriesListCN.index(UserInputCapitalize)
            tmp = countriesListEN[ListIdx]
            countriesListEN.pop(ListIdx)

            # remove in chinese list
            countriesListCN.remove(UserInputCapitalize)

            # add into input list
            countriesInput.append(UserInputCapitalize)
            countriesInput.append(tmp)

            # adds it into listbox
            var = tk.StringVar(value=countriesInput)
            labelCountryList.config(listvariable=var)

        else:
            keyedIn = countriesInput.count(UserInputCapitalize)

            if keyedIn > 0:
                labelBottom1.config(text='Country Keyed In')
                labelBottom2.config(text='国家已被输入')

            else:
                labelBottom1.config(text='No such Country')
                labelBottom2.config(text='此国家不存在')

    clear_text()
    return(UserInputCapitalize)


button1 = tk.Button(text='Check Answer / 检查答案', command=lambda: result(UserInputCapitalize),
                    bg='#4dabf7', fg='white', font=('helvetica', 12, 'bold'))
inputfield.bind('<Return>', result)

canvas1.create_window(200, 180, window=button1)

root.mainloop()