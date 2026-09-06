"""Verify routes, local links/anchors, legacy content, and Markdown publishing."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / '_site'

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == 'img':
            assert 'alt' in attrs, 'Image missing alt text'

pages = {p: Document(p.read_text()) for p in OUTPUT.rglob('*.html')}
for page, document in pages.items():
    for link in document.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = ((OUTPUT / unquote(url.path.lstrip('/'))) if url.path.startswith('/')
                  else (page.parent / unquote(url.path))) if url.path else page
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        assert target.is_relative_to(OUTPUT), (page, link)
        assert target.is_file(), f'Broken local link: {page}: {link}'
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, f'Missing anchor: {link}'

for path, expected in json.loads((ROOT / 'scripts/fixtures/legacy-articles.json').read_text()).items():
    output = (OUTPUT / path).read_text()
    body = output.split('<div class="prose">', 1)[1].split('</div>\n  <div class="article-end">', 1)[0]
    # Eleventy retains the final source newline around the body.
    assert hashlib.sha256(body.rstrip('\n').encode()).hexdigest() == expected or hashlib.sha256((body.rstrip('\n')+'\n').encode()).hexdigest() == expected, f'Legacy article changed: {path}'
for path in ('index.html', 'archives/index.html', 'tags/OS/index.html'):
    assert (OUTPUT/path).is_file(), path
    assert '/2018/05/03/hello-world/' not in (OUTPUT/path).read_text()
assert not (OUTPUT/'examples/new-post/index.html').exists(), 'Example was published'

with tempfile.TemporaryDirectory(prefix='leon-markdown-') as folder:
    folder = Path(folder)
    source = folder / 'src'
    shutil.copytree(ROOT/'src', source)
    shutil.copy(ROOT/'examples/new-post.md', source/'posts/workflow-check.md')
    shutil.copy(ROOT/'eleventy.config.js', folder/'eleventy.config.js')
    shutil.copy(ROOT/'package.json', folder/'package.json')
    shutil.copytree(ROOT/'images', folder/'images')
    subprocess.run(['node', str(ROOT/'node_modules/@11ty/eleventy/cmd.cjs'),
                    '--output=output'], cwd=folder, check=True,
                    stdout=None, stderr=None)
    generated = (folder/'output/2026/09/06/workflow-check/index.html').read_text()
    assert '<h2>The question</h2>' in generated
    assert 'Hello, notebook' in generated and '<pre>' in generated
    assert '/2026/09/06/workflow-check/' in (folder/'output/archives/index.html').read_text()
    assert '/2026/09/06/workflow-check/' in (folder/'output/index.html').read_text()
print('PASS: existing routes, internal links and anchors, image alternatives, exact legacy bodies, and unpublished Markdown workflow.')
