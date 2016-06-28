try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

try:
    Tree = ET.parse("movies.xml")
    root = Tree.getroot()
except Exception as err:
    print(err)
    sys.exit(1)

print("{}---{}".format(root.tag, root.attrib))
for child in root:
    print('title: ', child.get('title'))
    print('type: ', child.find('type').text)
    print('format: ', child.find('format').text)
    print('rating: ', child.find('rating').text)
    print('description: ', child.find('description').text)
    if child.find('rating').text == "R":
        root.remove(child)

Tree.write('output.xml')




print('*'*10)
