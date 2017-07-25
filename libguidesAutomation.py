
#!/usr/bin/python

# Open idname file
readFile = open("../idname.txt", "r")

# Read our idname and store it to a variable.
idName = readFile.read()

# Close idname file
readFile.close()


######## Check if we did get the idName
#print list(idName)
######## Remove /n whitespace in our text
idName = idName.rstrip()
#print list(idName)


# Create our desired pattern, it will be use to check if we got the correct pattern
idPattern = '<div class="bold"></div>\n'
secondidPattern = '<a id="_link"'
###################################################################################

#print "pattern id is: " + idPattern

# Close a file
readFile.close()

########### Maybe we can this to look for pattern
#import re
#
#patternID = re.compile(r'id="_link"')
#
#foundPattern = patternID.search(str(htmlCode))
#
#print(foundPattern.group())


# Remove all whitespace and letter space
def removeSpacesinCode(receiveCode):

    for item in receiveCode:

       item = item.rstrip()
 
    return receiveCode;

# Get the code from our HTML file

# Open the HTML file
readFile = open("/home/john/Desktop/LibGuides/Libguides.html", "r")

# Read our HTML file and store the code to a variable
htmlCode = readFile.readlines()

htmlCode = removeSpacesinCode(htmlCode)

# Check if we get the code
# print "This is what read from html code"
#print htmlCode

# Iterate throuhg the variable

def insertnewHtmlCode(htmlcode):

    #print "this work: " + htmlcode

    newhtmlcode = list(htmlcode)

    newhtmlcode.insert(18,idName)

    newhtmlcode = "".join(newhtmlcode)

    return newhtmlcode;


# Iterate through HTML Code
for i in range(len(htmlCode)):
    
    # print(htmlCode[i])
    #htmlCode[i] = htmlCode[i].rstrip()
    #print list(htmlCode[i])
    #htmlCode[i] = ''.join(htmlCode[i])
    #print htmlCode[i]
    
    # Check If we get a match
    
     if htmlCode[i] == idPattern:

     #print "htmlCode: " + htmlCode[i] + " Pattern: " + idPattern
     #print "Equal"

     # When we found a match we need to insert our idName on it, we are going to modify it
      htmlCode[i] = insertnewHtmlCode(htmlCode[i])

      print "This is the result: " + str(htmlCode[i])

     elif htmlCode[i] == secondidPattern: 

          # When we found a match we need to insert our idName on it, we are going to modify it
          htmlCode[i] = insertnewHtmlCode(htmlCode[i])
        
  #else:

     #print("htmlCode: " +htmlCode[i] + " Pattern: " + idPattern)
     #print "Type of code"
     #print type(htmlCode[i])
     #print "type of pattern"
     #print type(idPattern)
     #print "Not Equal"

# Overwrite the string with idName
# string = idName

# Open the HTML file
readFile = open("/home/john/Desktop/LibGuides/Libguides.html", "w")
#
#
## Overwrite the idname into our html file
readFile.writelines(htmlCode)
#
#
## Close a file
readFile.close()

# Append idName to idPattern

# Write each idname to a designated line and position on our html code
#for idnameline in idName

    # Search for this pattern
    # Create a condition
  
    # Write the idnameline on that position

    #readFile.writelines(idnameline)
    # print(idnameline)