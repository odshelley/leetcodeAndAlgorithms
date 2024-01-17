from Solution import Solution 

class PreprocessDates(Solution):
    '''
    Given a date string in the formate Day Month Year , where: 

        - Day is a string in the form "1st", "2nd", "3rd", "21st", "22nd", "23rd", "31st" 
          and all other are the number + "th", eg: "4th" or "12th".
        - Month is the fist three letters of the English language months, like "jan" for 
          January through "Dec" for December.
        - Year is 4 digits ranging form 1900 to 2100.

    Convert the date string "Day Month Year" to the date string "YYYY-MM-DD" in the format
    "4 digit year - 2 digit month - 2 digit day".
    '''
        
    def __init__(self):
        super().__init__() 
    
    def solution(self, dates: list[str]) -> None:

        monthMap = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }

        newDates = []

        for date in dates:

            newDate = date.split()

            if newDate[0][0].isnumeric() and newDate[0][1].isnumeric():
                day = newDate[0][:2]
            else:
                day = '0' + newDate[0][0]

            month = monthMap[newDate[1]]

            year = newDate[2]

            newDate = year + '-' + month + '-' + day
            newDates.append(newDate)

        self.solution(newDates)
