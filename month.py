import calendarDict
class Month:
    def __init__ (self, month, year):
        self.month = month
        self.year = year
        self.average = 0
        self.total = 0
        self.daysRecorded = 0

    def __str__(self):
        return (
            f"Your average for {calendarDict.calendar[self.month]} {self.year} is {round(self.average, 1)}.\n" 
        )
        
    def getAverage(self):
        return round(self.average, 1)

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def addToAverage(self, amount):
        self.total += amount
        if (self.daysRecorded > 0):
            self.average = self.total/self.daysRecorded

    def updateDaysRecorded(self):
        self.daysRecorded += 1

    def findChange(self, nextMonth):
        return nextMonth.getAverage() - self.average 
        
    
