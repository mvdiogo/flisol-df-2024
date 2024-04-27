from langchain_community.document_loaders.image import UnstructuredImageLoader
from langchain_community.document_loaders import ImageCaptionLoader
loader = UnstructuredImageLoader("1.png")
data = loader.load()
print(data)

loader = ImageCaptionLoader('ogaroto.jpg')
doc = loader.load()
print(doc)
