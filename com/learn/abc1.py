from xml.etree.ElementTree import ElementTree
mydoc = ElementTree(file='amfconfig.xml')
for e in mydoc.iterfind('./receiver/msg-destinations/msg-destination/dest-name'):
    print (e.text)
for e in mydoc.iterfind('./receiver/msg-destinations/msg-destination/queue/dest-exception-queue-name'):
    print (e.text)
for e in mydoc.iterfind('./sender/msg-destinations/msg-destination[isQueue="true"]/dest-name'):
    print (e.text)
print ('******************************')
for e in mydoc.iterfind('./sender/msg-destinations/msg-destination[isQueue="false"]/dest-name'):
    print (e.text)


'''import lxml.etree as ET

dom = ET.parse("test1.xml")
xslt = ET.parse("test1.xsl")
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))

from xml.etree.ElementTree import ElementTree
mydoc = ElementTree(file='test1.xml')
for e in mydoc.findall('.//catalog/cd'):
    print (e.get('title').text)


'''
