import xml.etree.ElementTree as ET
from email.utils import formatdate
from time import time

OUTPUT_FILE = "rss.xml"

items = [
    {
        "title": "[공지] 3월 보안교육 안내",
        "link": "https://example.com/notice1",
        "description": "3월 25일 오후 2시 대강당에서 진행됩니다.",
        "pubDate": formatdate(time(), usegmt=True),
    },
    {
        "title": "[공지] 전사 워크숍 일정",
        "link": "https://example.com/notice2",
        "description": "4월 첫째 주 워크숍 일정이 확정되었습니다.",
        "pubDate": formatdate(time(), usegmt=True),
    },
]

rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

ET.SubElement(channel, "title").text = "회사 공지 RSS"
ET.SubElement(channel, "link").text = "https://example.com"
ET.SubElement(channel, "description").text = "MagicInfo용 공지 피드"
ET.SubElement(channel, "language").text = "ko-kr"
ET.SubElement(channel, "lastBuildDate").text = formatdate(time(), usegmt=True)

for item in items:
    node = ET.SubElement(channel, "item")
    ET.SubElement(node, "title").text = item["title"]
    ET.SubElement(node, "link").text = item["link"]
    ET.SubElement(node, "description").text = item["description"]
    ET.SubElement(node, "pubDate").text = item["pubDate"]

tree = ET.ElementTree(rss)
tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)
