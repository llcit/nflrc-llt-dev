# formdata.py

countries = (
	("USA", "United States of America"),
	("CAN", "Canada"),
	("AFG", "Afghanistan"),
	("ALB", "Albania"),
	("DZA", "Algeria"),
	("ASM", "American Samoa"),
	("AND", "Andorra"),
	("AGO", "Angola"),
	("AIA", "Anguilla"),
	("ATA", "Antarctica"),
	("ATG", "Antigua and Barbuda"),
	("ARG", "Argentina"),
	("ARM", "Armenia"),
	("ABW", "Aruba"),
	("AUS", "Australia"),
	("AUT", "Austria"),
	("AZE", "Azerbaijan"),
	("BHS", "Bahamas"),
	("BHR", "Bahrain"),
	("BGD", "Bangladesh"),
	("BRB", "Barbados"),
	("BLR", "Belarus"),
	("BEL", "Belgium"),
	("BLZ", "Belize"),
	("BEN", "Benin"),
	("BMU", "Bermuda"),
	("BTN", "Bhutan"),
	("BOL", "Bolivia"),
	("BIH", "Bosnia and Herzegowina"),
	("BWA", "Botswana"),
	("BVT", "Bouvet Island"),
	("BRA", "Brazil"),
	("IOT", "British Indian Ocean Territory"),
	("BRN", "Brunei Darussalam"),
	("BGR", "Bulgaria"),
	("BFA", "Burkina Faso"),
	("BDI", "Burundi"),
	("KHM", "Cambodia"),
	("CMR", "Cameroon"),
	("CPV", "Cape Verde"),
	("CYM", "Cayman Islands"),
	("CAF", "Central African Republic"),
	("TCD", "Chad"),
	("CHL", "Chile"),
	("CHN", "China"),
	("CXR", "Christmas Island"),
	("CCK", "Cocoa (Keeling) Islands"),
	("COL", "Colombia"),
	("COM", "Comoros"),
	("COG", "Congo"),
	("COK", "Cook Islands"),
	("CRI", "Costa Rica"),
	("CIV", "Cote Divoire"),
	("HRV", "Croatia (local name: Hrvatska)"),
	("CUB", "Cuba"),
	("CYP", "Cyprus"),
	("CZE", "Czech Republic"),
	("DNK", "Denmark"),
	("DJI", "Djibouti"),
	("DMA", "Dominica"),
	("DOM", "Dominican Republic"),
	("TMP", "East Timor"),
	("ECU", "Ecuador"),
	("EGY", "Egypt"),
	("SLV", "El Salvador"),
	("GNQ", "Equatorial Guinea"),
	("ERI", "Eritrea"),
	("EST", "Estonia"),
	("ETH", "Ethiopia"),
	("FLK", "Falkland Islands (Malvinas)"),
	("FRO", "Faroe Islands"),
	("FJI", "Fiji"),
	("FIN", "Finland"),
	("FRA", "France"),
	("FXX", "France, Metropolitan"),
	("GUF", "French Guiana"),
	("PYF", "French Polynesia"),
	("ATF", "French Southern Territories"),
	("GAB", "Gabon"),
	("GMB", "Gambia"),
	("GEO", "Georgia"),
	("DEU", "Germany"),
	("GHA", "Ghana"),
	("GIB", "Gibraltar"),
	("GRC", "Greece"),
	("GRL", "Greenland"),
	("GRD", "Grenada"),
	("GLP", "Guadeloupe"),
	("GUM", "Guam"),
	("GTM", "Guatemala"),
	("GIN", "Guinea"),
	("GNB", "Guinea-Bissau"),
	("GUY", "Guyana"),
	("HTI", "Haiti"),
	("HMD", "Heard and Mc Donald Islands"),
	("HND", "Honduras"),
	("HKG", "Hong Kong"),
	("HUN", "Hungary"),
	("ISL", "Iceland"),
	("IND", "India"),
	("IDN", "Indonesia"),
	("IRN", "Iran (Islamic Republic of)"),
	("IRQ", "Iraq"),
	("IRL", "Ireland"),
	("ISR", "Israel"),
	("ITA", "Italy"),
	("JAM", "Jamaica"),
	("JPN", "Japan"),
	("JOR", "Jordan"),
	("KAZ", "Kazakhstan"),
	("KEN", "Kenya"),
	("KIR", "Kiribati"),
	("PRK", "Korea, Democratic Peoples Republic of"),
	("KOR", "Korea, Republic of"),
	("KWT", "Kuwait"),
	("KGZ", "Kyrgyzstan"),
	("LAO", "Lao Peoples Democratic Republic"),
	("LVA", "Latvia"),
	("LBN", "Lebanon"),
	("LSO", "Lesotho"),
	("LBR", "Liberia"),
	("LBY", "Libyan Arab Jamahiriya"),
	("LIE", "Liechtenstein"),
	("LTU", "Lithuania"),
	("LUX", "Luxembourg"),
	("MAC", "Macau"),
	("MKD", "Macedonia, The Former Yugoslav Republic of"),
	("MDG", "Madagascar"),
	("MWI", "Malawi"),
	("MYS", "Malaysia"),
	("MDV", "Maldives"),
	("MLI", "Mali"),
	("MLT", "Malta"),
	("MHL", "Marshall Islands"),
	("MTQ", "Martinique"),
	("MRT", "Mauritania"),
	("MVS", "Mauritius"),
	("MYT", "Mayotte"),
	("MEX", "Mexico"),
	("FSM", "Micronesia, Federated States of"),
	("MDA", "Moldova, Republic of"),
	("MCO", "Monaco"),
	("MNG", "Mongolia"),
	("MSR", "Montserrat"),
	("MAR", "Morocco"),
	("MOZ", "Mozambique"),
	("MMR", "Myanmar"),
	("NAM", "Namibia"),
	("NRU", "Nauru"),
	("NPL", "Nepal"),
	("NLD", "Netherlands"),
	("ANT", "Netherlands Antilles"),
	("NCL", "New Caledonia"),
	("NZL", "New Zealand"),
	("NIC", "Nicaragua"),
	("NER", "Niger"),
	("NGA", "Nigeria"),
	("NIU", "Niue"),
	("NFK", "Norfolk Island"),
	("MNP", "Northern Mariana Islands"),
	("MOR", "Norway"),
	("OMN", "Oman"),
	("PAK", "Pakistan"),
	("PLW", "Palau"),
	("PAN", "Panama"),
	("PNG", "Papua New Guinea"),
	("PRY", "Paraguay"),
	("PER", "Peru"),
	("PHL", "Philippines"),
	("PCN", "Pitcairn"),
	("POL", "Poland"),
	("PRT", "Portugal"),
	("PRI", "Puerto Rico"),
	("QAT", "Qatar"),
	("REU", "Reunion"),
	("ROM", "Romania"),
	("RUS", "Russian Federation"),
	("RWA", "Rwanda"),
	("KNA", "Saint Kitts and Nevis"),
	("LCA", "Saint Lucia"),
	("VCT", "Saint Vincent and the Grenadines"),
	("WSM", "Samoa"),
	("SMR", "San Marino"),
	("STP", "Sao Tome and Principe"),
	("SAU", "Saudi Arabia"),
	("SEN", "Senegal"),
	("SYC", "Seychelles"),
	("SLE", "Sierra Leone"),
	("SGP", "Singapore"),
	("SVK", "Slovakia (Slovak Republic)"),
	("SVN", "Slovenia"),
	("SLB", "Solomon Islands"),
	("SOM", "Somalia"),
	("ZAF", "South Africa"),
	("SGS", "South Georgia and the South Sandwich Islands"),
	("ESP", "Spain"),
	("LKA", "Sri Lanka"),
	("SHN", "St. Helena"),
	("SPM", "St. Pierre and Miquelon"),
	("SDN", "Sudan"),
	("SUR", "Suriname"),
	("SJM", "Svalbard and Jan Mayen Islands"),
	("SWZ", "Swaziland"),
	("SWE", "Sweden"),
	("CHE", "Switzerland"),
	("SYR", "Syrian Arab Republic"),
	("TWN", "Taiwan"),
	("TJK", "Tajikistan"),
	("TZA", "Tanzania, United Republic of"),
	("THA", "Thailand"),
	("TGO", "Togo"),
	("TKL", "Tokelau"),
	("TON", "Tonga"),
	("TTO", "Trinidad and Tobago"),
	("TUN", "Tunisia"),
	("TUR", "Turkey"),
	("TKM", "Turkmenistan"),
	("TCA", "Turks and Caicos Islands"),
	("TUV", "Tuvalu"),
	("UGA", "Uganda"),
	("UKR", "Ukraine"),
	("ARE", "United Arab Emirates"),
	("GBR", "United Kingdom"),
	("UMI", "United States Minor Outlying Islands"),
	("UNK", "Unknown Country"),
	("URY", "Uruguay"),
	("UZB", "Uzbekistan"),
	("VUT", "Vanuatu"),
	("VAT", "Vatican City State (Holy See)"),
	("VEN", "Venezuela"),
	("VNM", "Viet Nam"),
	("VGB", "Virgin Islands (British)"),
	("VIR", "Virgin Islands (U.S.)"),
	("WLF", "Wallisw and Futuna Islands"),
	("ESH", "Western Sahara"),
	("YEM", "Yeman"),
	("YUG", "Yugoslavia"),
	("ZAR", "Zaire"),
	("ZMB", "Zambia"),
	("ZWE", "Zimbabwe")
)

states = (
	("", "-- Select State/Province --"),
	("UNK", "Outside US / Canada"),
	("AL", "Alabama"),
	("AK", "Alaska"),
	("AB", "Alberta (CAN),"),
	("AS", "American Samoa"),
	("AZ", "Arizona"),
	("AR", "Arkansas"),
	("AA", "Armed Forces Americas"),
	("AE", "Armed Forces Europe"),
	("AP", "Armed Forces Pacific"),
	("BC", "British Columbia (CAN),"),
	("CA", "California"),
	("CO", "Colorado"),
	("CT", "Connecticut"),
	("DE", "Delaware"),
	("DC", "District Of Columbia"),
	("FL", "Florida"),
	("GA", "Georgia"),
	("GU", "Guam"),
	("HI", "Hawaii"),
	("ID", "Idaho"),
	("IL", "Illinois"),
	("IN", "Indiana"),
	("IA", "Iowa"),
	("KS", "Kansas"),
	("KY", "Kentucky"),
	("LA", "Louisiana"),
	("ME", "Maine"),
	("MB", "Manitoba (CAN),"),
	("MD", "Maryland"),
	("MA", "Massachusetts"),
	("MI", "Michigan"),
	("MN", "Minnesota"),
	("MS", "Mississippi"),
	("MO", "Missouri"),
	("MT", "Montana"),
	("NE", "Nebraska"),
	("NV", "Nevada"),
	("NB", "New Brunswick (CAN),"),
	("NH", "New Hampshire"),
	("NJ", "New Jersey"),
	("NM", "New Mexico"),
	("NY", "New York"),
	("NF", "Newfoundland (CAN),"),
	("NC", "North Carolina"),
	("ND", "North Dakota"),
	("MP", "Northern Mariana Is"),
	("NT", "Northwest Territories (CAN),"),
	("NS", "Nova Scotia (CAN),"),
	("OH", "Ohio"),
	("OK", "Oklahoma"),
	("ON", "Ontario"),
	("OR", "Oregon"),
	("PW", "Palau"),
	("PA", "Pennsylvania"),
	("PE", "Prince Edward Island (CAN),"),
	("PQ", "Province du Quebec (CAN),"),
	("PR", "Puerto Rico"),
	("RI", "Rhode Island"),
	("SK", "Saskatchewan (CAN),"),
	("SC", "South Carolina"),
	("SD", "South Dakota"),
	("TN", "Tennessee"),
	("TX", "Texas"),
	("UT", "Utah"),
	("VT", "Vermont"),
	("VI", "Virgin Islands"),
	("VA", "Virginia"),
	("WA", "Washington"),
	("WV", "West Virginia"),
	("WI", "Wisconsin"),
	("WY", "Wyoming"),
	("YT", "Yukon Territory (CAN)"),
)

languages = (
	("Afrikaans", "Afrikaans"),
	("Albanian", "Albanian"),
	("American Sign Language", "American Sign Language"),
	("Arabic", "Arabic"),
	("Armenian", "Armenian"),
	("Basque", "Basque"),
	("Belarusan", "Belarusan"),
	("Bosnian", "Bosnian"),
	("Bulgarian", "Bulgarian"),
	("Burarra", "Burarra"),
	("Cambodian", "Cambodian"),
	("Cantonese", "Cantonese"),
	("Catalan", "Catalan"),
	("Chinese", "Chinese"),
	("Corsican", "Corsican"),
	("Creole", "Creole"),
	("Croatian", "Croatian"),
	("Czech", "Czech"),
	("Danish", "Danish"),
	("Dutch", "Dutch"),
	("English", "English"),
	("Esperanto", "Esperanto"),
	("Euskara", "Euskara"),
	("Ewe", "Ewe"),
	("Farsi", "Farsi"),
	("Filipino", "Filipino"),
	("Finnish", "Finnish"),
	("French", "French"),
	("Galician", "Galician"),
	("German", "German"),
	("Grebo", "Grebo"),
	("Greek", "Greek"),
	("Gwichin", "Gwichin"),
	("Hawaiian", "Hawaiian"),
	("Hebrew", "Hebrew"),
	("Hindi", "Hindi"),
	("Hungarian", "Hungarian"),
	("Icelandic", "Icelandic"),
	("Indonesian", "Indonesian"),
	("Ingalik", "Ingalik"),
	("Irish", "Irish"),
	("Italian", "Italian"),
	("Japanese", "Japanese"),
	("Kartuli", "Kartuli"),
	("Korean", "Korean"),
	("Laotian", "Laotian"),
	("Latin", "Latin"),
	("Lithuanian", "Lithuanian"),
	("Maasai", "Maasai"),
	("Macedonian", "Macedonian"),
	("Malay", "Malay"),
	("Maltese", "Maltese"),
	("Maori", "Maori"),
	("Native American - Ojibwe", "Native American - Ojibwe"),
	("Ndjbbana", "Ndjbbana"),
	("Norwegian", "Norwegian"),
	("Old English", "Old English"),
	("Old French", "Old French"),
	("Old Norse", "Old Norse"),
	("Palauan", "Palauan"),
	("Pali", "Pali"),
	("Papiamentu", "Papiamentu"),
	("Pashtu", "Pashtu"),
	("Persian", "Persian"),
	("Polish", "Polish"),
	("Portuguese", "Portuguese"),
	("Punjabi", "Punjabi"),
	("Quechua", "Quechua"),
	("Remedial English", "Remedial English"),
	("Russian", "Russian"),
	("Scandinavian", "Scandinavian"),
	("Serbian", "Serbian"),
	("Shona", "Shona"),
	("Sindhi", "Sindhi"),
	("Sinhala", "Sinhala"),
	("Slavic", "Slavic"),
	("Slovak", "Slovak"),
	("Slovenian", "Slovenian"),
	("Sotho", "Sotho"),
	("Spanish", "Spanish"),
	("Swahili", "Swahili"),
	("Swedish", "Swedish"),
	("Tagalog", "Tagalog"),
	("Tamazight", "Tamazight"),
	("Tamil", "Tamil"),
	("Thai", "Thai"),
	("Tibetan", "Tibetan"),
	("Turkish", "Turkish"),
	("Ukrainian", "Ukrainian"),
	("Urdu", "Urdu"),
	("Uzbek", "Uzbek"),
	("Vietnamese", "Vietnamese"),
	("Welsh", "Welsh"),
	("Xhosa", "Xhosa"),
	("Yiddish", "Yiddish"),
	("Zulu", "Zulu"),
	("Other", "Other")
)

occupations = (
	("School teacher", "School teacher"), 
	("School administrator, staff, specialist, or teacher trainer", "School administrator, staff, specialist, or teacher trainer"), 
	("College/university faculty or teacher", "College/university faculty or teacher"), 
	("College/university administrator, staff, or teacher trainer", "College/university administrator, staff, or teacher trainer"), 
	("Adult or vocational education teacher, staff, or adminstrator", "Adult or vocational education teacher, staff, or adminstrator"), 
	("Researcher or materials developer (including software)", "Researcher or materials developer (including software)"), 
	("Undergraduate student", "Undergraduate student"), 
	("Graduate student", "Graduate student"), 
	("Other", "Other")
)