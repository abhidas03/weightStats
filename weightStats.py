from month import Month
import calendarDict
file = open("weights.txt", "r")
writeFile = open("yourStats.txt", "w")

months = []
currentM = Month("01", "1776")
for line in file:
  if (line[0] != "#"):
    data = line.split()
    date = data[0]
    month = date[0:2]
    day = date[3:5]
    year = date[-4:]
    weight = data[1].strip()
    weight = float(weight)

    monthYear = calendarDict.calendar[month] + " " + year
    if ((monthYear) not in months):
      if(currentM.getYear() != "1776"):
        print(currentM)
        months.append(monthYear)
      currentM = Month(month, year)
    currentM.updateDaysRecorded()
    currentM.addToAverage(weight)

file.close()
writeFile.close()