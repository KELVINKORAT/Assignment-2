from aiohttp import web
import zipfile


async def handle(request):
    return web.Response(text='''<!DOCTYPE html>
<html>
<body>
    <h1>Web app to extract files from the zip file</h1>
    <h3>Upload a zip file</h3>
    <form enctype="multipart/form-data" action="Filename" method="post">
        <p><input type="file" name="filename" /></p>
        <p><input type="submit" value="Extract"/></p>
    </form>    
</body>
</html>''', content_type='text/html')


async def handle1(request):
    data = await request.post()
    zip_file = data['filename'].file
    with zipfile.ZipFile(zip_file, 'r') as z:
        extracted_files = z.namelist()
        html = "<ul>"
        for file in extracted_files:
            html += f"<li><a href='/{file}' download>{file}</a></li>"
        html += "</ul>"
        return web.Response(text=html, content_type="text/html")

app = web.Application()
app.router.add_get('/', handle)
app.router.add_post('/Filename', handle1)
web.run_app(app)
