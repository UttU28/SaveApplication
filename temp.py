import json

links = [
        {
          "jobID": "0",
          "jobTitle": "Summer 2023 Intern - Application Developer - Monroe",
          "companyName": "IBM",
          "link": "https://app.joinhandshake.com/stu/jobs/7523962?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "May 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "1",
          "jobTitle": "Computer Science and Software Engineering Internships",
          "companyName": "MITRE Corporation",
          "link": "https://app.joinhandshake.com/stu/jobs/6946257?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "April 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "2",
          "jobTitle": "Software Data Engineering &amp; Analytics Internship (Summer 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7338525?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "March 31, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "3",
          "jobTitle": "2023 Information Technology Software Engineering - Intern ",
          "companyName": "Ford Motor Company",
          "link": "https://app.joinhandshake.com/stu/jobs/7383285?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "February 28, 2023 11:59 PM",
          "filled": ""
        },
        {
          "jobID": "4",
          "jobTitle": "Software Engineering Internship, IT Applications (Summer 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7338948?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "March 31, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "5",
          "jobTitle": "Software Engineering Intern 2023",
          "companyName": "Oscar Health Insurance",
          "link": "https://app.joinhandshake.com/stu/jobs/7111684?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "March 13, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "6",
          "jobTitle": "Enterprise Account Engineer Intern, Premium Support",
          "companyName": "Amazon",
          "link": "https://app.joinhandshake.com/stu/jobs/7455424?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "April 3, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "7",
          "jobTitle": "2023 - SWE Intern, US",
          "companyName": "MongoDB",
          "link": "https://app.joinhandshake.com/stu/jobs/7422092?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "April 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "8",
          "jobTitle": "Fall 2023 Intern - Electronics - Software Testing (Masters) *REMOTE",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7538375?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "9",
          "jobTitle": "Application Engineer Summer 2023 Internship",
          "companyName": "Beacon Platform, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7357055?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "April 14, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "10",
          "jobTitle": "Systems Engineering Intern (Wilmington, Massachusetts)",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7106700?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "11",
          "jobTitle": "Fall 2023 - Spring 2024 Software Development Intern",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7532046?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "12",
          "jobTitle": "Fall 2023 Intern - Electronics (Masters) *REMOTE",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7538835?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "13",
          "jobTitle": "(#R22-8470) Intern, Information Technology",
          "companyName": "Rockwell Automation",
          "link": "https://app.joinhandshake.com/stu/jobs/7514080?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "May 19, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "14",
          "jobTitle": "Fall 2023 Intern - Electronics (Bachelors/Masters) *REMOTE",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7538423?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "15",
          "jobTitle": "System Engineer Intern",
          "companyName": "NXP Semiconductors",
          "link": "https://app.joinhandshake.com/stu/jobs/7519872?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "June 29, 2023 12:00 PM",
          "filled": ""
        },
        {
          "jobID": "16",
          "jobTitle": "Fall 2023 Intern - Electronics - CAD Software Development and Testing (Masters/PhD) *REMOTE",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7533875?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "17",
          "jobTitle": "Grid Software Internship (Energy Business Advisory)",
          "companyName": "Siemens",
          "link": "https://app.joinhandshake.com/stu/jobs/7513038?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "April 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "18",
          "jobTitle": "Systems Engineering Intern",
          "companyName": "NXP Semiconductors",
          "link": "https://app.joinhandshake.com/stu/jobs/7519862?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "June 29, 2023 12:00 PM",
          "filled": ""
        },
        {
          "jobID": "19",
          "jobTitle": "SWE Intern, Summer 2023",
          "companyName": "Jobfair®",
          "link": "https://app.joinhandshake.com/stu/jobs/7501449?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 6, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "20",
          "jobTitle": "Quality Analyst",
          "companyName": "Eitacies Inc",
          "link": "https://app.joinhandshake.com/stu/jobs/6705105?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 30, 2023 2:30 PM",
          "filled": ""
        },
        {
          "jobID": "21",
          "jobTitle": "Intern, Software Development - Desktop Strategy",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7457476?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "22",
          "jobTitle": "Fall 2023 Intern - Electronics (Masters/PhD) *REMOTE",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7539843?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "23",
          "jobTitle": "Fall 2023 Intern - Systems &amp; Platform - Simulation Software Development (Bachelors/Masters)",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7542182?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "24",
          "jobTitle": "Summer 2023 Intern- Application Developer: Mainframe Mod – Lansing, MI",
          "companyName": "IBM",
          "link": "https://app.joinhandshake.com/stu/jobs/7497648?ref=open-in-new-tab&search_id=4c0ff02f-b940-4cce-bc11-040f02aa216f",
          "location": "May 6, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "25",
          "jobTitle": "Summer 2023 Intern- Application Developer: Mainframe Mod – Lansing, MI",
          "companyName": "IBM",
          "link": "https://app.joinhandshake.com/stu/jobs/7497648?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "May 6, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "26",
          "jobTitle": "Summer 2023 Intern – Application Developer – Baton Rouge",
          "companyName": "IBM",
          "link": "https://app.joinhandshake.com/stu/jobs/7524017?ref=open-in-new-tab&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "May 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "27",
          "jobTitle": "Summer 2023 Intern- Application Developer: RPA – Lansing, MI",
          "companyName": "IBM",
          "link": "https://app.joinhandshake.com/stu/jobs/7497686?ref=preview-header-click&search_id=3b208e2b-7e19-4e66-b1d1-17b2f3a96a69",
          "location": "May 6, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "28",
          "jobTitle": "Intern, Test Automation (Req #6025)",
          "companyName": "Spirent Communications, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7513228?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "May 29, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "29",
          "jobTitle": "Intern, Test Automation (Req #6027)",
          "companyName": "Spirent Communications, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7513350?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "May 29, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "30",
          "jobTitle": "Junior Analyst - Internship",
          "companyName": "EXL Service",
          "link": "https://app.joinhandshake.com/stu/jobs/7534729?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "May 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "31",
          "jobTitle": "Software Developer Intern (Hybrid)",
          "companyName": "BAE Systems, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7395129?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "June 1, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "32",
          "jobTitle": "IT/Devops Summer Intern",
          "companyName": "Draper",
          "link": "https://app.joinhandshake.com/stu/jobs/7147756?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "33",
          "jobTitle": "Intern, Test Automation (Req #6028)",
          "companyName": "Spirent Communications, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7513386?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "May 29, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "34",
          "jobTitle": "Intern-Software Engineer ",
          "companyName": "Corsearch",
          "link": "https://app.joinhandshake.com/stu/jobs/7405818?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "June 30, 2023 6:50 PM",
          "filled": ""
        },
        {
          "jobID": "35",
          "jobTitle": "Intern, Software Engineer (Req #6047)",
          "companyName": "Spirent Communications, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7513813?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "May 30, 2023 12:55 AM",
          "filled": ""
        },
        {
          "jobID": "36",
          "jobTitle": "Summer 2023 - Software Engineer Intern",
          "companyName": "CSAA Insurance Group, a AAA Insurer",
          "link": "https://app.joinhandshake.com/stu/jobs/6986514?ref=open-in-new-tab&search_id=ba8e0477-2c50-4cbb-af58-8996008128d4",
          "location": "April 8, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "37",
          "jobTitle": "Map/Coding internship for energy ecosystem project",
          "companyName": "American Energy Society",
          "link": "https://app.joinhandshake.com/stu/jobs/7463868?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "April 1, 2023 11:55 PM",
          "filled": ""
        },
        {
          "jobID": "38",
          "jobTitle": "Enterprise Software Applications Intern",
          "companyName": "Draper",
          "link": "https://app.joinhandshake.com/stu/jobs/7191314?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "39",
          "jobTitle": "NASA SCaN - Technology Educational Satellites Networking Experiment Development - SIP",
          "companyName": "NASA Glenn Research Center",
          "link": "https://app.joinhandshake.com/stu/jobs/7389946?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "40",
          "jobTitle": "Software Test Engineering Intern ",
          "companyName": "STERIS",
          "link": "https://app.joinhandshake.com/stu/jobs/6964028?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "March 31, 2023 11:59 PM",
          "filled": ""
        },
        {
          "jobID": "41",
          "jobTitle": "Substation and Data Innovation Engineering",
          "companyName": "Eversource Energy",
          "link": "https://app.joinhandshake.com/stu/jobs/7259816?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "June 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "42",
          "jobTitle": "Electrical Engineering Intern",
          "companyName": "Second Order Effects Inc",
          "link": "https://app.joinhandshake.com/stu/jobs/5732690?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "August 27, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "43",
          "jobTitle": "Software Engineering Intern",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7089084?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "44",
          "jobTitle": "Software Applications Engineer Intern ",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7442157?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "45",
          "jobTitle": "IT Systems and Software Intern (Wilmington, Massachusetts)",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7106352?ref=open-in-new-tab&search_id=ec05058b-a6a9-4836-af4b-e5fcdc3ba021",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "46",
          "jobTitle": "IT Automation Intern (Wilmington, Massachusetts)",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7106377?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "47",
          "jobTitle": "Functional Safety System &amp; Software Engineer  (Multiple)",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7106439?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "48",
          "jobTitle": "Engineering Leadership Development Program Internship (Factory Automation)",
          "companyName": "Siemens",
          "link": "https://app.joinhandshake.com/stu/jobs/6898250?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "March 1, 2023 12:00 PM",
          "filled": ""
        },
        {
          "jobID": "49",
          "jobTitle": "Quantitative Developer Intern",
          "companyName": "Beacon Platform, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7258882?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "April 14, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "50",
          "jobTitle": "Software Engineer Intern ",
          "companyName": "Odoo, Inc",
          "link": "https://app.joinhandshake.com/stu/jobs/7256435?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "June 30, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "51",
          "jobTitle": "Fall 2023 Intern - Meshing (Masters)",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7540564?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "52",
          "jobTitle": "(#R22-9722) Intern, Advanced Engineering",
          "companyName": "Rockwell Automation",
          "link": "https://app.joinhandshake.com/stu/jobs/7514070?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "May 19, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "53",
          "jobTitle": "Fall 2023 Intern - Systems &amp; Platform - Software Engineering",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7542203?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "54",
          "jobTitle": "Intern - Robotics Engineering",
          "companyName": "Alert Innovation",
          "link": "https://app.joinhandshake.com/stu/jobs/7507150?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "May 5, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "55",
          "jobTitle": "Fall 2023 Software Development Co-Op",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7542698?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "56",
          "jobTitle": "(#R22-10787) Intern, Firmware Engineering",
          "companyName": "Rockwell Automation",
          "link": "https://app.joinhandshake.com/stu/jobs/7514102?ref=open-in-new-tab&search_id=4c9536ae-be96-46e2-a251-c45b23335bf2",
          "location": "May 19, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "57",
          "jobTitle": "Intern, Test Automation (Req #6026)",
          "companyName": "Spirent Communications, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7513291?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "May 29, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "58",
          "jobTitle": "Summer 2023 Intern – Automation Test Specialist – Lansing, MI",
          "companyName": "IBM",
          "link": "https://app.joinhandshake.com/stu/jobs/7497602?ref=open-in-new-tab&search_id=e127f4dc-ac69-409c-9dec-9af525791fee",
          "location": "May 6, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "59",
          "jobTitle": "Bell Labs Analytics &amp; Algorithms Intern 2200000NAU",
          "companyName": "Nokia",
          "link": "https://app.joinhandshake.com/stu/jobs/7434998?ref=open-in-new-tab&search_id=e127f4dc-ac69-409c-9dec-9af525791fee",
          "location": "April 7, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "60",
          "jobTitle": "Bell Labs Robotics Intern 2200000MT6",
          "companyName": "Nokia",
          "link": "https://app.joinhandshake.com/stu/jobs/7304932?ref=open-in-new-tab&search_id=e127f4dc-ac69-409c-9dec-9af525791fee",
          "location": "March 10, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "61",
          "jobTitle": "Bell Labs Math &amp; Algorithms Summer Intern 2200000KYY",
          "companyName": "Nokia",
          "link": "https://app.joinhandshake.com/stu/jobs/7223290?ref=open-in-new-tab&search_id=e127f4dc-ac69-409c-9dec-9af525791fee",
          "location": "March 27, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "62",
          "jobTitle": "Bell Labs Autonomous Systems Summer Intern 2200000KQ0",
          "companyName": "Nokia",
          "link": "https://app.joinhandshake.com/stu/jobs/7223424?ref=open-in-new-tab&search_id=e127f4dc-ac69-409c-9dec-9af525791fee",
          "location": "March 17, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "63",
          "jobTitle": "Automation Development and Tooling Engineering Internship - Midwest USA (Fall 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7498197?ref=open-in-new-tab&search_id=0aacfcba-61df-4849-8665-c96c739fc3e9",
          "location": "May 19, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "64",
          "jobTitle": "Information Technology Intern",
          "companyName": "Texas Instruments Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7354084?ref=open-in-new-tab&search_id=0aacfcba-61df-4849-8665-c96c739fc3e9",
          "location": "April 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "65",
          "jobTitle": "2023 Internship -Computer Scientist / Applied Mathematician / Engineer - Scientific Applications for Intelligence, Surveillance, and Reconnaissance",
          "companyName": "Johns Hopkins University Applied Physics Laboratory",
          "link": "https://app.joinhandshake.com/stu/jobs/7237269?ref=open-in-new-tab&search_id=0aacfcba-61df-4849-8665-c96c739fc3e9",
          "location": "March 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "66",
          "jobTitle": "Computer Science / Electrical Engineering Intern - Summer 2023",
          "companyName": "Atkins, Member of the SNC-Lavalin Group",
          "link": "https://app.joinhandshake.com/stu/jobs/7276411?ref=open-in-new-tab&search_id=0aacfcba-61df-4849-8665-c96c739fc3e9",
          "location": "May 15, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "67",
          "jobTitle": "2023 START Technology Intern Program - Developer - Pittsburgh &amp; Lake Mary",
          "companyName": "Bank of New York Mellon (BNY Mellon)",
          "link": "https://app.joinhandshake.com/stu/jobs/6873832?ref=open-in-new-tab&search_id=0088e200-9a92-4b74-bc8c-cf14d8489d88",
          "location": "April 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "68",
          "jobTitle": "2023 Operations &amp; Technology Summer Analyst Program - Charlotte, NC - Hybrid",
          "companyName": "MUFG",
          "link": "https://app.joinhandshake.com/stu/jobs/7495269?ref=open-in-new-tab&search_id=0088e200-9a92-4b74-bc8c-cf14d8489d88",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "69",
          "jobTitle": "Amazon Robotics - System Development Eng Intern - Summer 2023",
          "companyName": "Amazon Robotics",
          "link": "https://app.joinhandshake.com/stu/jobs/7153170?ref=open-in-new-tab&search_id=0088e200-9a92-4b74-bc8c-cf14d8489d88",
          "location": "April 3, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "70",
          "jobTitle": "INROADS &amp; L3Harris: Software Engineering and Technology Related Summer Internship",
          "companyName": "INROADS",
          "link": "https://app.joinhandshake.com/stu/jobs/6826921?ref=open-in-new-tab&search_id=0088e200-9a92-4b74-bc8c-cf14d8489d88",
          "location": "June 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "71",
          "jobTitle": "Energy Engineering - Software Engineer/Data Scientist (Fall 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7498174?ref=open-in-new-tab&search_id=0088e200-9a92-4b74-bc8c-cf14d8489d88",
          "location": "May 19, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "72",
          "jobTitle": "Electrical Test Engineering Internship (Fall 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7498231?ref=open-in-new-tab&search_id=0088e200-9a92-4b74-bc8c-cf14d8489d88",
          "location": "May 19, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "73",
          "jobTitle": "Intern, Expert Services",
          "companyName": "Kroll",
          "link": "https://app.joinhandshake.com/stu/jobs/7470762?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "February 28, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "74",
          "jobTitle": "Software Engineering Intern",
          "companyName": "Crown Castle",
          "link": "https://app.joinhandshake.com/stu/jobs/7499944?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "February 28, 2023 12:59 PM",
          "filled": ""
        },
        {
          "jobID": "75",
          "jobTitle": "Software QA &amp; Test Engineering Internship (Summer 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7338368?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "March 31, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "76",
          "jobTitle": "Factory Automation Engineering Intern (Summer 2023)",
          "companyName": "GlobalFoundries",
          "link": "https://app.joinhandshake.com/stu/jobs/7495322?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "March 24, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "77",
          "jobTitle": "ETDP Intern - Software Engineering ",
          "companyName": "Highmark Health",
          "link": "https://app.joinhandshake.com/stu/jobs/7132242?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "April 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "78",
          "jobTitle": "Intern, Software Engineer (Req #6048)",
          "companyName": "Spirent Communications, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7513824?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "May 30, 2023 12:55 AM",
          "filled": ""
        },
        {
          "jobID": "79",
          "jobTitle": "RVO Health: 2023 Software Engineer Intern- Charlotte, NC",
          "companyName": "Red Ventures",
          "link": "https://app.joinhandshake.com/stu/jobs/6963104?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "April 14, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "80",
          "jobTitle": "IT - Software Engineering Summer Intern 2023b",
          "companyName": "John Deere",
          "link": "https://app.joinhandshake.com/stu/jobs/7326009?ref=open-in-new-tab&search_id=177f179b-86b0-4a61-94c9-5a2316edf0de",
          "location": "March 31, 2023 1:00 AM",
          "filled": ""
        },
        {
          "jobID": "81",
          "jobTitle": "Technology Internship Program",
          "companyName": "Macy's, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7434773?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "May 1, 2023 5:10 PM",
          "filled": ""
        },
        {
          "jobID": "82",
          "jobTitle": "System Integration &amp; Test Engineering Intern",
          "companyName": "Draper",
          "link": "https://app.joinhandshake.com/stu/jobs/7126446?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "83",
          "jobTitle": "Software Engineer Intern (EW - Electronic Warfare)",
          "companyName": "SRC, Inc",
          "link": "https://app.joinhandshake.com/stu/jobs/7429262?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "March 20, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "84",
          "jobTitle": "Engineering Technician II Intern 10883",
          "companyName": "Resideo Technologies, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7124656?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "April 29, 2023 10:00 PM",
          "filled": ""
        },
        {
          "jobID": "85",
          "jobTitle": "Computer Science Paid Intern ( SA-FM-JR7734)",
          "companyName": "Rangam Consultants Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7415325?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "September 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "86",
          "jobTitle": "2023 Software Developer Fox River Summer Analyst",
          "companyName": "Instinet",
          "link": "https://app.joinhandshake.com/stu/jobs/7369564?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "March 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "87",
          "jobTitle": "2023 Internship - Software Development - Multi-Mission Planning Development",
          "companyName": "Johns Hopkins University Applied Physics Laboratory",
          "link": "https://app.joinhandshake.com/stu/jobs/7251511?ref=open-in-new-tab&search_id=1cd48923-a933-4027-847d-0016bbcb4d55",
          "location": "February 28, 2023 9:00 PM",
          "filled": ""
        },
        {
          "jobID": "88",
          "jobTitle": "Technology Internship Program",
          "companyName": "Macy's, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7434773?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "May 1, 2023 5:10 PM",
          "filled": ""
        },
        {
          "jobID": "89",
          "jobTitle": "Engineering Technician II Intern 10883",
          "companyName": "Resideo Technologies, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7124656?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "April 29, 2023 10:00 PM",
          "filled": ""
        },
        {
          "jobID": "90",
          "jobTitle": "Computer Science Paid Intern ( SA-FM-JR7734)",
          "companyName": "Rangam Consultants Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7415325?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "September 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "91",
          "jobTitle": "2023 Software Developer Fox River Summer Analyst",
          "companyName": "Instinet",
          "link": "https://app.joinhandshake.com/stu/jobs/7369564?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "March 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "92",
          "jobTitle": "2023 Internship - Software Development - Multi-Mission Planning Development",
          "companyName": "Johns Hopkins University Applied Physics Laboratory",
          "link": "https://app.joinhandshake.com/stu/jobs/7251511?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "February 28, 2023 9:00 PM",
          "filled": ""
        },
        {
          "jobID": "93",
          "jobTitle": "Summer 2023 Software Engineer Internship",
          "companyName": "C4ADS",
          "link": "https://app.joinhandshake.com/stu/jobs/7544682?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "March 17, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "94",
          "jobTitle": "Health IT and Software Engineering Intern",
          "companyName": "MITRE Corporation",
          "link": "https://app.joinhandshake.com/stu/jobs/7128056?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "March 3, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "95",
          "jobTitle": "Software Intern--10913",
          "companyName": "Resideo Technologies, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7127932?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "April 29, 2023 10:00 PM",
          "filled": ""
        },
        {
          "jobID": "96",
          "jobTitle": "Software Engineer Intern --10787",
          "companyName": "Resideo Technologies, Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7078541?ref=open-in-new-tab&search_id=a3355495-48ea-489e-b5b1-0b7374c9d2b8",
          "location": "April 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "97",
          "jobTitle": "(#51421) 2023 Internship - Robotics Intern",
          "companyName": "Johns Hopkins University Applied Physics Laboratory",
          "link": "https://app.joinhandshake.com/stu/jobs/7387106?ref=open-in-new-tab&search_id=7e5ce9f7-de4c-49ac-9517-c5a30e0f9a7d",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "98",
          "jobTitle": "Amazon Robotics - C++ System Development Eng Intern - Summer 2023 (Onsite: Boston)",
          "companyName": "Amazon Robotics",
          "link": "https://app.joinhandshake.com/stu/jobs/7350930?ref=open-in-new-tab&search_id=e337d700-ff36-4510-bf04-575b76bf3400",
          "location": "March 3, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "99",
          "jobTitle": "Market Analytics Intern - Water",
          "companyName": "IDEXX",
          "link": "https://app.joinhandshake.com/stu/jobs/7554907?ref=open-in-new-tab&search_id=e337d700-ff36-4510-bf04-575b76bf3400",
          "location": "May 12, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "100",
          "jobTitle": "V&amp;V Test Engineer- Internship- Summer 2023",
          "companyName": "DEKA Research and Development",
          "link": "https://app.joinhandshake.com/stu/jobs/7432848?ref=open-in-new-tab&search_id=4337ef8a-f886-42d0-9f6d-0385f1ac7142",
          "location": "April 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "101",
          "jobTitle": "IT Operations Internship (Summer 2023)",
          "companyName": "Tesla",
          "link": "https://app.joinhandshake.com/stu/jobs/7339111?ref=open-in-new-tab&search_id=4337ef8a-f886-42d0-9f6d-0385f1ac7142",
          "location": "March 31, 2023 3:00 AM",
          "filled": ""
        },
        {
          "jobID": "102",
          "jobTitle": "Sensor Systems Integration and Test Intern",
          "companyName": "Draper",
          "link": "https://app.joinhandshake.com/stu/jobs/7520916?ref=open-in-new-tab&search_id=4337ef8a-f886-42d0-9f6d-0385f1ac7142",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "103",
          "jobTitle": "Software Developer Summer 2023 Intern ",
          "companyName": "U.S. News &amp; World Report",
          "link": "https://app.joinhandshake.com/stu/jobs/7466756?ref=open-in-new-tab&search_id=a26aa54e-6337-4447-b45b-21202b4b3399",
          "location": "May 1, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "104",
          "jobTitle": "S&amp;B E-Mobility Internship",
          "companyName": "S&amp;B USA Construction",
          "link": "https://app.joinhandshake.com/stu/jobs/7530745?ref=open-in-new-tab&search_id=a26aa54e-6337-4447-b45b-21202b4b3399",
          "location": "April 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "105",
          "jobTitle": "Earth, Moon, Mars GN&amp;C Graduate Intern (Houston Office)",
          "companyName": "Draper",
          "link": "https://app.joinhandshake.com/stu/jobs/7216562?ref=open-in-new-tab&search_id=a26aa54e-6337-4447-b45b-21202b4b3399",
          "location": "March 31, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "106",
          "jobTitle": "Intern: Bioinformatics",
          "companyName": "AstraZeneca",
          "link": "https://app.joinhandshake.com/stu/jobs/7224762?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "February 28, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "107",
          "jobTitle": "Technical Support Intern - Philadelphia",
          "companyName": "SIG",
          "link": "https://app.joinhandshake.com/stu/jobs/7330454?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "April 28, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "108",
          "jobTitle": "Technical Support Intern - Chicago",
          "companyName": "SIG",
          "link": "https://app.joinhandshake.com/stu/jobs/7330814?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "April 28, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "109",
          "jobTitle": "Test Engineering Intern",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7089122?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "110",
          "jobTitle": "Intern, Test Development (HW/SW)",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7445261?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "111",
          "jobTitle": "Test Engineering Intern (R230703)",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7441638?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "112",
          "jobTitle": "MEMS Test Development Intern",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7445148?ref=open-in-new-tab&search_id=b37927e6-90e8-4827-82c0-875e3d236473",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "113",
          "jobTitle": "Verification Intern ",
          "companyName": "Analog Devices Inc.",
          "link": "https://app.joinhandshake.com/stu/jobs/7190761?ref=open-in-new-tab&search_id=f92dc87e-c44f-455e-99f5-e416313bf970",
          "location": "June 30, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "114",
          "jobTitle": "System Engineer Intern",
          "companyName": "Dell Technologies",
          "link": "https://app.joinhandshake.com/stu/jobs/6896650?ref=open-in-new-tab&search_id=f92dc87e-c44f-455e-99f5-e416313bf970",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "115",
          "jobTitle": "Fall 2023 Intern - Software Testing - Design (Bachelor's)",
          "companyName": "Ansys",
          "link": "https://app.joinhandshake.com/stu/jobs/7542144?ref=open-in-new-tab&search_id=f92dc87e-c44f-455e-99f5-e416313bf970",
          "location": "March 10, 2023 12:00 AM",
          "filled": ""
        },
        {
          "jobID": "116",
          "jobTitle": "Systems Integration/Test Engineering Intern",
          "companyName": "Second Order Effects Inc",
          "link": "https://app.joinhandshake.com/stu/jobs/6986415?ref=open-in-new-tab&search_id=f92dc87e-c44f-455e-99f5-e416313bf970",
          "location": "August 27, 2023 3:00 AM",
          "filled": ""
        }
      ]

with open("savedApplications.json") as f:
    obj = json.load(f)
for i in range(len(links)):
    obj["remaining"]["companyData"].append({'jobID{}'.format(i) : links[i]})
with open("savedApplications.json","w+") as of:
    json.dump(obj,of)