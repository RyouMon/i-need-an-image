# i-need-an-image

Download only one image from web, only one API.   
从互联网中仅下载一张图片，使用时仅需一个接口。

Only support "Bing Image" for now.  
现在只支持必应图片。

Developing...  
根据自己的项目需求，开发中...

确保可以从互联网上获取一张符合条件图片。可以指定图片的以下特征：
+ 关键词或一句话里的某个关键词（后续可能会移除提取关键词的功能）
+ 图片的版式：横板、竖版、方形

我的关注点是尽可能地提高获取图片的成功率，可以通过不同细粒度的重试来达到这一目标：
1. 请求图片实际地址失败时进行重试。
2. 对同一搜索页面的不同图片进行请求尝试。
3. 尝试不同的来源网站（必应、百度、谷歌）。

架构愿景：
1. 希望可以像`Scrapy`的流水线一样，不同来源的下载器可随意插拔和扩展。
2. 入口点只有一个`need_image_from()`函数。

## Installation 安装
```
pip install i-need-an-image
```

## Usage 使用方式

```python3
>>> from need_an_image import need_image_from

# Get PIL Image object
>>> need_image_from('bing', keyword='Tom')
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=800x1200 at 0x12594FE0EB0>

# Save image to disk
>>> need_image_from('bing', keyword='Tom', save_to='.')
'.\\2f65cbef7b8944cd93d21d434e566bf3.jpg'

```